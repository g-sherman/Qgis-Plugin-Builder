"""
/***************************************************************************
    PluginBuilder

    Creates a QGIS plugin template for use as a starting point in plugin
    development.
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
    return "Plugin Builder"


def description():
    return "Creates a QGIS plugin template for developing a new plugin"


def version():
    return "Version 2.0"


def icon():
    return 'plugin_builder.png'


def qgisMinimumVersion():
    return "2.0"

def author():
    return "gsherman"

def email():
    return "gsherman@geoapt.com"

def classFactory(iface):
    # load PluginBuilder class from file PluginBuilder
    from pluginbuilder import PluginBuilder
    return PluginBuilder(iface)
