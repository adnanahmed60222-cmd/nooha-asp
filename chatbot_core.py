from database import DatabaseManager
from preprocessor import TextPreprocessor
from llm_handler import LLMHandler


class Chatbot:
    def __init__(self):
        self.db = DatabaseManager()
        self.preprocessor = TextPreprocessor()
        self.llm_handler = None
        self.is_connected = False

    def initialize(self):
        try:
            if self.db.connect():
                self.llm_handler = LLMHandler(db_manager=self.db)
                self.is_connected = True
                print("✓ Chatbot initialized successfully")
                return True
            else:
                print("✗ Failed to connect to database")
                return False
        except Exception as e:
            print(f"✗ Error: {e}")
            return False

    def process_message(self, user_prompt):
        
        if not self.is_connected:
            return {'success': False, 'message': 'Not connected', 'data': None}

        try:
            if not self.db.connection:
                if not self.db.connect():
                    return {'success': False, 'message': 'Connection lost', 'data': None}
            
            schema = self.db.get_full_schema()
            
            if not schema:
                return {'success': False, 'message': 'No schema', 'data': None}
            
            print(f"\n>>> User: {user_prompt}")
            sql_query = self.llm_handler.generate_sql_from_prompt(user_prompt, schema)
            print(f">>> SQL: {sql_query}\n")
            
            results = self.db.execute_query(sql_query)
            
            if results is None:
                return {
                    'success': False,
                    'message': 'Query failed',
                    'data': None,
                    'sql': sql_query
                }
            
            if len(results) == 0:
                return {
                    'success': False,
                    'message': 'No data found',
                    'data': None,
                    'sql': sql_query
                }
            
            # Deduplicate and format results
            unique_results = self._deduplicate_results(results)
            response_text = self._format_response(unique_results)
            
            return {
                'success': True,
                'message': response_text,
                'data': unique_results,
                'count': len(unique_results),
                'sql': sql_query
            }

        except Exception as e:
            print(f"✗ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            return {
                'success': False,
                'message': f'Error: {str(e)}',
                'data': None
            }
    
    def _deduplicate_results(self, results):
        """Remove duplicate rows"""
        if not results:
            return []
        
        seen = set()
        unique = []
        
        for row in results:
            if isinstance(row, dict):
                # Convert dict to tuple for hashing
                row_tuple = tuple(sorted(row.items()))
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    unique.append(row)
            else:
                if row not in seen:
                    seen.add(row)
                    unique.append(row)
        
        return unique
    
    def _format_response(self, results):
        """Format results for clean display"""
        if not results:
            return "No results found."
        
        if len(results) == 1:
            result = results[0]
            return self._format_single_row(result)
        else:
            return self._format_multiple_rows(results)
    
    def _format_single_row(self, row):
        """Format single row - show only values"""
        if isinstance(row, dict):
            values = []
            for key, value in row.items():
                if value is not None:
                    values.append(str(value))
            return " | ".join(values)
        return str(row)
    
    def _format_multiple_rows(self, rows):
        """Format multiple rows cleanly"""
        output = ""
        
        for i, row in enumerate(rows, 1):
            if isinstance(row, dict):
                values = []
                for key, value in row.items():
                    if value is not None:
                        values.append(str(value))
                output += " | ".join(values)
            else:
                output += str(row)
            
            if i < len(rows):
                output += "\n"
        
        return output

    def close(self):
        try:
            if self.db:
                self.db.close()
        except Exception as e:
            print(f"Error closing: {e}")
