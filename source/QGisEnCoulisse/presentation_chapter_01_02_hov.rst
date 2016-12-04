===============================================
Présentaton de deux référentiels : RTGE et PCRS
===============================================

Le fait d'adopter une structuration et une définition communes
est essentiel si les différents acteurs veulent échanger des plans
topographiques à grande échelle.

----

Le Référentiel à Très Grande Echelle (RTGE)
===========================================

Le **Référentiel à très Grande Echelle (RTGE)** peut être défini comme
étant le plan topographique idéal rêvé par tout utilisateur de SIG :
des données de références précises, exhaustives, correctement structurées,
mises à jour, etc, etc...

Or comme cela a été présenté dans le paragraphe précédent, chaque acteur a
sa propre vision de son Référentiel.

----

Le Plan Corps de Rue Simplifié (PCRS)
=====================================

Le **Plan Corps de Rue Simplifié (PCRS)** est une version allégée du plan topographique.

Il constitue le socle commun minimal décrivant à très grande échelle
les limites apparentes du terrain.

Le PCRS n'est pas à considérer comme étant un plan topographique complet.
Cependant, en faisant une concession sur l'exhaustivité de l'information,
la réflexion sur le PCRS est peut-être une opportunitée de se concentrer sur
les autres qualités attendues :

  -  la garantie d'une certaine classe de précision géométrique,
  -  la structuration de l'information,
  -  la mise à jour

----

Le PCRS se divise en 9 thématiques qui regroupent différents objets :

  - la topographie : les points de canevas, les points topo
  - le bati : les facades des batiments
  - la voirie : les bordures de voie
  - le ferroviaire : les rails
  - les clotures : les murs de clotures
  - le végétal : les arbres et les haies
  - les ouvrages d'art : les piles de pont
  - l'hydrographie
  - l'orographie

----

Les spécifications du PCRS sont connues
---------------------------------------

La documentation est ici :

PCRS accompagnement
http://cnig.gouv.fr/?page_id=1444

PCRS ressources
http://cnig.gouv.fr/?page_id=11745

----

Du RTGE vers le PCRS
====================

Une liste de correspondance
----------------------------

Chaque acteur doit etablir une liste pour
mettre en relation les objets de son Référentiel (son RTGE)
avec les objets correspondant du PCRS.

Cette liste permet à l'acteur de controler l'extraction et l'export
de ses données topographique vers un lot de données
qui doit être considéré comme conforme aux spécifications du PCRS.

----

Cette liste de correspondance est créée en plusieurs étapes :

  - un premier outil lit le fichier .dxf et stocke
    les données dans des tables postgis
  - un second outil lit ces tables brutes et génére des listes de correspondance
    (ce deuxième outil est CreateTableCorrespondanceRTGE_PCRS.sql)
  - une fois que ces listes de correspondance sont complétées, elles peuvent
    alors être utilisées par un troisième outil qui lit les tables brutes
    pour extraire les infos du RTGE et fabriquer le PCRS

----
