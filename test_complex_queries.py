
from chatbot_core import Chatbot


def test_complex_queries():
    """Test chatbot with complex join queries"""
    
    print("COMPLEX QUERY TESTING SUITE")
    print("=" * 70)
    
    chatbot = Chatbot()
    
    if not chatbot.initialize():
        print("❌ Failed to initialize chatbot")
        return False
    
    print("✓ Chatbot initialized successfully")
    
    # Test queries for non-technical users
    test_queries = [
        # Simple queries
        "Show me all applications",
        "List all contacts",
        
        # Filters
        "Show me applications from 2024",
        "Find all contacts with email",
        
        # Complex joins (adapt to your actual schema)
        "Show me applications with their contact details",
        "List all applications and the contact information associated with them",
        "Show applications grouped by contact type",
        
        # Aggregations
        "How many applications do we have",
        "Count the number of unique contacts",
    ]
    
    passed = 0
    failed = 0
    
    for query in test_queries:
        print(f"\n{'='*70}")
        print(f"Query: {query}")
        print(f"{'='*70}")
        response = chatbot.process_message(query)
        
        if response.get('success'):
            print(f"✓ SUCCESS")
            print(f"Generated SQL: {response.get('sql', 'N/A')}")
            print(f"Results: {response.get('count', 0)} rows")
            print(f"Summary: {response.get('message', 'N/A')[:200]}...")
            passed += 1
        else:
            print(f"❌ FAILED")
            print(f"Error: {response.get('message')}")
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"✅ Passed: {passed}/{len(test_queries)}")
    print(f"❌ Failed: {failed}")
    
    chatbot.close()
    
    return failed == 0


if __name__ == "__main__":
    test_complex_queries()
