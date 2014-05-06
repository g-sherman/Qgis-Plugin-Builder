# coding=utf-8
"""
/***************************************************************************
    ResultDialog

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

from PyQt4 import QtCore, QtGui, uic

BASE_CLASS = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'results_dialog_base.ui'))[0]


class ResultDialog(QtGui.QDialog, BASE_CLASS):
    """Dialog for showing the results of the plugin creation process."""
    def __init__(self, parent=None):
        super(ResultDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
