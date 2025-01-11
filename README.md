# Cosense Search Plugin for Dify

![Cosense Banner](./cosense_search_tool/_assets/cosense-banner.png)

A Dify plugin that enables seamless integration with Cosense's knowledge search capabilities.

## About Cosense

Cosense is a powerful knowledge management and collaboration platform that helps teams create, organize, and share information effectively. Key features include:

- **Intuitive Knowledge Creation**: Write and organize information with a wiki-like interface that supports rich text, code blocks, and media
- **Smart Linking**: Automatically connect related information and ideas across your knowledge base
- **Real-time Collaboration**: Work together with your team in real-time, seeing updates and changes instantly
- **Powerful Search**: Find information quickly with advanced search capabilities
- **Flexible Organization**: Create multiple projects for different teams or purposes
- **Public/Private Projects**: Support for both public knowledge sharing and private team documentation

The platform excels at helping teams build and maintain their knowledge bases, making information easily accessible and discoverable.

## Plugin Features

This Dify plugin integrates Cosense's powerful search capabilities into your AI workflows:

- Search across Cosense projects directly from Dify
- Access both public and private knowledge bases
- Get structured search results with titles and content
- Multilingual support (English/Japanese interface)

## Installation and Setup

1. Install the plugin through Dify Marketplace
2. Configure your project settings:
   - Project Name: The name of your Cosense project
   - Search Query: What you want to search for

### Authentication

This plugin supports both public and private Cosense projects:

- **Public Projects**: No authentication required. You can start searching immediately.
- **Private Projects**: Requires authentication via `connect.sid`:
  1. Log in to your Cosense account in your browser
  2. Access your browser's developer tools (usually F12)
  3. Go to the Application/Storage tab
  4. Find the `connect.sid` cookie under Cookies > scrapbox.io
  5. Copy the cookie value and use it for authentication

Note: The `connect.sid` value is only required when accessing private projects. For public projects, you can skip the authentication setup entirely.

## Usage Examples

The plugin accepts simple search parameters:

```json
{
  "project_name": "your-project",
  "query": "your search terms"
}
```

Example response:

```json
{
    "query": "API documentation",
    "project": "help-jp",
    "results": {
        "pages": [
            {"title": "REST API Guide", ...},
            {"title": "API Examples", ...}
        ]
    },
    "result_count": 2
}
```

---

![Cosense Logo](./cosense_search_tool/cosense-logo.png)

Built with ❤️ for the Cosense community
