# -*- coding: utf-8 -*-
"""
/***************************************************************************
 marbot
                                 A QGIS plugin
 Maritime boundary tools
                             -------------------
        begin                : 2017-06-28
        copyright            : (C) 2017 by Ivan Busthomi
        email                : ivanbusthomi@gmail.com
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
    """Load marbot class from file marbot.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .marbot import marbot
    return marbot(iface)
