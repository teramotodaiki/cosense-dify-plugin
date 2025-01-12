"""Plugin-specific test fixtures and configuration."""
import os
import pytest
from pathlib import Path

@pytest.fixture
def plugin_root():
    """Return the root directory of the plugin package."""
    return Path(__file__).parent.parent.parent / "cosense_search_tool"

@pytest.fixture
def manifest_path(plugin_root):
    """Return the path to the manifest.yaml file."""
    return plugin_root / "manifest.yaml"
