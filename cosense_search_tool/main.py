from dify_plugin import Plugin, DifyPluginEnv
from tool_provider import CosenseSearchToolProvider

plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=30))

if __name__ == "__main__":
    plugin.run()
