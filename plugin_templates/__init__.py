def templates():
    from toolbutton_with_dialog.plugin_template import ToolbuttonWithDialogPluginTemplate
    from processing_provider.plugin_template import ProcessingProviderPluginTemplate
    return [
        ToolbuttonWithDialogPluginTemplate(),
        ProcessingProviderPluginTemplate()
    ]
