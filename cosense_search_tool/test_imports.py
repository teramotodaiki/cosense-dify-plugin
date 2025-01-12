"""Test imports for the Cosense Search Tool."""
import sys
from typing import Any, Dict, List, Optional

try:
    # Test basic dify_plugin imports
    import dify_plugin
    from dify_plugin import Plugin, DifyPluginEnv, ToolProvider
    print("✓ Basic imports (Plugin, DifyPluginEnv, ToolProvider)")
    
    # Test tool imports
    from dify_plugin.entities.tool import ToolInvokeMessage
    print("✓ ToolInvokeMessage from entities.tool")
    
    # Test I18nObject import
    from dify_plugin.entities import I18nObject
    print("✓ I18nObject from entities")
    
    # Verify runtime functionality
    provider = ToolProvider()
    message = ToolInvokeMessage(type="text", data={})
    i18n = I18nObject(en_US="test", ja_JP="テスト")
    plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=30))
    
    # Verify object attributes
    assert message.type == "text", "Invalid ToolInvokeMessage type"
    assert i18n.en_US == "test", "Invalid I18nObject en_US value"
    assert isinstance(provider, ToolProvider), "Invalid ToolProvider instance"
    assert plugin.env.MAX_REQUEST_TIMEOUT == 30, "Invalid Plugin configuration"
    
    print("All imports and runtime checks passed!")
    sys.exit(0)
    
except Exception as e:
    print(f"Import error: {e}", file=sys.stderr)
    sys.exit(1)
