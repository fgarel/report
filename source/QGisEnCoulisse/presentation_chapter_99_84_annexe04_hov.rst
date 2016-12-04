=================================================
Coté administrateur : Mise en place d'un tutorial
=================================================

----

L'environnement de travail pour l'administrateur, c'est le 1er écran byobu.

C'est à dire, que l'administrateur travaille par defaut dans le repertoire

.. code::

  ~/Documents/install/source/geogig/

----

Création du jeu de données exemple
==================================

Dans une première partie, nous allons faire des manipulations afin de
créer un jeu de données exemples.

Dans une seconde partie, nous allons manipuler ces données à
l'aide de l'outil geogig.

----

Une base de données origine
---------------------------

Nous allons faire des manipulations afin de créer un jeu de données exemples.

Une première base de données, que l'on va appeler "origine",
va nous servir pour faire nos traitements qui ne sont pas liés à geogig.

Dans cette base de données, nous allons créer des tables qui vont
accueillir des données brutes :

 - le jeu exemple qui est fabriqué au départ sous libre office "calc" (!!)
   est transformé en sql, puis est injecté dans cette base origine
 - le pcrs exemple, récupéré sur le site du cnig, est lui aussi
   injecté dans cette base.

----

Le premier fichier sample.ods permet de montrer
l'évolution des emprises geographiques de 4 utilisateurs.

Le deuxième fichier, sample2.ods, permet de fabriquer le fichier sql
qui correspond aux 25 cases de l'emprise totale

A partir de ce deuxième fichier sample2.ods, nous allons fabriquer
3 fichiers sql :

  - create_sample.sql
  - insert_sample.sql
  - update_sample.sql

----

En executant ces trois fichiers, on obtient notre base exemple.

.. code::

  psql -h localhost -d gis -U fred -f create_sample.sql
  psql -h localhost -d gis -U fred -f insert_sample.sql
  psql -h localhost -d gis -U fred -f update_sample.sql

----

Injecter des données dans cette base
------------------------------------

Le transfert des données du jeu exemple, de libre office "calc"
vers la base origine est détaillé dans le fichier :

.. code::

  ~/Documents/install/source/geogig/installGeogigSample.sh

La conversion des fichiers pcrs, récupérés sur le site du cnig, au format gml,
vers la base postgreSQL est réalisé via le script :

.. code::

  ~/Documents/install/source/geogig/gmlToPostgis.sh

----

Manipuler les données, les extraire
-----------------------------------

Un certain nombres de scripts sql vont ensuite être joué afin de sélectionner,
en sortie, des données qui seront utilisées dans
la deuxième partie de notre procédure de test.

La manipulation des données et l'extraction se fait grace au script :

.. code::

  TODO

----

Utilisation de geogig
---------------------

La création des des dépots initiaux se fait grace au script :

.. code::

  ~/Documents/install/source/geogig/installGeogig2.sh

----
