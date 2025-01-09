import os
from typing import Dict, List, Optional, Union

import requests
from requests.exceptions import RequestException

class CosenseSearchError(Exception):
    """Custom exception for Cosense search errors"""
    pass

def cosense_search(
    project_name: str,
    query: str,
    *,
    connect_sid: Optional[str] = None
) -> Dict[str, Union[List[Dict], str]]:
    """
    Search Cosense pages using the search API.
    
    Args:
        project_name (str): Name of the Cosense project to search in
        query (str): Search query string
        connect_sid (Optional[str]): Override for connect.sid cookie. If None, uses environment variable
    
    Returns:
        Dict containing search results from Cosense API
    
    Raises:
        CosenseSearchError: If the search request fails
        ValueError: If required parameters are missing
    """
    if not project_name or not query:
        raise ValueError("Both project_name and query are required")

    # Get connect.sid from environment if not provided
    cookie = connect_sid or os.environ.get("Cosense_Login_Credential_connect_sid")
    if not cookie:
        raise CosenseSearchError("No connect.sid cookie found in environment variables")

    base_url = f"https://scrapbox.io/api/pages/{project_name}/search/query"
    
    headers = {
        "Cookie": f"connect.sid={cookie}",
        "Accept": "application/json"
    }
    
    params = {
        "q": query
    }
    
    try:
        response = requests.get(
            base_url,
            headers=headers,
            params=params,
            timeout=10  # 10 second timeout
        )
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise CosenseSearchError(f"Search request failed: {str(e)}")
