import os
import json
from typing import Optional

from cosense_search import cosense_search, CosenseSearchError

def test_search_basic_functionality() -> bool:
    """Test basic search functionality with environment credentials"""
    try:
        # Test with public project
        results = cosense_search(
            project_name="help-jp",
            query="API"
        )
        
        print("\n=== Basic Search Test ===")
        print(f"Query: 'API' in project 'help-jp'")
        print(f"Results found: {len(results.get('pages', []))}")
        print("Sample results:")
        for page in results.get('pages', [])[:3]:  # Show first 3 results
            print(f"- {page.get('title', 'No title')}")
            
        return True
            
    except CosenseSearchError as e:
        print(f"\nSearch error: {e}")
        return False
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return False

def test_search_parameter_validation() -> bool:
    """Test parameter validation"""
    print("\n=== Parameter Validation Test ===")
    
    try:
        # Test with empty project name
        cosense_search("", "test")
        print("❌ Empty project name validation failed")
        return False
    except ValueError:
        print("✓ Empty project name correctly rejected")
        
    try:
        # Test with empty query
        cosense_search("help-jp", "")
        print("❌ Empty query validation failed")
        return False
    except ValueError:
        print("✓ Empty query correctly rejected")
        
    return True

def main() -> None:
    """Run all tests"""
    print("\nRunning Cosense Search Tests...")
    print("Using environment credentials for authentication")
    
    # Check if we have credentials
    connect_sid = os.environ.get("Cosense_Login_Credential_connect_sid")
    if not connect_sid:
        print("⚠️  Warning: No connect.sid found in environment variables")
    
    # Run tests
    basic_test = test_search_basic_functionality()
    param_test = test_search_parameter_validation()
    
    # Summary
    print("\n=== Test Summary ===")
    print(f"Basic functionality test: {'✓ Passed' if basic_test else '❌ Failed'}")
    print(f"Parameter validation test: {'✓ Passed' if param_test else '❌ Failed'}")
    
if __name__ == "__main__":
    main()
