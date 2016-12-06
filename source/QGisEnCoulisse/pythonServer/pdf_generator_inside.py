#!/usr/bin/env python
# coding=utf-8

# A simple demonstration of to generate a PDF using a QGIS project
# and a QGIS layout template.
#
# This code is public domain, use if for any purpose you see fit.
# Tim Sutton 2015

import sys
from qgis.core import (
    QgsProject, QgsComposition, QgsApplication, QgsProviderRegistry)
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from PyQt4.QtCore import QFileInfo
from PyQt4.QtXml import QDomDocument


gui_flag = True
#app = QgsApplication(sys.argv, gui_flag)
##app = QgsApplication(sys.argv, gui_flag)


# Make sure QGIS_PREFIX_PATH is set in your env if needed!
##app.initQgis()

# Probably you want to tweak this
#project_path = 'project.qgs'
project_path = '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/test_gml4326.qgs'
#project_path = '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/dt-dict.qgs'

# and this
#template_path = 'template.qpt'
#template_path = '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/templateComposition.qpt'
template_path = '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/folio_A3_200.qpt'


report_path = '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/report.pdf'


canvas = QgsMapCanvas()
# Load our project
QgsProject.instance().read(QFileInfo(project_path))
bridge = QgsLayerTreeMapCanvasBridge(
    QgsProject.instance().layerTreeRoot(), canvas)
bridge.setCanvasLayers()

template_file = file(template_path)
template_content = template_file.read()
template_file.close()
document = QDomDocument()
document.setContent(template_content)
composition = QgsComposition(canvas.mapSettings())

# You can use this to replace any string like this [key]
# in the template with a new value. e.g. to replace
# [date] pass a map like this {'date': '1 Jan 2012'}
#substitution_map = {
#    'DATE_TIME_START': 'foo',
#    'DATE_TIME_END': 'bar'}
#composition.loadFromTemplate(document, substitution_map)
composition.loadFromTemplate(document)
#debug
composition.paperHeight()
composition.paperWidth()
composition.printResolution()


atlasComposition = QgsAtlasComposition(composition)

#debug
atlasComposition.composerMap().displayName()
atlasComposition.hideCoverage()
atlasComposition.enabled()
atlasComposition.coverageLayer().metadata()
atlasComposition.filenamePattern()
atlasComposition.setEnabled(True)
atlasComposition.enabled()
QgsProject.instance().layerTreeRoot().findLayerIds()
QgsProject.instance().layerTreeRoot().findLayerIds()[0]

# You must set the id in the template
map_item = composition.getComposerItemById('map')
map_item.setMapCanvas(canvas)
map_item.zoomToExtent(canvas.extent())
# You must set the id in the template
#legend_item = composition.getComposerItemById('legend')
#legend_item.updateLegend()
composition.refreshItems()
composition.exportAsPDF(report_path)
#QgsProject.instance().clear()


