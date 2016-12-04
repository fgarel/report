===========================================
Tests avancées : Des conditions réelles (?)
===========================================

----

Afin de valider que geogig puisse-être utilisé pour la gestion du PCRS,
il convient de pousser les tests en s'approchant le plus possible des
conditions réelles d'utilisation.

Les problèmes de format de fichiers et de géométrie d'emprise
sont donc à ajouter dans ces tests avancés.

Ces tests devront aussi être l'opportunité de valider l'utilisation des
trois branches :

  - PlanTopoControle
  - Controle
  - PlanTopoNonControle

Comment utiliser à bon escient les données de la DGFiP (qui pourraient être
ajoutées dans la branche Controle) pour controler
les plans topo et les faire basculer ainsi de la branche PlanTopoNonControle
vers la branche PlanTopoControle ?

----

Enfin, ces tests doivent nous permettre de vérifier que les logs de geogig
pourront être utilisés pour comptabiliser les contributions de chacun.

Combien de cases ont été apportés par tel acteur ?

Combien d'objets ont été controlés par tel autre ?

----

Scénario avancé
===============

  * L'acteur A

                - Format privilégié : DXF
                - Emprise : Case
                - Liste des objets levés : commun, puis à partir d'une certaine date, Arbre + Haie

  * L'acteur B

                - Format : Postgis
                - Emprise : Case
                - Liste des objets levés : commun, puis à partir d'une certaine date, Arbre + AffleurantSymbole

  * L'acteur C

                - Format : ShapeFile
                - Emprise : Polygone irrégulier
                - Liste des objets levés : commun, puis à partir d'une certaine date, Haie + PointCanevas

  * L'acteur D

                - Format : Spatialite
                - Emprise : Polygone irrégulier
                - Liste des objets levés : commun, puis à partir d'une certaine date, PointCanevas + AffleurantSymbole

...

----

Présentation du jeu de données exemple
======================================

La création du jeu de données original se fait grâce aux scripts :

.. code::

  ~/Documents/install/source/geogig/Admin_0*.sh

----

Présentation de la simulation
=============================

La simulation des ajouts des acteurs est réalisée grâce aux scripts :

.. code::

  ~/Documents/install/source/geogig/User_0*.sh

----
