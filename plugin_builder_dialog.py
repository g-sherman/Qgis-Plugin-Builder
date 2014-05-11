# coding=utf-8
"""
/***************************************************************************
    PluginBuilderDialog

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

import os
from PyQt4 import QtGui, uic

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
