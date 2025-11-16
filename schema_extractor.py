import psycopg2
import json
from dotenv import load_dotenv
import os

load_dotenv()

class SchemaExtractor:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD'),
            database=os.getenv('POSTGRES_DATABASE', 'rims'),
            port=int(os.getenv('POSTGRES_PORT', 5432))
        )
        self.schema = os.getenv('POSTGRES_SCHEMA', 'qasequences')
    
    def get_all_tables(self):
        """Get all table names"""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = %s AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """, (self.schema,))
        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return tables
    
    def get_table_columns(self, table_name):
        """Get columns for a table"""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
            ORDER BY ordinal_position
        """, (self.schema, table_name))
        columns = [{'name': row[0], 'type': row[1]} for row in cursor.fetchall()]
        cursor.close()
        return columns
    
    def get_unique_values(self, table_name, column_name, limit=20):
        """Get sample unique values from a column"""
        try:
            cursor = self.connection.cursor()
            query = f"""
                SELECT DISTINCT {column_name}
                FROM {self.schema}.{table_name}
                WHERE {column_name} IS NOT NULL
                ORDER BY {column_name}
                LIMIT %s
            """
            cursor.execute(query, (limit,))
            values = [str(row[0]) for row in cursor.fetchall()]
            cursor.close()
            return values
        except Exception as e:
            print(f"  WARNING: Could not get values for {table_name}.{column_name}: {e}")
            return []
    
    def extract_full_schema(self):
        """Extract complete schema with sample values"""
        
        print("\n" + "="*80)
        print("DATABASE SCHEMA EXTRACTION")
        print("="*80 + "\n")
        
        tables = self.get_all_tables()
        print(f"Found {len(tables)} tables\n")
        
        full_schema = {}
        
        for i, table in enumerate(tables, 1):
            print(f"[{i}/{len(tables)}] Extracting {table}...")
            
            columns = self.get_table_columns(table)
            
            table_data = {
                'columns': [],
                'column_count': len(columns)
            }
            
            for col in columns:
                col_name = col['name']
                col_type = col['type']
                
                # Get sample values for text/name columns
                sample_values = []
                if any(keyword in col_type.lower() for keyword in ['char', 'text', 'varchar', 'string']):
                    sample_values = self.get_unique_values(table, col_name, limit=5)
                
                table_data['columns'].append({
                    'name': col_name,
                    'type': col_type,
                    'sample_values': sample_values
                })
            
            full_schema[table] = table_data
        
        return full_schema
    
    def export_to_json(self, schema, filename='database_schema.json'):
        """Export schema to JSON file"""
        with open(filename, 'w') as f:
            json.dump(schema, f, indent=2)
        print(f"\n✓ Schema exported to {filename}")
    
    def print_summary(self, schema):
        """Print readable summary"""
        print("\n" + "="*80)
        print("SCHEMA SUMMARY")
        print("="*80 + "\n")
        
        for table, data in schema.items():
            print(f"\n{table.upper()}")
            print("-" * 60)
            
            for col in data['columns']:
                print(f"  {col['name']:<30} {col['type']:<20}", end="")
                if col['sample_values']:
                    print(f" [Examples: {', '.join(col['sample_values'][:2])}]")
                else:
                    print()
    
    def export_to_python_dict(self, schema, filename='schema_metadata.py'):
        """Export schema as Python dictionary for easy access"""
        
        with open(filename, 'w') as f:
            f.write("# Auto-generated schema metadata\n\n")
            f.write("SCHEMA_METADATA = {\n")
            
            for table, data in schema.items():
                f.write(f"    '{table}': {{\n")
                f.write(f"        'columns': [\n")
                
                for col in data['columns']:
                    f.write(f"            {{\n")
                    f.write(f"                'name': '{col['name']}',\n")
                    f.write(f"                'type': '{col['type']}',\n")
                    f.write(f"                'examples': {col['sample_values']},\n")
                    f.write(f"            }},\n")
                
                f.write(f"        ]\n")
                f.write(f"    }},\n")
            
            f.write("}\n\n")
            f.write("# Table names\n")
            f.write(f"TABLE_NAMES = {list(schema.keys())}\n\n")
            f.write("# Column alias mappings\n")
            f.write("COLUMN_ALIASES = {\n")
            f.write("    'email': ['emailid', 'email', 'mailid'],\n")
            f.write("    'name': ['name', 'applicantname', 'contactname', 'productname'],\n")
            f.write("    'phone': ['telephonumber', 'phonenumber', 'mobile'],\n")
            f.write("    'address': ['country', 'region', 'location'],\n")
            f.write("}\n")
        
        print(f"✓ Python metadata exported to {filename}")
    
    def close(self):
        self.connection.close()


if __name__ == '__main__':
    print("Starting schema extraction...\n")
    
    extractor = SchemaExtractor()
    
    try:
        schema = extractor.extract_full_schema()
        
        extractor.print_summary(schema)
        
        extractor.export_to_json(schema, 'database_schema.json')
        
        extractor.export_to_python_dict(schema, 'schema_metadata.py')
        
        print("\n✓ Extraction complete!")
        
    finally:
        extractor.close()
