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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Create a skeleton plugin" 
def description():
  return "Creates a skeleton QGIS plugin for use as a starting point"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load PluginBuilder class from file PluginBuilder
  from PluginBuilder import PluginBuilder 
  return PluginBuilder(iface)


