import datetime

from dify_plugin.core.entities.plugin.setup import (
    PluginConfiguration,
    PluginResourceRequirements,
    PluginType,
    PluginArch,
    PluginLanguage,
)
from dify_plugin.entities import I18nObject
from .tool_provider import CosenseSearchToolProvider

# Initialize the tool provider
tool_provider = CosenseSearchToolProvider()

manifest = PluginConfiguration(
    version="1.0.0",
    type=PluginType.Plugin,
    author="teramotodaiki",
    name="cosense-search-tool",
    description=I18nObject(
        en_US="Cosense read-only search integration",
        ja_JP="Cosense の読み取り専用検索インテグレーション"
    ),
    icon="cosense-logo.png",
    label=I18nObject(
        en_US="Cosense Search",
        ja_JP="Cosense 検索"
    ),
    created_at=datetime.datetime.now(),
    resource=PluginResourceRequirements(
        memory=1048576,
        permission=PluginResourceRequirements.Permission(
            tool=PluginResourceRequirements.Permission.Tool(enabled=True)
        )
    ),
    plugins=PluginConfiguration.Plugins(
        tools=["cosense_search"]
    ),
    meta=PluginConfiguration.Meta(
        version="1.0.0",
        arch=[PluginArch.AMD64, PluginArch.ARM64],
        runner=PluginConfiguration.Meta.PluginRunner(
            language=PluginLanguage.PYTHON,
            version="3.12",
            entrypoint="main"
        )
    )
)
