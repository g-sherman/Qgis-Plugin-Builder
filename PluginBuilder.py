"""
/***************************************************************************
PluginBuilder
A QGIS plugin
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
# Import Python stuff
import os
from string import Template
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from PluginBuilderDialog import PluginBuilderDialog
from ResultDialog import ResultDialog
from pluginspec import PluginSpec

class PluginBuilder:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.plugin_builder_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/pluginbuilder"

    def initGui(self):  
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/pluginbuilder/icon.png"), \
            "Plugin Builder...", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run) 

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Plugin Builder...", self.action)


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Plugin Builder...",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self): 
        # create and show the dialog 
        self.dlg = PluginBuilderDialog() 
        #QMessageBox.warning(self.dlg, "Plugin Dir", self.plugin_builder_dir)
        # connect the ok button to our method
        QObject.connect(self.dlg.ui.buttonBox, SIGNAL("accepted()"), self.validate_entries)

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_() 
        # See if OK was pressed
        if result == 1:
            spec = PluginSpec(self.dlg.ui)
            # get the location for the plugin
            self.plugin_dir = QFileDialog.getExistingDirectory(self.dlg, "Select Plugin Location", ".")
            # create the plugin directory using the class name
            self.plugin_dir = os.path.join(str(self.plugin_dir), str(self.dlg.ui.lineEdit_class_name.text()))
            QDir().mkdir(self.plugin_dir)
            # process the user entries
            self.populate_template(spec, 'Makefile.tmpl', 'Makefile')
            self.populate_template(spec, '__init__.tmpl', '__init__.py')
            self.populate_template(spec, 'TemplateClass.tmpl', "%s.py" % spec.class_name.lower())
            self.populate_template(spec, 'TemplateClassDialog.tmpl', "%sdialog.py" % spec.class_name.lower())
            self.populate_template(spec, 'Ui_TemplateClass.tmpl', "ui_%s.ui" % spec.class_name.lower())
            self.populate_template(spec, 'resources.tmpl', "resources.qrc")
            # copy the non-generated files to the new plugin dir
            template_dir = os.path.join(str(self.plugin_builder_dir), 'templateclass')
            icon = QFile(os.path.join(template_dir, 'icon.png'))
            icon.copy(os.path.join(self.plugin_dir, 'icon.png'))
            #resource = QFile(os.path.join(template_dir, 'resources.qrc'))
            #resource.copy(os.path.join(self.plugin_dir, 'resources.qrc'))

            # show the results
            res_dlg = ResultDialog()
            res_dlg.show()
            self.res_dlg.exec_()



        
    def validate_entries(self):
        # check to see that all fields have been entered
        ui = self.dlg.ui
        if ui.lineEdit_class_name.text() == '' or \
          ui.lineEdit_title.text() == '' or \
          ui.lineEdit_description == '' or \
          ui.lineEdit_version_no == '' or \
          ui.lineEdit_min_version_no == '' or \
          ui.lineEdit_menu_text == '' or \
          ui.lineEdit_company_name == '' or \
          ui.lineEdit_email_address == '':
              QMessageBox.warning(self.dlg, "Missing Information", \
                      'All fields are required to create a plugin')
        else:
            self.dlg.accept()


    def populate_template(self, spec, template_name, output_name):
        template_file = open(os.path.join(str(self.plugin_builder_dir), 'templateclass', template_name))
        s = template_file.read()
        template_file.close()
        template = Template(s)
        popped = template.substitute(spec.template_map)
        plugin_file = open(os.path.join(self.plugin_dir, output_name), 'w')
        plugin_file.write(popped)
        plugin_file.close()

