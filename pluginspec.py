"""
/***************************************************************************
    PluginSpec

    Creates a skeleton QGIS plugin for use as a starting point
                             -------------------
        begin                : 2011-01-20
        copyright            : (C) 2011 by GeoApt LLC
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
from string import capwords

# Class to store all information needed to create the plugin
class PluginSpec:

    def __init__(self, ui):
        self.class_name = str(ui.lineEdit_class_name.text())
        self.author = ui.lineEdit_company_name.text()
        self.description = ui.lineEdit_description.text()
        self.email_address = ui.lineEdit_email_address.text()
        self.menu_text = ui.lineEdit_menu_text.text()
        self.min_version_no = ui.lineEdit_min_version_no.text()
        self.title = ui.lineEdit_title.text()
        self.version_no = ui.lineEdit_version_no.text()
        self.website = ui.lineEdit_website.text()

        self.template_map = {'TemplateClass' : self.class_name,
                    'templateclass' : self.class_name.lower(),
                    'TemplateTitle' : self.title,
                    'TemplateDescription' : self.description,
                    'TemplateVersion' : self.version_no,
                    'TemplateQgisVersion' : self.min_version_no,
                    'TemplateAuthor' : self.author,
                    'TemplateEmail' : self.email_address,
                    'TemplateMenuText' : self.menu_text,
                    'PluginDirName' : self.class_name.lower()
                    }
