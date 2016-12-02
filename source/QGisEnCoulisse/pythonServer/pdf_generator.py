#!/usr/bin/env python
# coding=utf-8

# A simple demonstration of to generate a PDF using a QGIS project
# and a QGIS layout template.
#
# This code is public domain, use if for any purpose you see fit.
# Tim Sutton 2015

import sys
#from qgis.core import (
#    QgsProject, QgsComposition, QgsApplication, QgsProviderRegistry)
from qgis.core import (
    QgsProject, QgsComposition, QgsApplication)
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from PyQt4.QtCore import QFileInfo
from PyQt4.QtXml import QDomDocument


gui_flag = True
#app = QgsApplication(sys.argv, gui_flag)
app = QgsApplication(sys.argv, gui_flag)


# Make sure QGIS_PREFIX_PATH is set in your env if needed!
app.initQgis()

# Probably you want to tweak this
project_path = 'project.qgs'
project_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/test_gml4326.qgs'
project_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/dt-dict.qgs'


# and this
template_path = 'template.qpt'
template_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/templateComposition.qpt'
template_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/folio_A3_200.qpt'
template_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/A1_00200_situation.qpt'
template_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/A1_00200_case.qpt'

report_path = \
    '/home/fred/Travail/ecriture_sphinx/technic/source/dt-dict/report.pdf'

def make_pdf():
    '''
    fonction pour fabriquer un fichier pdf à partir d'un fichier
    template de compostion
    '''
    # http://qgis.org/api/classQgsMapCanvas.html
    # Map canvas is a class for displaying all GIS data types on a canvas.
    canvas = QgsMapCanvas()
    # Load our project
    # http://qgis.org/api/classQgsProject.html
    # Reads and writes project states.
    QgsProject.instance().read(QFileInfo(project_path))
    # http://qgis.org/api/classQgsLayerTreeMapCanvasBridge.html
    # The QgsLayerTreeMapCanvasBridge class takes care of updates of layer set for QgsMapCanvas from a layer tree.
    bridge = QgsLayerTreeMapCanvasBridge(
        QgsProject.instance().layerTreeRoot(), canvas)
    bridge.setCanvasLayers()

    template_file = file(template_path)
    template_content = template_file.read()
    template_file.close()
    #
    document = QDomDocument()
    document.setContent(template_content)
    # http://qgis.org/api/classQgsComposition.html
    # Graphics scene for map printing.
    composition = QgsComposition(canvas.mapSettings())
    # You can use this to replace any string like this [key]
    # in the template with a new value. e.g. to replace
    # [date] pass a map like this {'date': '1 Jan 2012'}
    substitution_map = {
        'DATE_TIME_START': 'foo',
        'DATE_TIME_END': 'bar'}
    composition.loadFromTemplate(document, substitution_map)
    # You must set the id in the template
    # chargement de l'objet 'map' défini dans le template de composition
    map_item = composition.getComposerItemById('map')
    map_item.setMapCanvas(canvas)
    map_item.zoomToExtent(canvas.extent())
    print "atlasMode = ", composition.atlasMode()
    #composition.setAtlasMode(QgsComposition.AtlasMode.PreviewAtlas)
    #composition.setAtlasMode(QgsComposition.AtlasMode['PreviewAtlas'])
    #print "QgsComposition ", type(QgsComposition.AtlasMode)
    print "atlasMode = ", composition.atlasMode()
    #composition_atlas = composition.atlasComposition()
    # You must set the id in the template
    #legend_item = composition.getComposerItemById('legend')
    #legend_item.updateLegend()
    composition.refreshItems()
    composition.exportAsPDF(report_path)
    QgsProject.instance().clear()

def make_atlas_pdf():
    '''
    fonction pour fabriquer un fichier pdf à partir d'un fichier
    template de compostion
    '''
    # http://qgis.org/api/classQgsMapCanvas.html
    # Map canvas is a class for displaying all GIS data types on a canvas.
    canvas = QgsMapCanvas()
    # Load our project
    # http://qgis.org/api/classQgsProject.html
    # Reads and writes project states.
    QgsProject.instance().read(QFileInfo(project_path))
    # http://qgis.org/api/classQgsLayerTreeMapCanvasBridge.html
    # The QgsLayerTreeMapCanvasBridge class takes care of updates of layer set for QgsMapCanvas from a layer tree.
    bridge = QgsLayerTreeMapCanvasBridge(
        QgsProject.instance().layerTreeRoot(), canvas)
    bridge.setCanvasLayers()

    template_file = file(template_path)
    template_content = template_file.read()
    template_file.close()
    #
    document = QDomDocument()
    document.setContent(template_content)
    # http://qgis.org/api/classQgsComposition.html
    # Graphics scene for map printing.
    composition = QgsComposition(canvas.mapSettings())
    # You can use this to replace any string like this [key]
    # in the template with a new value. e.g. to replace
    # [date] pass a map like this {'date': '1 Jan 2012'}
    substitution_map = {
        'DATE_TIME_START': 'foo',
        'DATE_TIME_END': 'bar'}
    composition.loadFromTemplate(document, substitution_map)
    # You must set the id in the template
    # chargement de l'objet 'map' défini dans le template de composition
    ##map_item = composition.getComposerItemById('map')
    ##map_item.setMapCanvas(canvas)
    ##map_item.zoomToExtent(canvas.extent())
    #print "atlasMode = ", composition.atlasMode()
    #composition.setAtlasMode(QgsComposition.AtlasMode.PreviewAtlas)
    # on passe en mode PreviewAtlas
    composition.setAtlasMode(1)
    composition.setAtlasMode(2)
    #print "QgsComposition ", type(QgsComposition.AtlasMode)
    #print "atlasMode = ", composition.atlasMode()
    composition_atlas = composition.atlasComposition()
    # You must set the id in the template
    #legend_item = composition.getComposerItemById('legend')
    #legend_item.updateLegend()
    #print "coverageLayer() = ", composition_atlas.coverageLayer()
    #print "coverageLayer() = ", composition_atlas.coverageLayer().metadata()
    num_features=composition_atlas.numFeatures()
    print "numFeatures() = ", composition_atlas.numFeatures()
    composition_atlas.setSingleFile(True)
    print "singleFile() = ", composition_atlas.singleFile()
    #print "renderBegun()", composition_atlas.renderBegun(), " ; renderEnded() = ", composition_atlas.renderEnded()
    composition_atlas.firstFeature()
    #print "renderBegun()", composition_atlas.renderBegun(), " ; renderEnded() = ", composition_atlas.renderEnded()
    composition_atlas.beginRender()
    #print "renderBegun()", composition_atlas.renderBegun(), " ; renderEnded() = ", composition_atlas.renderEnded()
    for i in range (0, num_features):
        print "i = ", i
        #print "renderBegun()", composition_atlas.renderBegun(), " ; renderEnded() = ", composition_atlas.renderEnded()
        composition_atlas.prepareForFeature(i, True)
        composition.exportAsPDF(report_path)
    #composition_atlas.beginRender()
    #print "renderBegun()", composition_atlas.renderBegun(), " ; renderEnded() = ", composition_atlas.renderEnded()
    #composition.refreshItems()
    composition.exportAsPDF(report_path)
    QgsProject.instance().clear()

def setFilename(format_echelle):
    '''
    '''
    case_file = format_echelle + '_case'
    print format_echelle
    return [case_file, 0]

if __name__ == '__main__':
    liste = setFilename('A1_00200')
    print liste[0]
    #make_pdf()
    #make_atlas_pdf()
