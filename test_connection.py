import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

print("Testing PostgreSQL Connection...")
print("-" * 50)

try:
    connection = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DATABASE'),
        port=os.getenv('POSTGRES_PORT')
    )
    
    print("✅ SUCCESS! Connected to PostgreSQL")
    
    # Test if schema exists
    cursor = connection.cursor()
    cursor.execute("""
        SELECT schema_name 
        FROM information_schema.schemata 
        WHERE schema_name = %s
    """, (os.getenv('POSTGRES_SCHEMA'),))
    
    result = cursor.fetchone()
    
    if result:
        print(f"✅ Schema '{os.getenv('POSTGRES_SCHEMA')}' exists")
    else:
        print(f"⚠️ Schema '{os.getenv('POSTGRES_SCHEMA')}' NOT FOUND")
    
    # Count tables
    cursor.execute("""
        SELECT COUNT(*) 
        FROM information_schema.tables 
        WHERE table_schema = %s
    """, (os.getenv('POSTGRES_SCHEMA'),))
    
    table_count = cursor.fetchone()[0]
    print(f"✅ Found {table_count} tables in schema")
    
    cursor.close()
    connection.close()
    
    print("-" * 50)
    print("✅ All tests passed! Ready to run chatbot")
    
except psycopg2.Error as e:
    print(f"❌ ERROR: {e}")
    print("-" * 50)
    print("Troubleshooting:")
    print(f"  1. Check password in .env")
    print(f"  2. Make sure PostgreSQL is running")
    print(f"  3. Verify 'rims' database exists in pgAdmin")
    
except FileNotFoundError:
    print("❌ .env file not found!")
    print("Create .env file in your chatbot folder")
    
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")
