"""
/***************************************************************************
ResultDialog
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

from PyQt4 import QtCore, QtGui 
from Ui_PluginBuilder import Ui_PluginBuilder
# create the dialog for showing results
class ResultDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_Results.py()
    self.ui.setupUi(self) 

