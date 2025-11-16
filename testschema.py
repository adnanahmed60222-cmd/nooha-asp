import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DATABASE'),
        port=os.getenv('POSTGRES_PORT')
    )
    
    cursor = conn.cursor()
    
    # Check what schema name is correct
    cursor.execute("SELECT schema_name FROM information_schema.schemata;")
    schemas = cursor.fetchall()
    print("Available schemas:")
    for schema in schemas:
        print(f"  - {schema[0]}")
    
    # Try to get tables from qasesequences
    cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'qasesequences'
    """)
    tables = cursor.fetchall()
    print(f"\nTables in 'qasesequences': {len(tables)}")
    for table in tables[:5]:
        print(f"  - {table[0]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"ERROR: {e}")
