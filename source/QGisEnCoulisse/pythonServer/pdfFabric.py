#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Script permettant de générer, de fabriquer des plans au format PDF.

Les fichiers nécessaires au fonctionnement de ce script sont :
    - des fichiers template Qgis
    - une connexion aux bases de données telles qu'elles sont décrites
      dans le fichier qgis.

"""

import getopt
#import csv
#import model
#import sqlalchemy.orm
import subprocess
#import re
import sys
#from qgis.core import (
#    QgsProject, QgsComposition, QgsApplication, QgsProviderRegistry)
from qgis.core import (
    QgsProject, QgsComposition, QgsApplication)
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

    def __init__(self, path):
        u"""
        Méthode pour initialiser l'objet.

        Lorque l'objet est instancié, c'est cette méthode qui est executée.

        """
        # Repertoire de travail
        self.path = path
        # Initialisation des variables
        self.qgis_project_file = self.path + '/' + 'dt-dict.qgs'
        self.list_situation = {}
        self.list_case = {}
        self.list_all = {}
        self.list_format = ['A4', 'A3', 'A2', 'A1', 'A0']
        self.list_echelle = ['00200', '00500', '01000']
        self.list_format_echelle = []
        self.setFilename()
        #print self.list_situation
        self.gui_flag = True
        self.myQgisApplication = QgsApplication(sys.argv, self.gui_flag)
        self.myQgisApplication.initQgis()
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

    def make_pdf(self, template_filename, report_filename):
        u"""
        Méthode pour fabriquer un pdf.

        En argument, un fichier template de compostion,
                    et le debut du nom du fichier pdf en sortie.
        En sortie, un seul fichier pdf.

        """
        #print "template_filename = " + template_filename
        #print "report_filename = " + report_filename

        template_file = file(template_filename)
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
        # chargement de l'objet 'map' défini dans le template de composition
        # You must set the id in the template
        map_item = composition.getComposerItemById('map')
        map_item.setMapCanvas(self.canvas)
        map_item.zoomToExtent(self.canvas.extent())

        # You must set the id in the template
        #legend_item = composition.getComposerItemById('legend')
        #legend_item.updateLegend()
        composition.refreshItems()
        composition.exportAsPDF(report_filename + '.pdf')
        QgsProject.instance().clear()

    def make_atlas_pdf(self,
                       template_filename,
                       report_filename,
                       do_or_simulate):
        u"""
        Méthode pour fabriquer plusieurs pdf.

        En argument, un fichier template de compostion,
                    et le debut du nom du fichier pdf en sortie.
        En sortie, plusieurs fichiers pdf, correspondant aux
        différents folios.

        """
        #print "template_filename = " + template_filename
        #print "report_filename = " + report_filename

        template_file = file(template_filename)
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
        if do_or_simulate is False:
            return num_features
        else:
            composition_atlas.setSingleFile(True)
            composition_atlas.firstFeature()
            composition_atlas.beginRender()
            report_filename_generic = report_filename + '_' + '*' + ".pdf"
            #print "report_filename_generic = " + report_filename_generic
            report_filename_final = report_filename + ".pdf"
            subprocess.call("rm " + report_filename_generic, shell=True)
            for i in range(0, num_features):
                composition_atlas.prepareForFeature(i, True)
                # le nom du pdf change à chaque folio
                report_filename_feature = report_filename + '_' + \
                    '{0:0>3}'.format(i) + '.pdf'
                #print "report_filename_feature = " + report_filename_feature
                composition.exportAsPDF(report_filename_feature)

            subprocess.call(["pdftk " + report_filename_generic +
                             " cat output " + report_filename_final],
                            shell=True)
            #print "report_filename_generic = " + report_filename_generic
            subprocess.call("rm " + report_filename_generic, shell=True)
            QgsProject.instance().clear()
            return 0

    def setFilename(self):
        u"""
        Methode pour attribuer un nom aux fichiers en sortie.

        Pour un format donné (A0, A1, ..., A4) et pour une echelle donnée
        (200, 500, 1000),
        il y a 3 fichiers qui peuvent être générés :
            situation : c'est un plan donnant une vue d'ensemble
            case : ce sont les différentes cases, folios, qui,
                   une fois assemblées,
                   couvrent l'emprise demandée dans la dt-dict
            all : c'est une compostion de deux plans précédents.

        """
        for fformat in self.list_format:
            for eechelle in self.list_echelle:
                self.list_format_echelle.append(fformat + '_' + eechelle)

        for fe in self.list_format_echelle:
            self.list_situation.update({'template_file_' + fe:
                                        fe + '_situation.qpt',
                                        'report_file_' + fe:
                                        fe + '_situation'})
            self.list_case.update({'template_file_' + fe:
                                   fe + '_case.qpt',
                                   'report_file_' + fe:
                                   fe + '_case'})
            self.list_all.update({'template_file_' + fe:
                                  fe + '.qpt',
                                  'report_file_' + fe:
                                  fe + ''})


def main(argv):
    u"""
    Programme principal.

    """
    fformat = ''
    eechelle = ''
    ttype = ''
    simulate = True

    try:
        opts, args = getopt.getopt(argv, "hf:e:t:s",
                                   ["format=", "echelle=", "type="])
    except getopt.GetoptError as err:
        print "pdfFabric.py -h"
        print 'pdfFabric.py -f <format> -e <echelle> -t <type> -s'
        print 'pdfFabric.py -f <format> -e <echelle> -t <type>'
        print str(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "pdfFabric.py -h"
            print 'pdfFabric.py -f <format> -e <echelle> -t <type> -s'
            print 'pdfFabric.py -f <format> -e <echelle> -t <type>'
            sys.exit()
        if opt == '-s':
            simulate = False
        elif opt in ("-f", "--format"):
            fformat = arg
        elif opt in ("-e", "--echelle"):
            eechelle = arg
        elif opt in ("-t", "--type"):
            ttype = arg
    #print 'format = ', fformat
    #print 'echelle = ', eechelle
    #print 'type = ', ttype
    #print 'simulate = ', simulate

    __myPdfFabric = PdfFabric('.')
    __myPdfFabric.prepare_before_make()

    # les noms des fichiers sont fabriques à partir des arguments
    if ttype == 'all':
        report_file = fformat + '_' + '{0:0>5}'.format(eechelle)
        template_file = report_file + '.qpt'
        report_file += '_' + ttype
    else:
        report_file = fformat + '_' + '{0:0>5}'.format(eechelle) + '_' + ttype
        template_file = report_file + '.qpt'

    if simulate is True:
        retour = __myPdfFabric.make_atlas_pdf(template_file,
                                              report_file,
                                              True)
    else:
        retour = __myPdfFabric.make_atlas_pdf(template_file,
                                              report_file,
                                              False)

    sys.exit(retour)

if __name__ == '__main__':
    main(sys.argv[1:])
