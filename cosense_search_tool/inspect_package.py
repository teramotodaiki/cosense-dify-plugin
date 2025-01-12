"""Script to inspect dify_plugin package structure."""
import inspect
import pkgutil
import sys
from typing import Any, Dict, List, Optional, Type

import dify_plugin

def inspect_module(module: Any, indent: str = "") -> None:
    """Inspect and print module contents."""
    print(f"{indent}Module: {module.__name__}")
    print(f"{indent}Path: {getattr(module, '__path__', 'N/A')}")
    
    if module.__doc__:
        print(f"{indent}Documentation:")
        print(f"{indent}  {module.__doc__.strip()}")
    
    print(f"{indent}Classes:")
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__.startswith(module.__name__):
            print(f"{indent}  - {name}")
            if obj.__doc__:
                doc = obj.__doc__.strip().split('\n')[0]  # First line only
                print(f"{indent}    {doc}")

def list_modules() -> None:
    """List and inspect all dify_plugin modules."""
    print("=== Listing dify_plugin modules ===")
    
    # Get the root package
    print("\nRoot Package Info:")
    inspect_module(dify_plugin)
    
    print("\nSubmodules:")
    for finder, name, ispkg in pkgutil.iter_modules(dify_plugin.__path__):
        try:
            # Import the module
            module = __import__(f"{dify_plugin.__name__}.{name}", fromlist=["*"])
            print(f"\nFound submodule: {name}")
            inspect_module(module, indent="  ")
        except Exception as e:
            print(f"Error loading module {name}: {e}")

if __name__ == "__main__":
    try:
        list_modules()
    except Exception as e:
        print(f"Error inspecting dify_plugin: {e}", file=sys.stderr)
        sys.exit(1)
