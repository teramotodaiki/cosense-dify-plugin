# Cosense Search Tool Plugin for Dify

A read-only search integration plugin for Dify that enables searching Cosense (formerly Scrapbox) projects.

## Features

- Search across Cosense projects using the official API
- Read-only integration (search only, no write operations)
- Support for multiple projects
- Cookie-based authentication

## Configuration

### Authentication

The plugin uses cookie-based authentication with Cosense. You need to set up the `connect.sid` cookie value in your environment:

1. Set the environment variable:
```bash
export Cosense_Login_Credential_connect_sid="your_connect_sid_value"
```

2. Or configure it in your Dify settings when installing the plugin.

### Parameters

The tool accepts two required parameters:

1. `project_name` (必須 / Required)
   - The name of the Cosense project to search in
   - Example: "help-jp" for searching in https://scrapbox.io/help-jp/

2. `query` (必須 / Required)
   - The search query string
   - Supports Cosense's search syntax
   - Example: "API" to search for pages containing "API"

## Usage Example

```python
# Example of how the tool is invoked
result = tool.invoke(
    user_id="user123",
    tool_parameters={
        "project_name": "help-jp",
        "query": "API"
    }
)
```

## Important Notes

- This is a **read-only** integration. It cannot create, modify, or delete pages.
- The search API is an internal Cosense API and may change without notice.
- Make sure to keep your `connect.sid` cookie value secure and up to date.
- The plugin requires proper authentication to access private projects.

## Response Format

The tool returns search results in the following format:

```json
{
    "query": "your search query",
    "project": "project_name",
    "results": {
        "pages": [
            {
                "title": "Page Title",
                "updated": "timestamp",
                "accessed": "timestamp",
                // other page metadata...
            }
        ]
    },
    "result_count": 42
}
```

## Error Handling

The plugin handles various error cases:

- Authentication errors (invalid or expired connect.sid)
- Missing required parameters
- Network connectivity issues
- API response errors

Error messages are returned in both English and Japanese where applicable.

## Development

This plugin is part of the Dify plugin system (beta). For more information about developing Dify plugins, please refer to the [Dify Plugin Documentation](https://github.com/langgenius/dify/tree/plugins/beta).
