"""Test imports for the Cosense Search Tool."""
import datetime
import json
import os
import sys
from typing import Any, Dict, List, Optional

# Load configuration from manifest.yaml first
import yaml
with open(os.path.join(os.path.dirname(__file__), "manifest.yaml"), "r") as f:
    manifest_data = yaml.safe_load(f)

# Import dify_plugin after setting up environment
import dify_plugin
from dify_plugin import Plugin, DifyPluginEnv
from dify_plugin.core.entities.plugin.setup import (
    PluginConfiguration,
    PluginResourceRequirements,
    PluginType,
    PluginArch,
    PluginLanguage,
)
from dify_plugin.entities import I18nObject
from dify_plugin.entities.tool import ToolInvokeMessage

from cosense_search_tool.tool_provider import CosenseSearchToolProvider

# Set up test configuration
os.environ["PYTHONPATH"] = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Convert manifest data to PluginConfiguration
test_config = PluginConfiguration(
    version=manifest_data["version"],
    type=PluginType.Plugin,
    author=manifest_data["author"],
    name=manifest_data["name"],
    description=I18nObject(**manifest_data["description"]),
    icon=manifest_data["icon"],
    label=I18nObject(**manifest_data["label"]),
    created_at=manifest_data["created_at"],
    resource=PluginResourceRequirements(
        memory=manifest_data["resource"]["memory"],
        permission=PluginResourceRequirements.Permission(
            tool=PluginResourceRequirements.Permission.Tool(
                enabled=manifest_data["resource"]["permission"]["tool"]["enabled"]
            )
        )
    ),
    plugins=PluginConfiguration.Plugins(
        tools=[os.path.splitext(t)[0] for t in manifest_data["plugins"]["tools"]]
    ),
    meta=PluginConfiguration.Meta(
        version=manifest_data["meta"]["version"],
        arch=[PluginArch(a) for a in manifest_data["meta"]["arch"]],
        runner=PluginConfiguration.Meta.PluginRunner(
            language=PluginLanguage(manifest_data["meta"]["runner"]["language"]),
            version=manifest_data["meta"]["runner"]["version"],
            entrypoint=manifest_data["meta"]["runner"]["entrypoint"]
        )
    )
)

# Set environment variables before creating plugin
try:
    print("✓ Basic imports (Plugin, DifyPluginEnv)")
    print("✓ ToolInvokeMessage from entities.tool")
    print("✓ I18nObject from entities")
    print("✓ CosenseSearchToolProvider import")
    
    # Create a test implementation of CosenseSearchToolProvider
    class TestCosenseSearchToolProvider(CosenseSearchToolProvider):
        def _validate_credentials(self) -> None:
            pass  # Mock implementation for testing
    
    # Verify runtime functionality
    provider = TestCosenseSearchToolProvider()
    message = ToolInvokeMessage(
        type="text",
        data={"test": "value"},
        message=ToolInvokeMessage.TextMessage(text="Test message")
    )
    i18n = I18nObject(en_US="test", ja_JP="テスト")
    
    # Set manifest configuration in environment before creating plugin
    manifest_json = test_config.model_dump_json()
    print("Debug - Manifest Configuration:", manifest_json[:100] + "...")  # Print first 100 chars
    os.environ["MANIFEST_CONFIGURATION"] = manifest_json
    print("Debug - Environment variable set:", "MANIFEST_CONFIGURATION" in os.environ)
    print("Debug - PYTHONPATH:", os.environ.get("PYTHONPATH", "not set"))
    
    # Initialize plugin with environment
    plugin = Plugin(DifyPluginEnv(
        MAX_REQUEST_TIMEOUT=30,
        INSTALL_METHOD="local"
    ))
    
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
