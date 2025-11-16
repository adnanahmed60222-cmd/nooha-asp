import requests
import json
import os
from dotenv import load_dotenv
from schema_config import SCHEMA_METADATA, get_search_columns_for_table, get_sample_values_for_column, find_synonym_matches

load_dotenv()

class LLMHandler:
    def __init__(self, db_manager=None):
        self.ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        self.ollama_model = os.getenv('OLLAMA_MODEL', 'mistral')
        self.db_manager = db_manager
    
    def generate_sql_from_prompt(self, user_prompt, table_schema):
        """Generate SQL - production optimized"""
        
        print(f"DEBUG: User prompt: {user_prompt}")
        keywords = self._extract_keywords(user_prompt)
        print(f"DEBUG: Keywords: {keywords}")
        
        # Find matching table by importance
        best_table = self._find_best_table(keywords, table_schema)
        print(f"DEBUG: Best table: {best_table}")
        
        if not best_table:
            return f"SELECT * FROM applicationcontactdetails LIMIT 10"
        
        # Get columns to return
        select_columns = self._get_select_columns(best_table, keywords)
        
        # Build query
        return self._build_sql_query(best_table, select_columns, keywords)
    
    def _find_best_table(self, keywords, table_schema):
        """Find the most relevant table"""
        
        # Priority mapping
        important_tables = SCHEMA_METADATA["important_search_columns"]
        
        best_match = None
        best_score = 0
        
        for table, search_cols in important_tables.items():
            if table not in table_schema:
                continue
            
            score = 0
            for keyword in keywords:
                keyword_lower = keyword.lower()
                
                # Check if keyword matches table name
                if keyword_lower in table.lower():
                    score += 100
                
                # Check if keyword matches any search column
                for col in search_cols:
                    if keyword_lower in col.lower():
                        score += 50
                    if keyword_lower[:3] in col.lower()[:3]:
                        score += 20
            
            if score > best_score:
                best_score = score
                best_match = table
        
        # Fallback to top table
        if not best_match:
            best_match = list(SCHEMA_METADATA["important_search_columns"].keys())[0]
        
        return best_match
    
    def _get_select_columns(self, table, keywords):
        """Get columns that user is looking for"""
        
        search_cols = get_search_columns_for_table(table)
        
        # Check if user is asking for specific columns
        for keyword in keywords:
            syn = find_synonym_matches(keyword)
            if syn:
                # User asked for email, phone, etc.
                matching_cols = [col for col in search_cols if syn.lower() in col.lower()]
                if matching_cols:
                    return matching_cols
        
        # Return first 3 important search columns
        return search_cols[:3] if search_cols else ["*"]
    
    def _build_sql_query(self, table, select_columns, keywords):
        """Build final SQL query"""
        
        select_str = ", ".join(select_columns)
        
        # Find search term (filter out keywords like "of", "the", etc)
        name_keywords = [k for k in keywords if k not in 
                        {'email', 'phone', 'mobile', 'fax', 'number', 'id', 'list', 'show',
                         'emailid', 'telephonumber', 'contactid', 'query', 'of', 'the'}]
        
        if not name_keywords:
            return f"SELECT {select_str} FROM {table} LIMIT 20"
        
        search_term = " ".join(name_keywords)
        search_col = get_search_columns_for_table(table)[0] if get_search_columns_for_table(table) else None
        
        if not search_col:
            return f"SELECT {select_str} FROM {table} LIMIT 20"
        
        # Find actual value in samples
        actual_value = self._find_matching_value(table, search_col, search_term)
        
        if actual_value:
            query = f"SELECT {select_str} FROM {table} WHERE {search_col} ILIKE '%{actual_value}%' LIMIT 20"
        else:
            query = f"SELECT {select_str} FROM {table} WHERE {search_col} ILIKE '%{search_term}%' LIMIT 20"
        
        return query
    
    def _find_matching_value(self, table, column, search_term):
        """Find actual value using sample data"""
        
        samples = get_sample_values_for_column(table, column)
        
        if not samples:
            # Query database for samples
            if self.db_manager:
                samples = self.db_manager.get_sample_values(table, column, limit=20)
        
        if not samples:
            return None
        
        search_lower = search_term.lower()
        best_match = None
        best_score = 0
        
        for sample in samples:
            if not sample:
                continue
            
            sample_str = str(sample).lower()
            score = 0
            
            if search_lower == sample_str:
                score += 500
            if search_lower in sample_str:
                score += 100
            
            for part in search_lower.split():
                if part in sample_str:
                    score += 50
            
            if score > best_score:
                best_score = score
                best_match = sample
        
        if best_score > 30:
            return best_match
        
        return None
    
    def _extract_keywords(self, text):
        """Extract keywords"""
        import re
        
        stop_words = {'the', 'a', 'an', 'is', 'are', 'am', 'be', 'been', 'being',
                      'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                      'could', 'should', 'may', 'might', 'must', 'can', 'i', 'you',
                      'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'where',
                      'when', 'why', 'how', 'of', 'in', 'on', 'at', 'by', 'to', 'for',
                      'and', 'or', 'not', 'if', 'as', 'from', 'with', 'that', 'this',
                      'just', 'want', 'get', 'show', 'list', 'find', 'give', 'me',
                      'all', 'any', 'please', 'request'}
        
        text_clean = re.sub(r'[^a-z0-9\s]', '', text.lower())
        words = text_clean.split()
        
        keywords = [w for w in words if len(w) > 1 and w not in stop_words]
        
        return keywords
    
    def format_query_results(self, results, user_prompt):
        if not results:
            return "No results found."
        return f"Found {len(results)} results."
