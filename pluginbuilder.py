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
from string import capwords
import datetime
import codecs
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from pluginbuilder_dialog import PluginBuilderDialog
from result_dialog import ResultDialog
from pluginspec import PluginSpec

class PluginBuilder:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.user_plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins"
        self.plugin_builder_dir = self.user_plugin_dir + "/pluginbuilder"

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/pluginbuilder/plugin_builder.png"), \
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

        # populate the left panel
        #QMessageBox.warning(self.dlg, "Help Path", "Setting help url to: file:///%s/help.html" % self.plugin_builder_dir)

        self.dlg.ui.webView.setUrl(QUrl("file:///%s/help.html" % self.plugin_builder_dir))

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            spec = PluginSpec(self.dlg.ui)
            # Add the date stuff to the template map
            now = datetime.date.today()
            spec.template_map['TemplateYear'] = now.year
            spec.template_map['TemplateBuildDate'] = "%i-%02i-%02i" % (now.year, now.month, now.day)

            # get the location for the plugin
            self.plugin_dir = QFileDialog.getExistingDirectory(self.dlg, "Select the Directory for your Plugin", ".")
            if self.plugin_dir == '':
                return
            # remove spaces from the plugin name
            
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
            release_script = QFile(os.path.join(template_dir, 'release.sh'))
            release_script.copy(os.path.join(self.plugin_dir, 'release.sh'))
            plugin_upload = QFile(os.path.join(template_dir, 'plugin_upload.py'))
            plugin_upload.copy(os.path.join(self.plugin_dir, 'plugin_upload.py'))
            QFile.setPermissions(os.path.join(
                self.plugin_dir, 'plugin_upload.py'),
                QFile.ReadOwner | QFile.WriteOwner | QFile.ExeOwner | QFile.ReadUser |
                QFile.WriteUser | QFile.ExeUser | QFile.ReadGroup | QFile.ExeGroup |
                QFile.ReadOther | QFile.ExeOther)
            # create a i18n directory
            QDir().mkdir(self.plugin_dir + "/i18n")
            # Create sphinx default project for help
            QDir().mkdir(self.plugin_dir + "/help")
            QDir().mkdir(self.plugin_dir + "/help/build")
            QDir().mkdir(self.plugin_dir + "/help/source")
            QDir().mkdir(self.plugin_dir + "/help/source/_static")
            QDir().mkdir(self.plugin_dir + "/help/source/_templates")
            # copy doc makefiles
            QFile.copy(os.path.join(template_dir, "help/make.bat"),
                    os.path.join(self.plugin_dir, "help/make.bat"))
            QFile.copy(os.path.join(template_dir, "help/Makefile"),
                    os.path.join(self.plugin_dir, "help/Makefile"))
            # populate and write help files
            self.populate_template(spec, 'help/source/conf.py.tmpl', "help/source/conf.py")
            self.populate_template(spec, 'help/source/index.rst.tmpl', "help/source/index.rst")

            #resource = QFile(os.path.join(template_dir, 'resources.qrc'))
            #resource.copy(os.path.join(self.plugin_dir, 'resources.qrc'))

            # populate the results html template
            template_file = open(os.path.join(str(self.plugin_builder_dir), 'templateclass', 'results.tmpl'))
            s = template_file.read()
            template_file.close()
            template = Template(s)
            result_map = {'PluginDir': self.plugin_dir,
                    'TemplateClass': spec.template_map['TemplateClass'],
                    'templateclass': spec.template_map['templateclass'],
                    'UserPluginDir': self.user_plugin_dir}
            results_popped = template.substitute(result_map)

            # write the results info to the README HTML file
            readme = codecs.open(os.path.join(str(self.plugin_dir), 'README.html'), 'w', "utf-8")
            readme.write(results_popped)
            readme.close()

            # populate the results readme text template
            template_file = open(os.path.join(str(self.plugin_builder_dir), 'templateclass', 'readme.tmpl'))
            s = template_file.read()
            template_file.close()
            template = Template(s)
            result_map = {'PluginDir': self.plugin_dir,
                    'TemplateClass': spec.template_map['TemplateClass'],
                    'templateclass': spec.template_map['templateclass'],
                    'UserPluginDir': self.user_plugin_dir}
            popped = template.substitute(result_map)

            # write the results info to the README txt file
            readme = codecs.open(os.path.join(str(self.plugin_dir), 'README.txt'), 'w', "utf-8")
            readme.write(popped)
            readme.close()

            # create the metadata file
            md = codecs.open(os.path.join(str(self.plugin_dir), 'metadata.txt'), 'w', "utf-8")
            metadata_comment = """# This file contains metadata for your plugin. Beginning
# with version 1.8 this is the preferred way to supply information about a
# plugin. The current method of embedding metadata in __init__.py will
# be supported until version 2.0

# This file should be included when you package your plugin.

# Mandatory items:
\n\n"""

            md.write(metadata_comment)
            md.write("[general]\n")
            md.write("name=%s\n" % spec.title)
            md.write("qgisMinimumVersion=%s\n" % spec.min_version_no)
            md.write("description=%s\n" % spec.description)
            md.write("version=%s\n" % spec.version_no)
            md.write("author=%s\n" % spec.author)
            md.write("email=%s\n\n" % spec.email_address)
            md.write("# end of mandatory metadata\n\n")
            md.write("# Optional items:\n\n")
            md.write("# Uncomment the following line and add your changelog entries:\n")
            md.write("# changelog=\n\n")
            md.write("# tags are comma separated with spaces allowed\n")
            md.write("tags=%s\n\n" % spec.tags)

            md.write("homepage=%s\n" % spec.homepage)
            md.write("tracker=%s\n" % spec.tracker)
            md.write("repository=%s\n" % spec.repository)
            md.write("icon=%s\n" % spec.icon)

            md.write("# experimental flag\n")
            md.write("experimental=%s\n\n" % spec.experimental)

            md.write("# deprecated flag (applies to the whole plugin, not just a single version\n")
            md.write("deprecated=%s\n\n" % spec.deprecated)

            md.close()


            # show the results
            res_dlg = ResultDialog()
            res_dlg.ui.webView.setHtml(results_popped)
            res_dlg.show()
            res_dlg.exec_()




    def validate_entries(self):
        # check to see that all fields have been entered
        msg = ''
        ui = self.dlg.ui
        if ui.lineEdit_class_name.text() == '' or \
            ui.lineEdit_title.text() == '' or \
            ui.lineEdit_description.text() == '' or \
            ui.lineEdit_version_no.text() == '' or \
            ui.lineEdit_min_version_no.text() == '' or \
            ui.lineEdit_menu_text.text() == '' or \
            ui.lineEdit_company_name.text() == '' or \
            ui.lineEdit_email_address.text() == '':
                msg = 'Some required fields are missing. Please complete the form.\n'
        try:
            flt = float(str(ui.lineEdit_version_no.text()))
            flt = float(str(ui.lineEdit_min_version_no.text()))
        except ValueError:
            msg += 'Version numbers must be numeric.\n'
        # validate plugin name
        # check that we have only ascii char in class name
        try:
            unicode(ui.lineEdit_class_name.text()).decode('ascii')
        except UnicodeEncodeError:
            ui.lineEdit_class_name.setText(
                unicode(
                    ui.lineEdit_class_name.text()).encode('ascii', 'ignore'))
            msg += 'The Class name must be ASCII characters only, '
            msg += 'the name has been modified for you. \n'
        # check space and force CamelCase
        if str(ui.lineEdit_class_name.text()).find(' ') > -1:
            class_name = capwords(str(ui.lineEdit_class_name.text()))
            ui.lineEdit_class_name.setText(class_name.replace(' ', ''))
            msg += 'The Class name must use CamelCase. '
            msg += 'No spaces are allowed; the name has been modified for you.'
        if msg != '':
            QMessageBox.warning(self.dlg,
                                "Information missing or invalid",
                                msg)
        else:
            self.dlg.accept()

    def populate_template(self, spec, template_name, output_name):
        template_file = open(
            os.path.join(str(self.plugin_builder_dir),
                         'templateclass', template_name))
        s = template_file.read()
        template_file.close()
        template = Template(s)
        popped = template.substitute(spec.template_map)
        plugin_file = codecs.open(
            os.path.join(self.plugin_dir, output_name), 'w', "utf-8")
        plugin_file.write(popped)
        plugin_file.close()
