# coding=utf-8
"""
/***************************************************************************
    PluginBuilderDialog

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

import os
from PyQt4 import QtGui, uic
from PyQt4.QtGui import QMessageBox, QFrame
from string import capwords
from plugin_templates import templates

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'plugin_builder_dialog_base.ui'))


class PluginBuilderDialog(QtGui.QDialog, FORM_CLASS):
    """Dialog for defining the new plugin properties.

    Note we use multiple inheritance so you can reference any gui elements
    directly from this class without needing to go through self.ui and
    so that qt autoconnect slots work.

    """
    def __init__(self, parent=None):
        """Constructor."""
        super(PluginBuilderDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.template_subframe = None
        self.templates = templates()
        for templ in self.templates:
            self.template_cbox.addItem(templ.descr())
        self.update_prev_next_buttons()
        self.update_template()
        self.stackedWidget.currentChanged.connect(self.update_prev_next_buttons)
        self.next_button.clicked.connect(self.next)
        self.prev_button.clicked.connect(self.prev)
        self.template_cbox.currentIndexChanged.connect(self.update_template)
        self.next_button.setFocus()

    def update_prev_next_buttons(self):
        i = self.stackedWidget.currentIndex()
        self.prev_button.setEnabled(i > 0)

    def next(self):
        i = self.stackedWidget.currentIndex()
        if i < 5:
            ok = True
            if i == 0:
                ok = self.validate_entries()
            if i == 1:
                ok = self.validate_about()
            if i == 4:
                ok = self.validate_publication()
                
            if ok:
                if i < 4:
                    self.stackedWidget.setCurrentIndex(i + 1)
                else:
                    self.accept()

    def prev(self):
        i = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(i - 1)

    def template(self):
        return self.templates[self.template_cbox.currentIndex()]

    def update_template(self):
        if self.template_subframe is not None:
            self.template_subframe.setParent(None)
        subframe = QFrame(self.template_frame)
        self.frame_layout.addWidget(subframe, 1, 0, 1, 2)
        self.template_subframe = uic.loadUi(os.path.join(
            self.template().subdir(), 'wizard_form_base.ui'),
            subframe)

    def validate_entries(self):
        """Check to see that all fields have been entered."""
        message = ''
        if self.class_name.text() == '' or \
           self.title.text() == '' or \
           self.description.text() == '' or \
           self.module_name.text() == '' or \
           self.plugin_version.text() == '' or \
           self.qgis_minimum_version.text() == '' or \
           self.author.text() == '' or \
           self.email_address.text() == '':
                message = (
                    'Some required fields are missing. '
                    'Please complete the form.\n')
        try:
            # Assigning to _ is python sugar for a variable that will be unused
            _ = float(str(self.plugin_version.text()))
            _ = float(str(self.qgis_minimum_version.text()))
        except ValueError:
            message += 'Version numbers must be numeric.\n'
        # validate plugin name
        # check that we have only ascii char in class name
        try:
            unicode(self.class_name.text()).decode('ascii')
        except UnicodeEncodeError:
            self.class_name.setText(
                unicode(
                    self.class_name.text()).encode('ascii', 'ignore'))
            message += (
                'The Class name must be ASCII characters only, '
                'the name has been modified for you. \n')
        # check space and force CamelCase
        if str(self.class_name.text()).find(' ') > -1:
            class_name = capwords(str(self.class_name.text()))
            self.class_name.setText(class_name.replace(' ', ''))
            message += (
                'The Class name must use CamelCase. '
                'No spaces are allowed; the name has been modified for you.')
        # noinspection PyArgumentList
        if message != '':
            QMessageBox.warning(
                self, 'Information missing or invalid', message)
        else:
            return True

    def validate_about(self):
        if len(self.about.toPlainText()) == 0:
            QMessageBox.warning(
                self,
                "Missing About",
                "Please enter a bit of detail about your plugin "
                "(purpose, function, requirements, etc.).\n\n"
                "You can modify this later by editing the 'about' tag in the "
                "generated metadata.txt file.")
            return False
        else:
            return True

    def validate_publication(self):
        if len(self.tracker.text()) == 0 or len(self.repository.text()) == 0:
            QMessageBox.warning(
                self,
                "Missing Tracker/Repository",
                "A bug tracker and repository entry are now required. "
                "You may enter placeholders here, but will need valid "
                "entries prior to submitting your plugin to the QGIS "
                "plugin repository.")
            return False
        else:
            return True


