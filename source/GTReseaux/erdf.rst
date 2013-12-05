************************
Analyse des données erdf
************************

Intégration
===========

Les fichiers sont des binaires, format dgn v8.

Le système de projection est le Lambert 2.

Lecture des données, après transformation en dxf

.. code::

  ogrinfo ~/f/CARTOGRAPHIE/donnees/vecteur/comparaison_VLR_ERDF/ERDF/999-02-00047-00026-13-B-17-FP2.dxf entities

Import des données sous postgis

.. code::

  ./convertDaoSig.sh --host=10.2.10.56 --dbname=dbmapnik --user=contrib --dxftopsql ~/f/CARTOGRAPHIE/donnees/vecteur/comparaison_VLR_ERDF/ERDF/999-02-00047-00026-13-B-17-FP2.dxf



Comparaison avec les données de La Rochelle
===========================================
