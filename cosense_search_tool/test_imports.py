"""Test imports for the Cosense Search Tool."""
from typing import Any, Dict, List, Optional

# Test dify_plugin imports
from dify_plugin import Plugin, ToolProvider
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.i18n import I18nObject

def test_imports() -> None:
    """Test that all required imports are available."""
    # Type annotations to verify imports
    provider: ToolProvider
    message: ToolInvokeMessage
    i18n: I18nObject
    plugin: Plugin
