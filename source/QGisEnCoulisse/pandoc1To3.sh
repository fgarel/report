pandoc -s doc1.md -t rst -o doc2.rst
pandoc --atx-headers -s doc2.rst -t markdown -o doc3.md
#pandoc -s doc3.md -t rst -o doc4.rst
#pandoc --atx-headers -s doc4.rst -t markdown -o doc5.md

diff doc1.md doc3.md
diff doc2.rst doc4.rst

pandoc -s QGisEnCoulisse.md -t rst -o QGisEnCoulisse2.rst
pandoc --atx-headers -s QGisEnCoulisse2.rst -t markdown -o QGisEnCoulisse3.md
#pandoc -s QGisEnCoulisse3.md -t rst -o QGisEnCoulisse4.rst
#pandoc --atx-headers -s QGisEnCoulisse4.rst -t markdown -o QGisEnCoulisse5.md

diff QGisEnCoulisse.md QGisEnCoulisse3.md
diff QGisEnCoulisse2.rst QGisEnCoulisse4.rst
