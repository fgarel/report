#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Script permettant de lire des pdf.

Les pdf qui sont lus sont des formulaires
de DT/DICT (déclarations)
Ces formulaires contiennent :
 - un numéro unique
 - la date de la demande
 - l'adresse mail du demandeur
 - l'emprise du chantier

Ces informations doivent etre récupérées
pour ensuite les utiliser comme paramètres
pour la génération de plans pdf.

"""

import getopt
import sys
import subprocess
#import re
#from decimal import Decimal


class Pdf2Txt(object):

    u"""
    Classe d'objet dont l'objectif principal est la lecture de pdf.

    .

    """

    def __init__(self, pdf_filename, metadata_filename):
        u"""
        Méthode pour initialiser l'objet.

        Lorque l'objet est instancié, c'est cette méthode qui est executée.

        """
        self.pdf_filename = pdf_filename
        self.metadata_filename = metadata_filename
        self.typePdf = ''
        self.filenameGeometry = 'empriseDeclaration4326.gml'
        self.filenameValidGml = 'empriseDeclarationQgis4326.gml'
        self.filenameValidShp = 'empriseDeclarationQgis3946.shp'
        self.numeroDict = ''
        self.capaciteImpression = ''
        self.mailResponsable = ''

        self.bbox_emprise = []

        self.listeTable = ['00042x00030',
                           '00070x00050',
                           '00098x00070',
                           '00112x00080',
                           '00140x00100',
                           '00168x00120',
                           '00182x00130',
                           '00210x00150',
                           '00224x00160',
                           '00245x00175',
                           '00336x00240',
                           '00350x00250',
                           '00490x00350',
                           '00525x00375',
                           '00700x00500',
                           '01050x00750']

    def simplify(self):
        u"""
        Simplifie le pdf et essaye de déterminer son type.

        Il existe plusieurs "type" de pdf et chaque type de
        pdf a sa méthode associée pour le lire :
         - certains sont lisibles selon la procédure A
         - d'autres sont lisibles selon la procédure B
        etc....

        """
        # 1ère partie : deflatter le fichier pdf
        # le fichier initial, document.pdf, contient des chaines
        # de caractères encodeés
        # le fichier final,document1.pdf, contient
        # des caractères decopdés (dezipés ?)
        # vu ici : http://stackoverflow.com/questions/11731425/
        # data-extraction-from-filter-flatedecode-pdf-stream-in-php
        # http://qpdf.sourceforge.net/

        subprocess.call(
            "rm document1.pdf",
            shell=True)

        subprocess.call(
            ['qpdf', '--qdf', '--object-streams=disable',
             self.pdf_filename, 'document1.pdf'],
            shell=False)

        # 2ème étape : test pour connaitre le type de pdf

        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "EPSG"],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        # p2.communicate renvoit un tuple : on ne prend que le 1er element
        chaineType1 = p2.communicate()[0]
        #print "chaineType1 = " + chaineType1
        if chaineType1:
            self.typePdf = 'DICT.fr'

        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'\(.*\t46.*\)'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        # p2.communicate renvoit un tuple : on ne prend que le 1er element
        chaineType2 = p2.communicate()[0]
        #print "chaineType2 = " + chaineType2
        if chaineType2:
            self.typePdf = 'PROTYS.fr'

        return self.typePdf

    def ddict(self):
        u"""
        Recuperation des données d'un pdf type dict.fr.

        .

        """
        # 3ème étape : extraction de l'information geographique
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "EPSG"],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/[^\()]*\(//',
                               '-e', r's/\)[^\()]*\(//g',
                               '-e', r's/\)[^\()]*//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        chaineType1 = p3.communicate()[0]
        ffile = open(self.filenameGeometry, "w")
        ffile.write(chaineType1)
        ffile.close()
        #print "chaineType1 = " + chaineType1

        # 3ème étape suite : extraction du numero de la dict
        # cat document1.pdf | \
        #     grep -E -e '(\([0-9]\)[^\(]*){13}' | \
        #     sed -E -e 's/^[^\(]*//g' \
        #            -e 's/[^\)]*$//g' \
        #            -e 's/\)[^\)\(]*//g' \
        #            -e 's/\(//g'
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'(\([0-9]\)[^\(]*){13}'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/^[^\(]*//g',
                               '-e', r's/[^\)]*$//g',
                               '-e', r's/\)[^\)\(]*//g',
                               '-e', r's/\(//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()
        #p4 = subprocess.Popen(['sed', '-E',
        #                       '-e', r's/^[^\(]*//g'],
        #                      stdin=p3.stdout,
        #                      stdout=subprocess.PIPE)
        #p3.stdout.close()
        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        # et en plus, on supprime le dernier caractère
        chaine = p3.communicate()[0]
        chaine = chaine[:-1]
        # on ne prend que la dernière ligne
        splitchaine = chaine.split('\n')
        #print "chaine = " + chaine
        #print "derniere ligne = " + splitchaine[-1]
        self.numeroDict = splitchaine[-1]
        #print "Numéro de la DT/DICT = " + self.numeroDict

        # 3ème étape suite : capacite d'impression
        # cat document1.pdf | \
        #     grep -E -e 'BMC.*\(A[0-9]\)' | \        
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'BMC.*\(A[0-9]\)'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/.*\(//g',
                               '-e', r's/\).*//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        # et en plus, on supprime le dernier caractère
        self.capaciteImpression = p3.communicate()[0][:-1]
        #print "Capacité d'impression = " + self.capaciteImpression

        # 3ème étape suite : mail du responsable
        # cat document1.pdf | \
        #     grep -E -e 'BMC.*\(.*\@.*\..*\)' | \    
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'BMC.*\(.*\@.*\..*\)'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/.*\(//g',
                               '-e', r's/\).*//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        # et en plus, on supprime le dernier caractère
        self.mailResponsable = p3.communicate()[0][:-1]
        #print "Courriel du responsable du projet = " + self.mailResponsable

        ffile = open(self.metadata_filename, "a")
        ffile.write(self.numeroDict + ';' +
                    self.capaciteImpression + ";" +
                    self.mailResponsable + "\n")
        ffile.close()

    def pprotys(self):
        u"""
        Recuperation des données d'un pdf type protys.fr.

        .

        """
        # 3ème étape : extraction de l'information geographique
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'\(.*\t46.*\)'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/[^\()]*\(/EPSG: 4326; Points[[/',
                               '-e', r's/\)[^\()]*\(/]; [/g',
                               '-e', r's/\)[^\()]*/]; ]/g',
                               '-e', r's/ \\t/,/g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        chaineType1 = p3.communicate()[0]
        ffile = open(self.filenameGeometry, "w")
        ffile.write(chaineType1)
        ffile.close()
        #print "chaineType1 = " + chaineType1

        # 3ème étape suite : extraction du numero de la dict
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'\([0-9]{12}.*\)$'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/.*\(//g',
                               '-e', r's/\).*//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        # et en plus, on supprime le dernier caractère
        self.numeroDict = p3.communicate()[0][:-1]
        #print "Numéro de la DT/DICT = " + self.numeroDict

        #ffile = open(self.filenameGeometry, "w")
        #ffile.write(chaineType1)
        #ffile.close()

        # 3ème étape suite : capacite d'impression
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'\(A[0-9]\)$'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/.*\(//g',
                               '-e', r's/\).*//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        # et en plus, on supprime le dernier caractère
        self.capaciteImpression = p3.communicate()[0][:-1]
        #print "Capacité d'impression = " + self.capaciteImpression

        #ffile = open(self.filenameGeometry, "w")
        #ffile.write(chaineType1)
        #ffile.close()

        # 3ème étape suite : mail du responsable
        
        p1 = subprocess.Popen(['cat', 'document1.pdf'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-E",
                               "-e", r'\(.*\@.*\)$'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', '-E',
                               '-e', r's/.*\(//g',
                               '-e', r's/\).*//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        # p3.communicate renvoit un tuple : on ne prend que le 1er element
        # et en plus, on supprime le dernier caractère
        self.mailResponsable = p3.communicate()[0][:-1]
        #print "Courriel du responsable du projet = " + self.mailResponsable

        #ffile = open(self.filenameGeometry, "w")
        #ffile.write(chaineType1)
        #ffile.close()
        ffile = open(self.metadata_filename, "a")
        ffile.write(self.numeroDict + ';' +
                    self.capaciteImpression + ";" +
                    self.mailResponsable + "\n")
        ffile.close()

    def convert2validGml(self):
        u"""
        conversion de la geometrie vers un fichier gml valide.

        .

        """
        # 4ème étape : convertir ce fichier txt en
        # un vrai fichier lisible par ogr
        subprocess.call(
            ["rm", self.filenameValidGml],
            shell=False)
        ffileWrite = open(self.filenameValidGml, "w")
        ffileRead = open("header4326.gml", "r")
        for line in ffileRead.readlines():
            ffileWrite.write(line)
        ffileRead.close()
        p1 = subprocess.Popen(['cat', self.filenameGeometry],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['sed', '-E',
                               '-e', r's/EPSG: 4326; Points//g',
                               '-e', r's/\[//g',
                               '-e', r's/\]//g'],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['sed', r'$!N;s/\n//g'],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()
        p4 = subprocess.Popen(['sed', '-E',
                               '-e', r's/; /\n/g'],
                              stdin=p3.stdout,
                              stdout=subprocess.PIPE)
        p3.stdout.close()
        p5 = subprocess.Popen(['sed',
                               '-e', r'/^$/d'],
                              stdin=p4.stdout,
                              stdout=subprocess.PIPE)
        p4.stdout.close()
        chaine = p5.communicate()[0]

        ffileWrite.write(chaine)

        #print "chaine = " + chaine

        ffileRead = open('footer4326.gml', "r")
        for line in ffileRead.readlines():
            ffileWrite.write(line)
        ffileRead.close()
        ffileWrite.close()

    def convert2validShp(self):
        u"""
        conversion de la geometrie vers un fichier shp valide.

        .

        """
        # 5ème étape : convertir ce fichier txt en
        # un vrai fichier lisible par ogr
        subprocess.call(
            ["rm", self.filenameValidShp],
            shell=False)
        subprocess.call(
            ["ogr2ogr",
             '-a_srs', 'EPSG:3946',
             '-t_srs', 'EPSG:3946',
             '-s_srs', 'EPSG:4326',
             self.filenameValidShp, self.filenameValidGml],
            shell=False)


def main(argv):
    u"""
    Programme principal.

    """

    ffile = ''
    metadata_file = ''
    try:
        opts, args = getopt.getopt(argv, "hf:m:",
                                   ["file=", "metadata="])
    except getopt.GetoptError as err:
        print "pdf2txt.py -h"
        print 'pdf2txt.py -f <file> -m <metadata>'
        print str(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "pdf2txt.py -h"
            print 'pdf2txt.py -f <file> -m <metadata>'
            sys.exit()
        if opt in ("-f", "--file"):
            ffile = arg
        elif opt in ("-m", "--metadata"):
            metadata_file = arg

    #print 'file = ', ffile
    # instanciation de la classe d'objet
    __myPdf2Txt = Pdf2Txt(ffile, metadata_file)

    # 1. on simplifie le pdf et on essaye de déterminer
    # son type
    __typePdf = __myPdf2Txt.simplify()
    #print "Détection du type de pdf : origine de la DT/DICT  = ", __typePdf

    # selon le pdf, on procède à l'extraction de la geometrie
    if __myPdf2Txt.typePdf == "PROTYS.fr":
        __myPdf2Txt.pprotys()
    if __myPdf2Txt.typePdf == "DICT.fr":
        __myPdf2Txt.ddict()

    #print "Numéro de la DT/DICT = " + __myPdf2Txt.numeroDict
    #print "Capacité d'impression = " + __myPdf2Txt.capaciteImpression
    #print "Courriel du responsable du projet = " + __myPdf2Txt.mailResponsable

    __myPdf2Txt.convert2validGml()
    __myPdf2Txt.convert2validShp()

if __name__ == '__main__':
    main(sys.argv[1:])
