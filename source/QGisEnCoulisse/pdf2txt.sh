#!/bin/sh

# le but de ce script est :
# à partir d'un fichier pdf (document.pdf), 
#     qui contient une chaine de caractères "EPSG: 4326......." (chaine de caractères correspondant à un polygone d'emprise)
# on extrait cette information du pdf,
# on fabrique un fichier gml, qui pourra etre lu par qgis

# 1ère partie : deflatter le fichier pdf
# le fichier initial, document.pdf, contient des chaines de caractères encodeés
# le fichier final,document1.pdf, contient des caractères decopdés (dezipés ?)
# vu ici : http://stackoverflow.com/questions/11731425/data-extraction-from-filter-flatedecode-pdf-stream-in-php
# http://qpdf.sourceforge.net/
rm document1.pdf
qpdf --qdf --object-streams=disable document.pdf document1.pdf

# 2ème étape : extraire l'information geographique
rm empriseDeclaration4326.gml
cat document1.pdf | grep EPSG | sed -E -e 's/[^\()]*\(//' -e 's/\)[^\()]*\(//g' -e 's/\)[^\()]*//g' > empriseDeclaration4326.gml
cat document1.pdf | grep -E -e '\(.*\t46.*\)'
# 3ème étape : covertir ce fichier txt en un vrai fichier lisible par ogr

# 3.A. conversion d'un gml codé en 4171
#rm empriseDeclarationQgis4171.gml
#rm empriseDeclarationQgis4171.gfs
#cat header4171.gml > empriseDeclarationQgis4171.gml
#cat empriseDeclaration4171.gml | sed -E -e 's/\r$//g' -e 's/<.*>/\n/' | sed -e '/^$/d' | sed '$!N;s/\n/ /g' | sed '$!N;s/\n/ /g' | sed -E -e 's/(\S*) (\S*) /\1,\2\n/g' | sed -E -e 's/(\S*) (\S*)/\1,\2/g' >> empriseDeclarationQgis4171.gml
#cat footer4171.gml >> empriseDeclarationQgis4171.gml
#ogrinfo empriseDeclarationQgis4171.gml empriseDeclaration

# 3.B. conversion d'un gml codé en 4326
rm empriseDeclarationQgis4326.gml
rm empriseDeclarationQgis4326.gfs
cat header4326.gml > empriseDeclarationQgis4326.gml
cat empriseDeclaration4326.gml | sed -E -e 's/EPSG: 4326; Points//g' -e 's/\[//g' -e 's/\]//g' | sed '$!N;s/\n//g' | sed -E -e 's/; /\n/g' | sed -e '/^$/d' >> empriseDeclarationQgis4326.gml
cat footer4326.gml >> empriseDeclarationQgis4326.gml
#ogrinfo empriseDeclarationQgis4326.gml empriseDeclaration

# 4ème étape : convertir au format shape
rm empriseDeclarationQgis3946.shp
rm empriseDeclarationQgis3946.shx
rm empriseDeclarationQgis3946.dbf
rm empriseDeclarationQgis3946.prj
ogr2ogr -a_srs EPSG:3946 -t_srs EPSG:3946 -s_srs EPSG:4326 empriseDeclarationQgis3946.shp empriseDeclarationQgis4326.gml

ogrinfo empriseDeclarationQgis3946.shp empriseDeclarationQgis3946
