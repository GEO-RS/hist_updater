# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HistogramHandler
                                 A QGIS plugin
 hanldes and updates db with histogram and path / drivenames
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-01-30
        copyright            : (C) 2019 by ASDFE
        email                : askho@sdfe.dk
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HistogramHandler class from file HistogramHandler.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .histogram_handler import HistogramHandler
    return HistogramHandler(iface)
