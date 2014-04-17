# coding=utf-8
"""
/***************************************************************************
    PluginBuilder
                                 A QGIS plugin
    Creates a skeleton QGIS plugin for use as a starting point
                             -------------------
        begin                : 2011-01-20
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
# Import Python stuff
import os
import errno
import shutil
from string import Template
from string import capwords
import datetime
import codecs
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import QFileInfo, QUrl, QFile, QDir
from PyQt4.QtGui import (
    QAction, QIcon, QFileDialog, QMessageBox, QDesktopServices)
from qgis.core import QgsApplication
# Initialize Qt resources from file resources.py
# Do not remove this import even though your IDE / pylint may report it unused
# noinspection PyUnresolvedReferences
import resources
# Import the code for the dialog
from plugin_builder_dialog import PluginBuilderDialog
from result_dialog import ResultDialog
from plugin_specification import PluginSpecification


class PluginBuilder:
    """A QGIS plugin that allows you to build QGIS plugins."""

    def __init__(self, iface):
        """Constructor

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface

        """
        # Save reference to the QGIS interface
        self.iface = iface
        # noinspection PyArgumentList
        self.user_plugin_dir = QFileInfo(
            QgsApplication.qgisUserDbFilePath()).path() + 'python/plugins'
        self.plugin_builder_dir = os.path.dirname(__file__)

        # class members
        self.action = None
        self.dlg = None
        self.plugin_dir = None

    # noinspection PyPep8Naming
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(':/plugins/plugin_builder/plugin_builder.png'),
            'Plugin Builder...', self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu('&Plugin Builder...', self.action)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu('&Plugin Builder...', self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        """Run method that performs all the real work"""
        # create and show the dialog
        self.dlg = PluginBuilderDialog()

        # connect the ok button to our method
        self.dlg.button_box.accepted.connect(self.validate_entries)
        self.dlg.button_box.helpRequested.connect(self.show_help)

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            specification = PluginSpecification(self.dlg)
            # Add the date stuff to the template map
            now = datetime.date.today()
            specification.template_map['TemplateYear'] = now.year
            specification.template_map['TemplateBuildDate'] = '%i-%02i-%02i' % (
                now.year, now.month, now.day)

            # get the location for the plugin
            # noinspection PyCallByClass,PyTypeChecker
            self.plugin_dir = QFileDialog.getExistingDirectory(
                self.dlg, 'Select the Directory for your Plugin', '.')
            if self.plugin_dir == '':
                return
            else:
                while not QFileInfo(self.plugin_dir).isWritable():
                    # noinspection PyTypeChecker,PyArgumentList
                    QMessageBox.critical(
                        None, 'Error', 'Directory is not writeable')
                    # noinspection PyCallByClass,PyTypeChecker
                    self.plugin_dir = QFileDialog.getExistingDirectory(
                        self.dlg, 'Select the Directory for your Plugin', '.')
                    if self.plugin_dir == '':
                        return

            # remove spaces from the plugin name
            # create the plugin directory using the class name
            self.plugin_dir = os.path.join(
                str(self.plugin_dir),
                str(self.dlg.class_name.text()))
            QDir().mkdir(self.plugin_dir)
            # process the user entries
            self.populate_template(
                specification, 'Makefile.tmpl', 'Makefile')
            self.populate_template(
                specification, '__init__.tmpl', '__init__.py')
            self.populate_template(
                specification, 'template_class.tmpl',
                '%s.py' % specification.class_name.lower())
            self.populate_template(
                specification, 'template_class_dialog.tmpl',
                '%sdialog.py' % specification.class_name.lower())
            self.populate_template(
                specification, 'template_class_dialog_base.ui.tmpl',
                'ui_%s.ui' % specification.class_name.lower())
            self.populate_template(
                specification, 'resources.tmpl', 'resources.qrc')
            # copy the non-generated files to the new plugin dir
            template_dir = os.path.join(
                str(self.plugin_builder_dir), 'templateclass')
            icon = QFile(os.path.join(template_dir, 'icon.png'))
            icon.copy(os.path.join(self.plugin_dir, 'icon.png'))
            release_script = QFile(os.path.join(template_dir, 'release.sh'))
            release_script.copy(os.path.join(self.plugin_dir, 'release.sh'))
            plugin_upload = QFile(
                os.path.join(template_dir, 'plugin_upload.py'))
            plugin_upload.copy(
                os.path.join(self.plugin_dir, 'plugin_upload.py'))
            # noinspection PyCallByClass,PyTypeChecker
            QFile.setPermissions(os.path.join(
                self.plugin_dir, 'plugin_upload.py'),
                QFile.ReadOwner | QFile.WriteOwner | QFile.ExeOwner |
                QFile.ReadUser | QFile.WriteUser | QFile.ExeUser |
                QFile.ReadGroup | QFile.ExeGroup | QFile.ReadOther |
                QFile.ExeOther)
            # create a i18n directory
            QDir().mkdir(self.plugin_dir + '/i18n')
            # Create sphinx default project for help
            QDir().mkdir(self.plugin_dir + '/help')
            QDir().mkdir(self.plugin_dir + '/help/build')
            QDir().mkdir(self.plugin_dir + '/help/source')
            QDir().mkdir(self.plugin_dir + '/help/source/_static')
            QDir().mkdir(self.plugin_dir + '/help/source/_templates')
            # copy doc makefiles
            # noinspection PyCallByClass,PyTypeChecker
            QFile.copy(
                os.path.join(template_dir, 'help/make.bat'),
                os.path.join(self.plugin_dir, 'help/make.bat'))
            # noinspection PyCallByClass,PyTypeChecker
            QFile.copy(
                os.path.join(template_dir, 'help/Makefile'),
                os.path.join(self.plugin_dir, 'help/Makefile'))
            # populate and write help files
            self.populate_template(
                specification,
                'help/source/conf.py.tmpl', 'help/source/conf.py')
            self.populate_template(
                specification,
                'help/source/index.rst.tmpl', 'help/source/index.rst')

            # copy the unit tests folder
            test_source = os.path.join(
                os.path.dirname(__file__), 'templateclass', 'test')
            copy(test_source, self.plugin_dir)

            #resource = QFile(os.path.join(template_dir, 'resources.qrc'))
            #resource.copy(os.path.join(self.plugin_dir, 'resources.qrc'))

            # populate the results html template
            template_file = open(os.path.join(
                str(self.plugin_builder_dir), 'templateclass', 'results.tmpl'))
            content = template_file.read()
            template_file.close()
            template = Template(content)
            result_map = {
                'PluginDir': self.plugin_dir,
                'TemplateClass': specification.template_map['TemplateClass'],
                'templateclass': specification.template_map['templateclass'],
                'UserPluginDir': self.user_plugin_dir}
            results_popped = template.substitute(result_map)

            # write the results info to the README HTML file
            readme = codecs.open(os.path.join(
                str(self.plugin_dir), 'README.html'), 'w', 'utf-8')
            readme.write(results_popped)
            readme.close()

            # populate the results readme text template
            template_file = open(os.path.join(
                str(self.plugin_builder_dir), 'templateclass', 'readme.tmpl'))
            content = template_file.read()
            template_file.close()
            template = Template(content)
            result_map = {
                'PluginDir': self.plugin_dir,
                'TemplateClass': specification.template_map['TemplateClass'],
                'templateclass': specification.template_map['templateclass'],
                'UserPluginDir': self.user_plugin_dir}
            popped = template.substitute(result_map)

            # write the results info to the README txt file
            readme_txt = codecs.open(
                os.path.join(str(self.plugin_dir), 'README.txt'), 'w', 'utf-8')
            readme_txt.write(popped)
            readme_txt.close()

            # create the metadata file
            metadata_file = codecs.open(os.path.join(
                str(self.plugin_dir), 'metadata.txt'), 'w', 'utf-8')
            metadata_comment = (
                '# This file contains metadata for your plugin. Since \n'
                '# version 2.0 of QGIS this is the proper way to supply \n'
                '# information about a plugin. The old method of \n'
                '# embedding metadata in __init__.py will \n'
                '# is no longer supported since version 2.0.\n\n'
                '# This file should be included when you package your plugin.'
                '# Mandatory items:\n\n')

            metadata_file.write(metadata_comment)
            metadata_file.write('[general]\n')
            metadata_file.write('name=%s\n' % specification.title)
            metadata_file.write(
                'qgisMinimumVersion=%s\n' % specification.qgis_minimum_version)
            metadata_file.write(
                'description=%s\n' % specification.description)
            metadata_file.write(
                'version=%s\n' % specification.plugin_version)
            metadata_file.write(
                'author=%s\n' % specification.author)
            metadata_file.write(
                'email=%s\n\n' % specification.email_address)
            metadata_file.write(
                '# End of mandatory metadata\n\n')
            metadata_file.write(
                '# Optional items:\n\n')
            metadata_file.write(
                '# Uncomment the following line and add your changelog:\n')
            metadata_file.write(
                '# changelog=\n\n')
            metadata_file.write(
                '# Tags are comma separated with spaces allowed\n')
            metadata_file.write(
                'tags=%s\n\n' % specification.tags)
            metadata_file.write(
                'homepage=%s\n' % specification.homepage)
            metadata_file.write(
                'tracker=%s\n' % specification.tracker)
            metadata_file.write(
                'repository=%s\n' % specification.repository)
            metadata_file.write(
                'icon=%s\n' % specification.icon)
            metadata_file.write(
                '# experimental flag\n')
            metadata_file.write(
                'experimental=%s\n\n' % specification.experimental)
            metadata_file.write(
                '# deprecated flag (applies to the whole plugin, not \n'
                'just a single version)\n')
            metadata_file.write('deprecated=%s\n\n' % specification.deprecated)
            metadata_file.close()
            # show the results
            res_dlg = ResultDialog()
            res_dlg.web_view.setHtml(results_popped)
            res_dlg.show()
            res_dlg.exec_()

    def validate_entries(self):
        """Check to see that all fields have been entered."""
        msg = ''
        dlg = self.dlg
        if dlg.class_name.text() == '' or \
            dlg.title.text() == '' or \
            dlg.description.text() == '' or \
            dlg.module_name.text() == '' or \
            dlg.plugin_version.text() == '' or \
            dlg.qgis_minimum_version.text() == '' or \
            dlg.menu_text.text() == '' or \
            dlg.author.text() == '' or \
            dlg.email_address.text() == '':
                msg = (
                    'Some required fields are missing. '
                    'Please complete the form.\n')
        try:
            # Assigning to _ is python sugar for a variable that will be unused
            _ = float(str(dlg.plugin_version.text()))
            _ = float(str(dlg.qgis_minimum_version.text()))
        except ValueError:
            msg += 'Version numbers must be numeric.\n'
        # validate plugin name
        # check that we have only ascii char in class name
        try:
            unicode(dlg.class_name.text()).decode('ascii')
        except UnicodeEncodeError:
            dlg.class_name.setText(
                unicode(
                    dlg.class_name.text()).encode('ascii', 'ignore'))
            msg += (
                'The Class name must be ASCII characters only, '
                'the name has been modified for you. \n')
        # check space and force CamelCase
        if str(dlg.class_name.text()).find(' ') > -1:
            class_name = capwords(str(dlg.class_name.text()))
            dlg.class_name.setText(class_name.replace(' ', ''))
            msg += (
                'The Class name must use CamelCase. '
                'No spaces are allowed; the name has been modified for you.')
        if msg != '':
            QMessageBox.warning(
                self.dlg, 'Information missing or invalid', msg)
        else:
            self.dlg.accept()

    def populate_template(self, spec, template_name, output_name):
        """Populate the template based on user data.

        :param spec: Descriptive data that will be used to create the plugin.
        :type spec: PluginSpecification

        :param template_name: Name for the template.
        :type template_name: str

        :param output_name:  Name of the output file to create.
        :type output_name: str
        """
        template_file = open(os.path.join(
            str(self.plugin_builder_dir), 'templateclass', template_name))
        content = template_file.read()
        template_file.close()
        template = Template(content)
        popped = template.substitute(spec.template_map)
        plugin_file = codecs.open(
            os.path.join(self.plugin_dir, output_name), 'w', 'utf-8')
        plugin_file.write(popped)
        plugin_file.close()

    def show_help(self):
        """Display application help to the user."""
        help_file = 'file:///%s/help/index.html' % self.plugin_builder_dir
        # For testing path:
        #QMessageBox.information(None, 'Help File', help_file)
        # noinspection PyCallByClass,PyTypeChecker
        QDesktopServices.openUrl(QUrl(help_file))


def copy(source, destination):
    """Copy files recursively.

    Taken from: http://www.pythoncentral.io/
                how-to-recursively-copy-a-directory-folder-in-python/

    :param source: Source directory.
    :type source: str

    :param destination: Destinatio directory.
    :type destination: str

    """
    try:
        shutil.copytree(source, destination)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(source, destination)
        else:
            print('Directory not copied. Error: %s' % e)
