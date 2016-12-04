========================
Environnement de travail
========================

----

Description de l'environnement de Travail pour ce travail sur les plans topos.

Nous allons utiliser byobu pour le mode console.

Nous allons utiliser sphinx et hovercraft pour la rédaction de la documentation.

----

Utilisation de Byobu pour le mode console
=========================================

1er Terminal : Pour l'administration
------------------------------------
Le premier ecran est destiné au repertoire

.. code::

  ~/Documents/install/source

L'ecran peut-etre divisé en deux :

En haut, acces au sous-repentoire

.. code::

  ~/Documents/install/source/environnementTravail/

pour modifier les fichiers de type

.. code::

  ./installPostgresqlGeogig*.sh

En bas, accès au sous-repertoire

.. code::

  /Documents/install/source/geogig/

pour modifier les fichiers de type

.. code::

  ./installGeogig.sh
  ./dxfToPostgis.sh # utilitaire pour convertir dxf en postgis

----

2d Terminal : Pour l'utilisation
--------------------------------
Le second écran est destiné au repertoire

.. code::

  ~/Documents/technic/source/geogig/

----

3ème Terminal : Pour la rédaction de la documentation
-----------------------------------------------------
Le troisième écran est dédié à la documentation

Cet écran peut lui aussi etre divisé en plusieurs frames :

En haut (Edition), accès au sous-repertoire

.. code::

  ~/Documents/technic/source/geogig
  cd ~/Documents/technic/source/geogig/

pour modifier les fichiers .rst

.. code::

  vi chapter01_hov.rst

----

Nous verrons dans le paragraphe suivant, que nous pouvons même subdiviser cette partie haute
en trois panneaux verticaux.

  - à gauche pour l'edition du fichier du niveau racine, c'est a dire geogig.rst
  - au centre pour l'edition des fichiers de niveau 1, c'est à dire part*.rst
  - à droite pour l'edition des fichiers de niveau 2, c'est à dire chapter*.rst


En bas (Compilation), accès au sous-repertoire

.. code::

  ~/Documents/technic
  cd ~/Documents/technic

pour compiler la documentation.

Avant, il faut se mettre dans l'environemment virtuel ecriture_sphinx

.. code::

  pew workon_ecriture_sphinx
  ./build.sh ; ./visualize.sh

----

Utilisation de Sphinx et hovercraft pour générer la documentation
=================================================================

Conventions de syntaxe
----------------------

Il s'agit de prendre quelques conventions pour que
les fichiers restructured text soient correctement formatés

Le fichier "racine" est geogig.rst.

Il inclut quelques fichiers "fils" :

  - part_introduction.rst
  - part01.rst
  - part02.rst
  - part03.rst
  - part_conclusion.rst

----

Chacun de ces fichiers part, peut lui même inclure des fichiers fils,
c'est à dire des "petits-fils"

On va essayer d'organiser les fichiers de facons à ce que le niveau
d'inclusion des fichiers correspondent au niveau de hierarchie dans le plan du document.

----

=====================  ===================  =======================  =================  ===================
\  Nom du Fichier       Niveau du fichier      Titre principal        Marque du titre   Niveau dans le plan
=====================  ===================  =======================  =================  ===================
geogig.rst                      0           Utilisation de geogig    surligné # # # #   titre du projet
part_introduction.rst           1           Intro : des données et   surligné * * * *   "chapitre 1"
chapter_introduction            2           Introduction             surligné = = = =   1.1. Introduction
chapter_sommaire_avec           2           Sommaire                 surligné = = = =   1.2. Sommaire
part01.rst                      1           Partie 1 : Présentation  surligné + + + +   "chapitre 2"
chapter01.rst                   2           Le PCRS                  surligné = = = =   2.1. Le PCRS
chapter02.rst                   2           Le RTGE                  surligné = = = =   2.2. Le RTGE
=====================  ===================  =======================  =================  ===================

----

=====================  ===================  =======================  =================  ===================
\  Nom du Fichier       Niveau du fichier      Titre principal        Marque du titre   Niveau dans le plan
=====================  ===================  =======================  =================  ===================
geogig.rst                      0           Utilisation de geogig    surligné # # # #   titre du projet
part02.rst                      1           Partie 2 : Des outils..  surligné + + + +   "chapitre 3"
chapter03.rst                   2           Généralités sur geogig   surligné = = = =   3.1. Geogig
chapter04.rst                   2           Quelques notions de ge   surligné = = = =   3.2. Notions
\                               \           Les acteurs              \= \= \= \=        3.2.1. Acteurs
\                               \           Les niveaux d'acteurs    - - - -            Les niveaux d'a
part03.rst                      1           Partie 3 : Cas Concret   surligné + + + +   "chapitre 4"
chapter05.rst                   2           Organisation envisagée   surligné = = = =   4.1. Organisation
\                               \           Définition des acteurs   \= \= \= \=        4.1.1. Acteurs
\                               \           Les acteurs départeme..  - - - -            Les acteurs dép
\                               \           Un dépot public et ...   . . . .            Un dépôt public
=====================  ===================  =======================  =================  ===================

----

Organisation pour l'edition
---------------------------
Le troisième écran sous byobu est donc séparé en deux :

  - en haut pour l'édition des fichiers rst
  - en bas pour la compilation (le build)

Il est possible d'aller plus loin dans le détail.
La partie haute est divisé en trois panneaux verticaux :

  - à gauche pour l'edition du fichier du niveau racine, c'est a dire geogig.rst
  - au centre pour l'edition des fichiers de niveau 1, c'est à dire part*.rst
  - à droite pour l'edition des fichiers de niveau 2, c'est à dire chapter*.rst

----

Outils pour faciliter la génération de cette documentation
==========================================================

Afin d'améliorer la génération de la documentation, nous avons réalisé
quelques scripts qui automatisent le build.

Ces outils sont dans le repertoire ~/Documents/technic

----

build.sh
--------
Ce script regroupe tout simplement plusieurs appels à make

A la fin de l'execution, nous avons du html, du pdf, des slides, etc

visualize.sh
------------
Script qui permet tout simplement de lancer les outils pour consulter la
nouvelle documentation.

rstToHovRst.sh
--------------
L'utilitaire hovercraft utilise le "langage" rst, mais avec peut-être un dialecte un peu différent.

Le but est de transformer le fichier /chapter_annexe05.rst en fichier _hov.rst

----

Installation d'utilitaires divers
=================================
  * petl

    - https://pypi.python.org/pypi/petl
    - https://petl.readthedocs.org/en/latest/index.html
    - https://github.com/alimanfoo/petlx
    - http://petlx.readthedocs.org/en/latest/index.html

  * setl

    - https://stetl.readthedocs.org/en/latest/
    - https://github.com/justb4/stetl
    - http://fr.slideshare.net/justb4/stetl-foss4g20131024v1

----

  * manipulation de fichier svg et graphviz

    - https://www.npmjs.com/package/rsvg
    - http://www.hokstad.com/making-graphviz-output-pretty-with-xsl-updated
    - http://www.hokstad.com/making-graphviz-output-pretty-with-xsl
    - https://github.com/vidarh/diagram-tools
    - http://www.hokstad.com/graphviz

  * plantuml

    - http://fr.plantuml.com/usecase.html#Skinparam
    - http://plantuml.com/sequence.html

  * aafig

    - https://pythonhosted.org/sphinxcontrib-aafig/
    - https://github.com/thewtex/sphinx-contrib/tree/master/aafig

----
