#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Du pdf initial vers des plans pdf finaux.

Script permettant d'enchainer la lecture du pdf initial
et la génération des plans pdf finaux.

"""

import getopt
import sys
import subprocess


class PdfReader(object):

    u"""
    Classe d'objet dont l'objectif principal est la génération de pdf.

    Le script a besoin d'arguments (utilisation de getopt).
    Le détail est dans la fonction main().

    """

    def __init__(self, pdf_filename):
        u"""
        Méthode pour initialiser l'objet.

        Lorque l'objet est instancié, c'est cette méthode qui est executée.

        """
        self.pdf_filename = pdf_filename
        self.metadata_filename = 'metadatadict.txt'
        self.numeroDict = ''
        self.capaciteImpression = ''
        self.mailResponsable = ''


def main(argv):
    u"""
    Programme principal.

    """

    ffile = ''
    try:
        opts, args = getopt.getopt(argv, "hf:",
                                   ["file="])
    except getopt.GetoptError as err:
        print "do_all.py -h"
        print 'do_all.py -f <file>'
        print str(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "do_all.py -h"
            print 'do_all.py -f <file>'
            sys.exit()
        if opt in ("-f", "--file"):
            ffile = arg

    #print 'file = ', ffile

    # instance de l'objet
    __myPdfReader = PdfReader(ffile)

    # recuperation de l'emprise geographique d'un declaration,
    # en lisant le fichier pdf (document.pdf)

    ##./pdf2txt.sh
    subprocess.call(
        ["./pdf2txt.py", '-f', ffile, '-m', __myPdfReader.metadata_filename],
        shell=False)

    # lecture du fichier metadata
    ffileRead = open(__myPdfReader.metadata_filename, "r")
    for line in ffileRead.readlines():
        metadata_dict = line.split(";")
    ffileRead.close()
    __myPdfReader.numeroDict = metadata_dict[0]
    __myPdfReader.capaciteImpression = metadata_dict[1]
    __myPdfReader.mailResponsable = metadata_dict[2]
    print "numeroDict = " + __myPdfReader.numeroDict

    # generation des cases
    # ./case_generator.py
    command = "./caseFabric.py -f empriseDeclarationQgis3946.shp "
    command += "-t Floating 2> /dev/null"
    subprocess.call(
        command,
        shell=True)

    # generation des plans
    ##rm report.pdf
    ##ipython pdf_generator.py
    ##display report.pdf
    if __myPdfReader.capaciteImpression == 'A4':
        command = "./pdfFabricAll.py -f A4 -F " + __myPdfReader.capaciteImpression
        command += "  -n 10"
    elif __myPdfReader.capaciteImpression == 'A3':
        command = "./pdfFabricAll.py -f A4 -F " + __myPdfReader.capaciteImpression
        command += "  -n 2"
    elif __myPdfReader.capaciteImpression == 'A2':
        command = "./pdfFabricAll.py -f A3 -F " + __myPdfReader.capaciteImpression
        command += "  -n 2"
    elif __myPdfReader.capaciteImpression == 'A1':
        command = "./pdfFabricAll.py -f A3 -F " + __myPdfReader.capaciteImpression
        command += "  -n 2"
    elif __myPdfReader.capaciteImpression == 'A0':
        command = "./pdfFabricAll.py -f A3 -F " + __myPdfReader.capaciteImpression
        command += "  -n 2"        

    #p3 = subprocess.call(
    #    "./pdfFabricAll.py -f A4 -F A3 -n 20",
    #    shell=True)
    print "command = " + command
    subprocess.call(
        command,
        shell=True)

    # on renomme les plans
    command = "rename 's/(.*)/" + __myPdfReader.numeroDict
    command += "_$1/' A*.pdf"
    subprocess.call(
        command,
        shell=True)

if __name__ == '__main__':
    main(sys.argv[1:])
