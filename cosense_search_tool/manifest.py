import datetime

from core.plugin.entities.plugin import PluginDeclaration, PluginResourceRequirements, PluginCategory
from core.tools.entities.common_entities import I18nObject
from .tool_provider import CosenseSearchToolProvider

# Initialize the tool provider
tool_provider = CosenseSearchToolProvider()

manifest = PluginDeclaration(
    version="0.1.0",
    author="teramotodaiki",
    name="cosense-search-tool",
    description=I18nObject(
        en="Cosense read-only search integration",
        ja="Cosense の読み取り専用検索インテグレーション"
    ),
    icon="",  # TODO: Add icon
    label=I18nObject(
        en="Cosense Search",
        ja="Cosense 検索"
    ),
    category=PluginCategory.Tool,
    created_at=datetime.datetime.now(),
    resource=PluginResourceRequirements(
        memory=256,
        permission=PluginResourceRequirements.Permission(
            tool=PluginResourceRequirements.Permission.Tool(enabled=True)
        )
    ),
    plugins=PluginDeclaration.Plugins(tools=["cosense_search"]),
    tags=["search", "knowledge-base", "cosense"],
    verified=False,
    tool=tool_provider
)
