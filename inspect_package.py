"""Script to inspect dify_plugin package structure."""
import inspect
import pkgutil
import dify_plugin

def inspect_package(package):
    """Inspect and print package structure."""
    print(f"=== {package.__name__} Package Structure ===")
    print("\nPackage Help:")
    help(package)
    
    print("\nSubmodules:")
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        print(f"- {name}")
        try:
            module = getattr(__import__(f"{package.__name__}.{name}"), name)
            print(f"  Classes:")
            for item_name, item in inspect.getmembers(module):
                if inspect.isclass(item) and item.__module__.startswith(package.__name__):
                    print(f"    - {item_name}")
        except Exception as e:
            print(f"  Error loading module: {e}")

if __name__ == "__main__":
    inspect_package(dify_plugin)
