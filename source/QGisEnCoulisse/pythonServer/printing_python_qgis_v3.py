#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""QGIS Unit tests for QgsLayout

A simple demonstration of to generate a PDF using a QGIS project
and a QGIS layout template.

Inspiration originale, en version 2, mais adaptée à la version 3
http://kartoza.com/how-to-create-a-qgis-pdf-report-with-a-few-lines-of-python/

Inspiration suivante, en version 3, mais adaptée à linux
https://github.com/carey136/Standalone-Export-Atlas-QGIS3
https://github.com/carey136/Standalone-Export-Atlas-QGIS3/blob/master/AtlasExport.py

"""


__author__ = 'Frédéric Garel'
__date__ = '02/04/2017'
__copyright__ = 'Copyright 2019'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import qgis  # NOQA

import os
from os.path import expanduser
#from qgis.testing import start_app
from qgis.core import (QgsApplication,
                       QgsLayout,
                       QgsLayoutAtlas,
                       QgsLayoutExporter,
                       QgsProject,
                       QgsPrintLayout)

# On defintit nos varaibles
# 1. le nom du fichier projet Qgis
myProject = '/home/fred/Documents/report/source/QGisEnCoulisse/data/dtdict2.qgz'
# 2. le nom de la mise en page
layoutName = 'A3_Paysage'
# 3. le nom de l'entité couche de couverture
coverageLayer = 'slt_armoire'
# 4. Filtre de l'atlas
atlasFilter = '"column" = "value"'
atlasFilter = ''
# 5. Format du fichier sortie
outputFormat = "pdf"
# 6. le repertoire de sortie
outputFolder = '/home/fred/Documents/report/source/QGisEnCoulisse/data'
# 7. On coche l'option pour créer un seul fichier pdf en résultat
outputName = "query producing unique value"
# 8. le nom du fichier resultat
pdfName = 'report'



def make_simple_pdf():

    #### Initialising QGIS in back end (utilising users temp folder) ####
    # Il exsite 2 facons de lancer qgis en mode autonome :
    # - 1ère methode de lancement (mode production)
    #   create a reference to the QgsApplication, setting the
    #   second argument for GUI
    #     False = disables the GUI = standalone scripts
    #     True = enable the GUI = custom application
    gui_flag = False
    app = QgsApplication([], gui_flag)
    #   Make sure QGIS_PREFIX_PATH is set in your env if needed!
    app.initQgis()

    # - 2de methode de lancement (mode debugage)
    #   start_app()

    # Une instance de QGis va ouvrir le projet
    projectInstance = QgsProject.instance()
    # project_path = '/home/fred/Documents/report/source/QGisEnCoulisse/data/dtdict2.qgz'
    projectInstance.read(myProject)
    # print(project.fileName())

    # Le gestionnaire de mise en page est utilisé pour ouvrir notre layout
    #layout_name = 'A3_Paysage'
    layoutManager = projectInstance.layoutManager()
    layout = layoutManager.layoutByName(layoutName) #Layout name
    #print(layout.items()[1])

    layoutExporter = QgsLayoutExporter(layout)
    settings = QgsLayoutExporter.PdfExportSettings()
    settings.dpi = 80
    settings.rasterizeWholeImage = False
    settings.forceVectorOutput = False
    #settings.exportMetadata = True
    #print(settings.dpi)
    resultpdf_path = '/home/fred/Documents/report/source/QGisEnCoulisse/data/report.pdf'
    layoutExporter.exportToPdf(resultpdf_path, settings)

    projectInstance.clear()



def make_atlas_pdf():

    #### Initialising QGIS in back end (utilising users temp folder) ####
    #home = expanduser("~")
    #QgsApplication( [], False, home + "/.local/tmp" )
    #QgsApplication.setPrefixPath("/usr/bin/qgis", True) #Change path for standalone QGIS install
    gui_flag = False
    app = QgsApplication([], gui_flag)
    #   Make sure QGIS_PREFIX_PATH is set in your env if needed!
    app.initQgis()


    #### Defining map path and contents ####
    project = QgsProject.instance()
    manager = project.layoutManager()
    project.read(myProject)
    # Le gestionnaire de mise en page est utilisé pour ouvrir notre layout
    myLayout = manager.layoutByName(layoutName) #Layout name
    myAtlas = myLayout.atlas()
    myAtlasMap = myAtlas.layout()

    #### atlas query ####
    if(coverageLayer in locals()):
        myAtlas.setCoverageLayer(QgsProject.instance().mapLayersByName(coverageLayer))
    myAtlas.setFilterFeatures(True)
    myAtlas.setFilterExpression(atlasFilter)

    #### image output name ####
    myAtlas.setFilenameExpression(outputName)

    #### image and pdf settings ####
    pdf_settings=QgsLayoutExporter(myAtlasMap).PdfExportSettings()
    image_settings = QgsLayoutExporter(myAtlasMap).ImageExportSettings()
    image_settings.dpi = 200

    #### Export images or PDF (depending on flag) ####
    if outputFormat == "image":
        imageExtension = '.jpg'
        for myLayout in QgsProject.instance().layoutManager().printLayouts():
            if myAtlas.enabled():
                result, error = QgsLayoutExporter.exportToImage(myAtlas,
                                    baseFilePath=outputFolder + '/', extension=imageExtension, settings=image_settings)
                if not result == QgsLayoutExporter.Success:
                    print(error)
    if outputFormat == "pdf":
        for myLayout in QgsProject.instance().layoutManager().printLayouts():
            if myAtlas.enabled():
                result, error = QgsLayoutExporter.exportToPdf(myAtlas, outputFolder + '/' + pdfName + '.pdf', settings=pdf_settings)
                if not result == QgsLayoutExporter.Success:
                    print(error)
    print("Success!")


make_atlas_pdf()
