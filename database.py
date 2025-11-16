import psycopg2
import psycopg2.extras
from psycopg2 import Error
from config import Config


class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.schema = Config.POSTGRES_SCHEMA
        self.all_tables_cache = None
        self.all_columns_cache = None
        self.column_search_cache = None
        
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = psycopg2.connect(
                host=Config.POSTGRES_HOST,
                user=Config.POSTGRES_USER,
                password=Config.POSTGRES_PASSWORD,
                database=Config.POSTGRES_DATABASE,
                port=Config.POSTGRES_PORT
            )
            print("Successfully connected to PostgreSQL database")
            return True
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return False
    
    def execute_query(self, query, params=None):
        """Execute a SELECT query and return results"""
        try:
            query = self._add_schema_prefix(query)
            print(f"Executing query: {query}")
            cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            results = cursor.fetchall()
            cursor.close()
            print(f"Query returned {len(results)} rows")
            return results
        except Error as e:
            print(f"Error executing query: {e}")
            print(f"Failed query was: {query}")
            return None
    
    def _add_schema_prefix(self, query):
        """Add schema prefix to table names"""
        schema_name = self.schema
        tables = self.get_all_tables()
        
        for table in tables:
            patterns = [f" {table}", f"({table}", f"\n{table}", f"JOIN {table}"]
            for pattern in patterns:
                if pattern in query:
                    replacement = pattern.replace(table, f"{schema_name}.{table}")
                    if replacement not in query:
                        query = query.replace(pattern, replacement)
        
        return query
    
    def get_table_schema(self, table_name):
        """Get column information for a table"""
        try:
            cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            query = """
                SELECT column_name as "Field", data_type as "Type", is_nullable as "Null"
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                ORDER BY ordinal_position
            """
            cursor.execute(query, (self.schema, table_name))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error getting schema for {table_name}: {e}")
            return None
    
    def get_all_tables(self):
        """Get all table names"""
        if self.all_tables_cache:
            return self.all_tables_cache
        
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s AND table_type = 'BASE TABLE'
                ORDER BY table_name
            """
            cursor.execute(query, (self.schema,))
            results = cursor.fetchall()
            cursor.close()
            if results:
                self.all_tables_cache = [row[0] for row in results]
                return self.all_tables_cache
            return []
        except Error as e:
            print(f"Error getting table list: {e}")
            return []
    
    def get_all_columns_map(self):
        """Get all tables and their columns"""
        if self.all_columns_cache:
            return self.all_columns_cache
        
        tables = self.get_all_tables()
        columns_map = {}
        
        for table in tables:
            schema = self.get_table_schema(table)
            if schema:
                col_names = [col.get('Field') or col.get('column_name') for col in schema]
                columns_map[table] = col_names
        
        self.all_columns_cache = columns_map
        return columns_map
    
    def search_column_by_keyword(self, keyword):
        """Find column name that matches keyword - VERY fuzzy"""
        columns_map = self.get_all_columns_map()
        keyword_lower = keyword.lower()
        
        best_match = None
        best_score = 0
        best_table = None
        
        for table, cols in columns_map.items():
            for col in cols:
                col_lower = col.lower()
                
                score = 0
                if keyword_lower in col_lower:
                    score += 100
                if col_lower in keyword_lower:
                    score += 100
                if keyword_lower.replace(' ', '') in col_lower.replace('_', ''):
                    score += 50
                if col_lower.startswith(keyword_lower):
                    score += 30
                
                if score > best_score:
                    best_score = score
                    best_match = col
                    best_table = table
        
        print(f"DEBUG: Keyword '{keyword}' -> Column '{best_match}' in table '{best_table}' (score: {best_score})")
        return best_table, best_match if best_score > 0 else (None, None)
    
    def find_matching_tables(self, keywords):
        """Find tables matching keywords"""
        columns_map = self.get_all_columns_map()
        matching_tables = {}
        
        keywords_lower = [k.lower() for k in keywords]
        
        for table, columns in columns_map.items():
            columns_lower = [c.lower() for c in columns]
            
            matches = 0
            for keyword in keywords_lower:
                for col in columns_lower:
                    if keyword in col or col in keyword:
                        matches += 1
            
            if matches > 0:
                matching_tables[table] = {
                    'matches': matches,
                    'columns': columns
                }
        
        sorted_tables = sorted(matching_tables.items(), key=lambda x: x[1]['matches'], reverse=True)
        return dict(sorted_tables)
    
    def get_sample_values(self, table_name, column_name, limit=3):
        """Get sample values from column"""
        try:
            query = f"SELECT DISTINCT {column_name} FROM {self.schema}.{table_name} WHERE {column_name} IS NOT NULL LIMIT %s"
            cursor = self.connection.cursor()
            cursor.execute(query, (limit,))
            results = cursor.fetchall()
            cursor.close()
            return [row[0] for row in results if row[0]]
        except Error as e:
            print(f"Error getting sample values: {e}")
            return []
    
    def get_table_relationships(self):
        """Get foreign key relationships"""
        try:
            cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            query = """
                SELECT
                    tc.table_name as table_name,
                    kcu.column_name as column_name,
                    ccu.table_name as foreign_table_name,
                    ccu.column_name as foreign_column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage ccu
                    ON ccu.constraint_name = tc.constraint_name
                    AND ccu.table_schema = tc.table_schema
                WHERE tc.constraint_type = 'FOREIGN KEY'
                    AND tc.table_schema = %s
            """
            cursor.execute(query, (self.schema,))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error getting relationships: {e}")
            return []
    
    def get_relationships_map(self):
        """Get relationships as map"""
        relationships = self.get_table_relationships()
        rel_map = {}
        
        for rel in relationships:
            table = rel.get('table_name')
            col = rel.get('column_name')
            foreign_table = rel.get('foreign_table_name')
            foreign_col = rel.get('foreign_column_name')
            
            if table not in rel_map:
                rel_map[table] = []
            
            rel_map[table].append({
                'column': col,
                'references': f"{foreign_table}.{foreign_col}"
            })
        
        return rel_map
    
    def get_full_schema(self):
        """Get complete schema"""
        schema = {}
        tables = self.get_all_tables()
        print(f"Found tables: {tables}")
        for table in tables:
            schema[table] = self.get_table_schema(table)
        return schema
    
    def close(self):
        """Close connection"""
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection closed")
