"""Test imports for the Cosense Search Tool."""
import sys
from typing import Any, Dict, List, Optional

try:
    # Test basic dify_plugin imports
    import dify_plugin
    from dify_plugin import Plugin, DifyPluginEnv
    print("✓ Basic imports (Plugin, DifyPluginEnv)")
    
    # Test tool imports
    from dify_plugin.entities.tool import ToolInvokeMessage
    print("✓ ToolInvokeMessage from entities.tool")
    
    # Test I18nObject import
    from dify_plugin.entities import I18nObject
    print("✓ I18nObject from entities")
    
    # Import our concrete provider
    from tool_provider import CosenseSearchToolProvider
    print("✓ CosenseSearchToolProvider import")
    
    # Verify runtime functionality
    provider = CosenseSearchToolProvider()
    message = ToolInvokeMessage(type="text", data={})
    i18n = I18nObject(en_US="test", ja_JP="テスト")
    plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=30))
    
    # Verify object attributes
    assert message.type == "text", "Invalid ToolInvokeMessage type"
    assert i18n.en_US == "test", "Invalid I18nObject en_US value"
    assert isinstance(provider, CosenseSearchToolProvider), "Invalid CosenseSearchToolProvider instance"
    assert plugin.env.MAX_REQUEST_TIMEOUT == 30, "Invalid Plugin configuration"
    
    print("All imports and runtime checks passed!")
    sys.exit(0)
    
except ImportError as e:
    print(f"Import error: {e}", file=sys.stderr)
    print("Please check that all required packages are installed and import paths are correct", file=sys.stderr)
    sys.exit(1)
except AssertionError as e:
    print(f"Verification error: {e}", file=sys.stderr)
    print("Please check that all objects are properly initialized", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}", file=sys.stderr)
    sys.exit(1)
