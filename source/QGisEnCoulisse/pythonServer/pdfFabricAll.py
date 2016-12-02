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
import subprocess
#import re
import sys


class PdfFabricAll(object):

    u"""
    Classe d'objet dont l'objectif principal est la génération de pdf.

    Le script a besoin d'arguments (utilisation de getopt).
    Le détail est dans la fonction main().

    """

    def __init__(self, fformat_min, fformat_max, nb_case_max):
        u"""
        Méthode pour initialiser l'objet.

        Lorque l'objet est instancié, c'est cette méthode qui est executée.

        """
        self.list_format = ['A4', 'A3', 'A2', 'A1', 'A0']
        self.list_echelle = ['00200', '00500', '01000']
        self.list_format_echelle = []
        self.nb_folio_A4_00200_case = 0
        self.nb_folio_A3_00200_case = 0
        self.nb_folio_A2_00200_case = 0
        self.nb_folio_A1_00200_case = 0
        self.nb_folio_A0_00200_case = 0
        self.nb_folio_A4_00500_case = 0
        self.nb_folio_A3_00500_case = 0
        self.nb_folio_A2_00500_case = 0
        self.nb_folio_A1_00500_case = 0
        self.nb_folio_A0_00500_case = 0
        self.nb_folio_A4_01000_case = 0
        self.nb_folio_A3_01000_case = 0
        self.nb_folio_A2_01000_case = 0
        self.nb_folio_A1_01000_case = 0
        self.nb_folio_A0_01000_case = 0
        self.fformat_min = fformat_min
        self.fformat_max = fformat_max
        self.nb_case_max = int(nb_case_max)
        self.fe_choisi = ''

    def doMap(self):
        u"""
        Méthode pour generer les plans.

        """

        split_fe_choisi = self.fe_choisi.split('_')
        fformat_choisi = split_fe_choisi[0]
        eechelle_choisi = split_fe_choisi[1]
        #print "fformat_choisi  = " + fformat_choisi
        #print "eechelle_choisi = " + eechelle_choisi
        
        print "Generation du plan de situation"
        ligne_commande = "./pdfFabric.py -f " + fformat_choisi + \
            " -e " + eechelle_choisi + " -t situation 2> /dev/null"
        #print 'command = ' + ligne_commande
        subprocess.call(
            ligne_commande,
            shell=True)
            
        print "Generation des différents folios 1/2"
        ligne_commande = "./pdfFabric.py -f " + fformat_choisi + \
            " -e " + eechelle_choisi + " -t case 2> /dev/null"
        subprocess.call(
            ligne_commande,
            shell=True)

        # assemblage plan de situation et case
        #print "pdftk " + self.fe_choisi + "_situation.pdf " + \
        #                 self.fe_choisi + "_case.pdf" + \
        #                 " cat output " + self.fe_choisi + ".pdf"
        subprocess.call(["pdftk " + self.fe_choisi + "_situation.pdf " +
                         self.fe_choisi + "_case.pdf" +
                         " cat output " + self.fe_choisi + ".pdf"],
                        shell=True)
        """                
        print "Generation des différents folios 2/2"
        if fformat_choisi == 'A4':
            ligne_commande = "./pdfFabric.py -f " + fformat_choisi + \
                " -e " + eechelle_choisi + \
                " -t 'all' 2> /dev/null"
            subprocess.call(
                ligne_commande,
                shell=True)
            ligne_commande = "./pdfFabric.py -f " + 'A3' + \
                " -e " + eechelle_choisi + \
                " -t 'all' 2> /dev/null"
            subprocess.call(
                ligne_commande,
                shell=True)
        if fformat_choisi == 'A3':
            print "A3->A2 ?"
            ligne_commande = "./pdfFabric.py -f " + 'A2' + \
                " -e " + eechelle_choisi + \
                " -t 'all' 2> /dev/null"
            subprocess.call(
                ligne_commande,
                shell=True)
        if fformat_choisi == 'A2':
            ligne_commande = "./pdfFabric.py -f " + 'A1' + \
                " -e " + eechelle_choisi + \
                " -t 'all' 2> /dev/null"
            subprocess.call(
                ligne_commande,
                shell=True)
        if fformat_choisi == 'A1':
            ligne_commande = "./pdfFabric.py -f " + 'A0' + \
                " -e " + eechelle_choisi + \
                " -t 'all' 2> /dev/null"
            subprocess.call(
                ligne_commande,
                shell=True)
        """

    def choose(self):
        u"""
        Méthode pour choisir le format et l'echelle.

        """
        #self.fe_choisi = 'A4_00200'
        print "Début du test pour le choix du format et de l'echelle"

        # initialisation = simulation initiale, au 200, pour le format_min
        if self.fformat_min == 'A4':
            self.fe_choisi = 'A4_00200'
            self.nb_folio_A4_00200_case = subprocess.call(
                "./pdfFabric.py -f A4 -e 200 -t case -s 2> /dev/null",
                shell=True)
            print "A4_00200_case : " + str(self.nb_folio_A4_00200_case)

        if self.fformat_min == 'A3':
            self.fe_choisi = 'A3_00200'
            self.nb_folio_A3_00200_case = subprocess.call(
                "./pdfFabric.py -f A3 -e 200 -t case -s 2> /dev/null",
                shell=True)
            #print "A3_00200_case : " + str(self.nb_folio_A3_00200_case)

        if self.fformat_min == 'A2':
            self.fe_choisi = 'A2_00200'
            self.nb_folio_A2_00200_case = subprocess.call(
                "./pdfFabric.py -f A2 -e 200 -t case -s 2> /dev/null",
                shell=True)
            #print "A2_00200_case : " + str(self.nb_folio_A2_00200_case)

        if self.fformat_min == 'A1':
            self.fe_choisi = 'A1_00200'
            self.nb_folio_A1_00200_case = subprocess.call(
                "./pdfFabric.py -f A1 -e 200 -t case -s 2> /dev/null",
                shell=True)
            #print "A1_00200_case : " + str(self.nb_folio_A1_00200_case)

        if self.fformat_min == 'A0':
            self.fe_choisi = 'A0_00200'
            self.nb_folio_A0_00200_case = subprocess.call(
                "./pdfFabric.py -f A0 -e 200 -t case -s 2> /dev/null",
                shell=True)
            #print "A0_00200_case : " + str(self.nb_folio_A0_00200_case)

        #print "initialisation : fe_choisi = " + self.fe_choisi

        # ensuite on agrandit le format si besoin
        # puis, si le format n'est plus suffisant,
        # on modifie l'echelle
        if self.fformat_max == 'A4':
            #print "fformat_max == 'A4'"
            if self.nb_folio_A4_00200_case > self.nb_case_max:
                self.fe_choisi = 'A4_00500'
                self.nb_folio_A4_00500_case = subprocess.call(
                    "./pdfFabric.py -f A4 -e 500 -t case -s 2> /dev/null",
                    shell=True)
                #print "A4_00500_case : " + str(self.nb_folio_A4_00500_case)
                if self.nb_folio_A4_00500_case > self.nb_case_max:
                    self.fe_choisi = 'A4_01000'

        if self.fformat_max == 'A3':
            #print "fformat_max == 'A3'"
            if self.fformat_min == 'A4':
                if self.nb_folio_A4_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A3_00200'
                    self.nb_folio_A3_00200_case = subprocess.call(
                        "./pdfFabric.py -f A3 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A3_00200_case : " + \
                    #        str(self.nb_folio_A3_00200_case)
            if self.nb_folio_A3_00200_case > self.nb_case_max:
                self.fe_choisi = 'A3_00500'
                self.nb_folio_A3_00500_case = subprocess.call(
                    "./pdfFabric.py -f A3 -e 500 -t case -s 2> /dev/null",
                    shell=True)
                #print "A3_00500_case : " + str(self.nb_folio_A3_00500_case)
                if self.nb_folio_A3_00500_case > self.nb_case_max:
                    self.fe_choisi = 'A3_01000'

        if self.fformat_max == 'A2':
            #print "fformat_max == 'A2'"
            if self.fformat_min == 'A4':
                if self.nb_folio_A4_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A3_00200'
                    self.nb_folio_A3_00200_case = subprocess.call(
                        "./pdfFabric.py -f A3 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A3_00200_case : " + \
                    #        str(self.nb_folio_A3_00200_case)
            if self.fformat_min == 'A3' or self.fformat_min == 'A4':
                #print "2 fformat_min = " + self.fformat_min
                #print "2 fformat_max = " + self.fformat_max
                #print "2 nb_case_max = " + self.nb_case_max
                #print "2 nb_folio_A3_00200_case = " + \
                #        str(self.nb_folio_A3_00200_case)
                if self.nb_folio_A3_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A2_00200'
                    self.nb_folio_A2_00200_case = subprocess.call(
                        "./pdfFabric.py -f A2 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A2_00200_case : " + \
                    #        str(self.nb_folio_A2_00200_case)
            if self.nb_folio_A2_00200_case > self.nb_case_max:
                self.fe_choisi = 'A2_00500'
                self.nb_folio_A2_00500_case = subprocess.call(
                    "./pdfFabric.py -f A2 -e 500 -t case -s 2> /dev/null",
                    shell=True)
                #print "A2_00500_case : " + str(self.nb_folio_A2_00500_case)
                if self.nb_folio_A2_00500_case > self.nb_case_max:
                    self.fe_choisi = 'A2_01000'

        if self.fformat_max == 'A1':
            #print "fformat_max == 'A1'"
            if self.fformat_min == 'A4':
                if self.nb_folio_A4_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A3_00200'
                    self.nb_folio_A3_00200_case = subprocess.call(
                        "./pdfFabric.py -f A3 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A3_00200_case : " + \
                    #        str(self.nb_folio_A3_00200_case)
            if self.fformat_min == 'A3' or self.fformat_min == 'A4':
                if self.nb_folio_A3_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A2_00200'
                    self.nb_folio_A2_00200_case = subprocess.call(
                        "./pdfFabric.py -f A2 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A2_00200_case : " + \
                    #        str(self.nb_folio_A2_00200_case)
            if self.fformat_min == 'A2' or \
               self.fformat_min == 'A3' or \
               self.fformat_min == 'A4':
                if self.nb_folio_A2_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A1_00200'
                    self.nb_folio_A1_00200_case = subprocess.call(
                        "./pdfFabric.py -f A1 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A1_00200_case : " + \
                    #        str(self.nb_folio_A1_00200_case)
            if self.nb_folio_A1_00200_case > self.nb_case_max:
                self.fe_choisi = 'A1_00500'
                self.nb_folio_A1_00500_case = subprocess.call(
                    "./pdfFabric.py -f A1 -e 500 -t case -s 2> /dev/null",
                    shell=True)
                #print "A1_00500_case : " + str(self.nb_folio_A1_00500_case)
                if self.nb_folio_A1_00500_case > self.nb_case_max:
                    self.fe_choisi = 'A1_01000'

        if self.fformat_max == 'A0':
            #print "fformat_max == 'A0'"
            if self.fformat_min == 'A4':
                if self.nb_folio_A4_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A3_00200'
                    self.nb_folio_A3_00200_case = subprocess.call(
                        "./pdfFabric.py -f A3 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A3_00200_case : " + \
                    #        str(self.nb_folio_A3_00200_case)
            if self.fformat_min == 'A3' or self.fformat_min == 'A4':
                if self.nb_folio_A3_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A2_00200'
                    self.nb_folio_A2_00200_case = subprocess.call(
                        "./pdfFabric.py -f A2 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A2_00200_case : " + \
                    #        str(self.nb_folio_A2_00200_case)
            if self.fformat_min == 'A2' or \
               self.fformat_min == 'A3' or \
               self.fformat_min == 'A4':
                if self.nb_folio_A2_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A1_00200'
                    self.nb_folio_A1_00200_case = subprocess.call(
                        "./pdfFabric.py -f A1 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A1_00200_case : " + \
                    #        str(self.nb_folio_A1_00200_case)
            if self.fformat_min == 'A1' or \
               self.fformat_min == 'A2' or \
               self.fformat_min == 'A3' or \
               self.fformat_min == 'A4':
                if self.nb_folio_A1_00200_case > self.nb_case_max:
                    self.fe_choisi = 'A0_00200'
                    self.nb_folio_A0_00200_case = subprocess.call(
                        "./pdfFabric.py -f A0 -e 200 -t case -s 2> /dev/null",
                        shell=True)
                    #print "A0_00200_case : " + \
                    #        str(self.nb_folio_A0_00200_case)
            if self.nb_folio_A0_00200_case > self.nb_case_max:
                self.fe_choisi = 'A0_00500'
                self.nb_folio_A0_00500_case = subprocess.call(
                    "./pdfFabric.py -f A0 -e 500 -t case -s 2> /dev/null",
                    shell=True)
                #print "A0_00500_case : " + str(self.nb_folio_A0_00500_case)
                if self.nb_folio_A0_00500_case > self.nb_case_max:
                    self.fe_choisi = 'A0_01000'


def main(argv):
    u"""
    Programme principal.

    """
    fformat_min = ''
    fformat_max = ''
    nb_case_max = ''
    try:
        opts, args = getopt.getopt(
            argv,
            "hf:F:n:",
            ["formatMin=", "FormatMax=", "nombreCaseMax="])
    except getopt.GetoptError as err:
        print "pdfFabricAll.py -h"
        print 'pdfFabricAll.py -f <formatMin> ' + \
            '-F <FormatMax> -n <nombreCaseMax>'
        print str(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "pdfFabricAll.py -h"
            print 'pdfFabricAll.py -f <formatMin> ' + \
                '-F <FormatMax> -n <nombreCaseMax>'
            sys.exit()
        if opt in ("-f", "--formatMin"):
            fformat_min = arg
        elif opt in ("-F", "--FormatMax"):
            fformat_max = arg
        elif opt in ("-n", "--nombreCaseMax"):
            nb_case_max = arg

    #print 'format_min = ', fformat_min
    #print 'format_max = ', fformat_max
    #print 'nb_case_max = ', nb_case_max

    __myPdfFabricAll = PdfFabricAll(fformat_min, fformat_max, nb_case_max)
    #__myPdfFabricAll.simulate('A4', '200')
    __myPdfFabricAll.choose()
    print 'fe_choisi = ' + __myPdfFabricAll.fe_choisi
    __myPdfFabricAll.doMap()

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])
