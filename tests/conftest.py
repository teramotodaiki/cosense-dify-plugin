"""Pytest configuration and fixtures for Cosense Dify Plugin tests."""
import os
import sys
from pathlib import Path

# Add the root directory to PYTHONPATH for imports
root_dir = str(Path(__file__).parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
