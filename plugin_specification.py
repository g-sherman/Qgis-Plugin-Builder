# coding=utf-8
"""
/***************************************************************************
    PluginSpec

    Creates a skeleton QGIS plugin for use as a starting point
                             -------------------
        begin                : 2011-01-20
        git sha              : $Format:%H$
        copyright            : (C) 2011-2014 by GeoApt LLC
        email                : gsherman@geoapt.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


class PluginSpecification(object):
    """A convenience store with information needed to create the plugin."""
    def __init__(self, dialog):
        """Constructor.

        After calling the constructor, the class properties
        self.template_map, self.experimental etc. will be set.

        :param dialog: A plugin builder dialog with populated options.
        :type dialog: PluginBuilderDialog

        """
        self.class_name = str(dialog.class_name.text())
        self.author = dialog.author.text()
        self.description = dialog.description.text()
        self.module_name = dialog.module_name.text()
        self.email_address = dialog.email_address.text()
        self.menu_text = dialog.menu_text.text()
        self.qgis_minimum_version = dialog.qgis_minimum_version.text()
        self.title = dialog.title.text()
        self.plugin_version = dialog.plugin_version.text()
        self.homepage = dialog.homepage.text()
        self.tracker = dialog.tracker.text()
        self.repository = dialog.repository.text()
        self.tags = dialog.tags.text()
        # icon selection from disk will be added at a later version
        self.icon = 'icon.png'
        self.experimental = dialog.experimental.isChecked()
        # deprecated is always false for a new plugin
        self.deprecated = False

        self.template_map = {
            'TemplateClass': self.class_name,
            'TemplateTitle': self.title,
            'TemplateDescription': self.description,
            'TemplateModuleName': self.module_name,
            'TemplateVersion': self.plugin_version,
            'TemplateQgisVersion': self.qgis_minimum_version,
            'TemplateAuthor': self.author,
            'TemplateEmail': self.email_address,
            'TemplateMenuText': self.menu_text,
            'PluginDirectoryName': self.class_name.lower()
        }
