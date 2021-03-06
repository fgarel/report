#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Script permettant de générer, de fabriquer des plans au format PDF.

Les fichiers nécessaires au fonctionnement de ce script sont :
    - des fichiers template Qgis
    - une connexion aux bases de données telles qu'elles sont décrites
      dans le fichier qgis.

"""

import time
import gdal
import qgis.utils
import getopt
#import csv
#import model
#import sqlalchemy.orm
import subprocess
#import re
import sys
#from qgis.core import (
#    QgsProject, QgsComposition, QgsApplication, QgsProviderRegistry)
#from qgis.core import (
#    QgsProject, QgsComposition, QgsApplication, QgsProviderRegistry)
    
from qgis.core import *
#from qgis.core import (
#    QgsProject, QgsComposition)
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from PyQt4.QtCore import QFileInfo
from PyQt4.QtXml import QDomDocument


class PdfFabric(object):
    
    u"""
    Classe d'objet dont l'objectif principal est la génération de pdf.
    
    Le script a besoin d'arguments (utilisation de getopt).
    Le détail est dans la fonction main().
    
    """
    
    def __init__(self, path, qgis_file, template_file):
        u"""
        Méthode pour initialiser l'objet.
        
        Lorque l'objet est instancié, c'est cette méthode qui est executée.
        
        """
        # Repertoire de travail
        self.path = path
        # Initialisation des variables
        self.qgis_project_file = self.path + '/' + qgis_file
        self.template_file = self.path + '/' + template_file
        #self.list_situation = {}
        #print self.list_situation
        self.gui_flag = True
        
        self.myQgisApplication = QgsApplication(sys.argv, self.gui_flag)
        QgsApplication.setPrefixPath("c:/osgeo4w/apps/qgis-ltr", True)
        self.myQgisApplication.initQgis()
        if len(QgsProviderRegistry.instance().providerList()) == 0:
            raise RuntimeError('No data providers available.')
        self.canvas = None
        self.bridge = None
        
    def prepare_before_make(self):
        u"""
        Méthode pour la préparation avant la fabrication de pdf.
        
        """
        # http://qgis.org/api/classQgsMapCanvas.html
        # Map canvas is a class for displaying all GIS data types on a canvas.
        self.canvas = QgsMapCanvas()
        #print "template_filename = " + template_filename
        # chargement du projet qgis
        # http://qgis.org/api/classQgsProject.html
        # Reads and writes project states.
        QgsProject.instance().read(QFileInfo(self.qgis_project_file))
        #print "report_filename = " + report_filename
        # creation d'un pont entre la hierarchie des niveaux du canvas
        # et la hierarchie des niveaux du projet qgis
        # http://qgis.org/api/classQgsLayerTreeMapCanvasBridge.html
        # The QgsLayerTreeMapCanvasBridge class takes care of updates of
        # layer set for QgsMapCanvas from a layer tree.
        self.bridge = QgsLayerTreeMapCanvasBridge(
            QgsProject.instance().layerTreeRoot(), self.canvas)
        self.bridge.setCanvasLayers()
        
        
        
    def make_atlas_pdf(self,
                       report_filename):
        u"""
        Méthode pour fabriquer plusieurs pdf.
        
        En argument, un fichier template de compostion,
                    et le debut du nom du fichier pdf en sortie.
        En sortie, plusieurs fichiers pdf, correspondant aux
        différents folios.
        Ces différents pdf sont assemblés avec pdftk
        
        """
        #print "template_filename = " + template_filename
        #print "report_filename = " + report_filename
        
        template_file = file(self.template_file)
        template_content = template_file.read()
        template_file.close()
        #
        document = QDomDocument()
        document.setContent(template_content)
        # http://qgis.org/api/classQgsComposition.html
        # Graphics scene for map printing.
        composition = QgsComposition(self.canvas.mapSettings())
        # You can use this to replace any string like this [key]
        # in the template with a new value. e.g. to replace
        # [date] pass a map like this {'date': '1 Jan 2012'}
        substitution_map = {
            'DATE_TIME_START': 'foo',
            'DATE_TIME_END': 'bar'}
        composition.loadFromTemplate(document, substitution_map)
        # on passe en mode PreviewAtlas
        composition.setAtlasMode(1)
        composition.setAtlasMode(2)
        composition_atlas = composition.atlasComposition()
        # You must set the id in the template
        #legend_item = composition.getComposerItemById('legend')
        #legend_item.updateLegend()
        num_features = composition_atlas.numFeatures()
        
        composition_atlas.setSingleFile(True)
        composition_atlas.firstFeature()
        composition_atlas.beginRender()
        report_filename_generic = report_filename + '_' + '*' + ".pdf"
        #print "report_filename_generic = " + report_filename_generic
        report_filename_final = report_filename + ".pdf"
        #subprocess.call("del " + report_filename_generic, shell=True)
        #subprocess.call(["del", report_filename_generic], shell=True)
        for i in range(0, num_features):
            composition_atlas.prepareForFeature(i, True)
            # le nom du pdf change à chaque folio
            report_filename_feature = report_filename + '_' + \
                '{0:0>3}'.format(i) + '.pdf'
            #print "report_filename_feature = " + report_filename_feature
            composition.exportAsPDF(report_filename_feature)
            
        subprocess.call(["pdftk", report_filename_generic, 
                         "cat", "output", report_filename_final],
                        shell=True)
        #print "report_filename_generic = " + report_filename_generic
        subprocess.call(["del", report_filename_generic], shell=True)
        QgsProject.instance().clear()
        return 0
        
def main(argv):
    u"""
    Programme principal.
    
    """
    # valeurs par defaut
    fformat = 'A4'
    oorientation = 'Paysage'
    llayers = 'Orthophotoplan'
    
    try:
        opts, args = getopt.getopt(argv, "hf:o:l:",
                                   ["format=", "orientation=", "layers="])
    except getopt.GetoptError as err:
        print "pdfFabric.py -h"
        print 'pdfFabric.py -f <format> -o <orientation> -l <layers>'
        print str(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "pdfFabric.py -h"
            print 'pdfFabric.py -f <format> -o <orientation> -t <layers>'
            sys.exit()
        if opt in ("-f", "--format"):
            fformat = arg
        elif opt in ("-o", "--orientation"):
            oorientation = arg
        elif opt in ("-l", "--layers"):
            llayers = arg
    
    #print 'format = ', fformat
    #print 'orientation = ', oorientation
    #print 'layers = ', llayers
    
    qgis_file = "QGisEnCoulisse.qgs"
    report_file = "plan"
    # le nom du fichier template est fabriqué à partir des arguments
    template_file = fformat + '_' + oorientation + '_' + llayers + '.qpt'
    #template_file = "A4_Paysage_Orthophotoplan.qpt"
    
    __myPdfFabric = PdfFabric('../../../apps/qgis-ltr/bin', qgis_file, template_file)
    __myPdfFabric.prepare_before_make()
    retour = __myPdfFabric.make_atlas_pdf('..\QGisEnCoulisse\pdf\\' + report_file)

    #QgsApplication.exitQgis()
    sys.exit(retour)
    
if __name__ == '__main__':
    main(sys.argv[1:])

