==================================================
Les données initiales et l'installation des outils
==================================================

----

Les données sont sous forme de fichiers ou stockées dans des bases de données.
Qgis va nous servir à visualiser ces données.

Qgis
====

Actuellement, il y a plusieurs exemples :

=========================================  ===============  ====================================================
Emplacement du fichier qgis                Base de données  Commentaires
=========================================  ===============  ====================================================
/technic/source/geogig/pcrs/PCRS-GML.qgs                    fichiers gml de Strasbourg
/technic/source/qgis/pcrs.qgs              origine          fichiers dxf de la rochelle
/technic/source/geogig/sample.qgs          rtge_VLR         les données sont fabriquées à partir du fihcier calc
/technic/source/geogig/pcrs.qgs            sandbox          Structuration Stricte
=========================================  ===============  ====================================================

----

Les données fichiers
====================

En ce qui concerne les fichiers, nous avons un lot de données pcrs
sous la forme de plusieurs fichiers gml

Le pcrs au format gml est ici :

.. code::

  ~/Documents/technic/source/geogig/....

----

Les donnéees topographiques completes, c'est à dire les données RTGE au
format Dxf sont ici :

.. code::

  ~/Documents/technic/source/geogig/....

----

Postgresql / Postgis
====================

Le serveur est VLR6180Y

Pour chacun des acteurs, nous allons attribuer deux bases de données.

La base origine contient les données tests qui ne sont pas partagées.

C'est un peu la base privée de chacun des utilisateurs.

La base sandbox est utilisée lors de la manipulation de geogig.

----

L'installation de Postgresql et le paramétrage des bases de données
sont réalisés via les scripts :

.. code::

  ~/Documents/install/source/environnementTravail/installPostgresql.sh

  ~/Documents/install/source/environnementTravail/installPostgresqlGeogigGTReseaux.sh

----

Geogig
======

En ce qui concerne l'outil geogig, il faut distinguer deux choses :

 - l'installation du logiciel
 - la création des commits initiaux


Installation de geogig
----------------------

L'installation est automatisée et détaillée
via l'execution du script

.. code::

  ~/Documents/install/source/geogig/installGeogig.sh

----
