from typing import Any, Dict, List, Optional

from dify_plugin import ToolProvider
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities import I18nObject

from .cosense_search import cosense_search, CosenseSearchError

class CosenseSearchToolProvider(ToolProvider):
    type = "CUSTOM"
    name: str = "cosense_search"
    
    def _validate_credentials(self) -> None:
        """Validate the credentials for the Cosense search tool."""
        # No credentials needed for read-only search
        pass
        
    description: I18nObject = I18nObject(
        en_US="Search Cosense pages across projects",
        ja_JP="Cosense のページを検索"
    )
    parameters: List[Dict[str, Any]] = [
        {
            "name": "project_name",
            "type": "string",
            "required": True,
            "label": I18nObject(
                en_US="Project Name",
                ja_JP="プロジェクト名"
            ),
            "description": I18nObject(
                en_US="Name of the Cosense project to search in",
                ja_JP="検索対象のCosenseプロジェクト名"
            )
        },
        {
            "name": "query",
            "type": "string",
            "required": True,
            "label": I18nObject(
                en_US="Search Query",
                ja_JP="検索クエリ"
            ),
            "description": I18nObject(
                en_US="Search terms to look for in the project",
                ja_JP="プロジェクト内で検索するキーワード"
            )
        }
    ]

    def invoke(self, user_id: str, tool_parameters: Dict[str, Any], **kwargs) -> ToolInvokeMessage:
        """
        Invoke the Cosense search tool with the given parameters.
        
        Args:
            user_id: The ID of the user invoking the tool
            tool_parameters: Dictionary containing project_name and query
            **kwargs: Additional keyword arguments
            
        Returns:
            ToolInvokeMessage containing the search results
            
        Raises:
            ValueError: If required parameters are missing
            CosenseSearchError: If the search request fails
        """
        try:
            project_name = tool_parameters.get("project_name")
            query = tool_parameters.get("query")
            
            if not project_name or not query:
                raise ValueError("Both project_name and query parameters are required")
            
            results = cosense_search(project_name=project_name, query=query)
            
            # Format the results for display
            formatted_results = {
                "query": query,
                "project": project_name,
                "results": results,
                "result_count": len(results.get("pages", [])) if results.get("pages") else 0
            }
            
            return ToolInvokeMessage(
                type="text",
                data=formatted_results,
                message=ToolInvokeMessage.TextMessage(text=f"Found {formatted_results['result_count']} results for '{query}' in project '{project_name}'")
            )
            
        except (ValueError, CosenseSearchError) as e:
            return ToolInvokeMessage(
                type="error",
                data={"error": str(e)},
                message=ToolInvokeMessage.TextMessage(text=str(e))
            )
