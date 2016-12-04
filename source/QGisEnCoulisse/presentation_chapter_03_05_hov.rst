==============================================
Organisation envisagée pour la gestion du PCRS
==============================================

----

Après avoir présenté les acteurs, c'est à dire les personnes
concernées par ce projet,
nous proposerons un modèle de branches.

----

Les acteurs
===========

Les acteurs sont les personnes qui vont échanger les informations
et dont ces échanges devront être quantifiées (comptabilisées)

- Combien de "plans" ont été apportées par l'acteur A ?
- Combien de "cases" ont été exploitées par l'acteur B ?

Les "commits" dans un dépot geogig sont liés à un acteur.

- Qui a modifié tel objet (et quand) ?
- Qui a controlé ce plan ?

----

Geogig et Git sont des systèmes de gestion de versions distribués.
Dans les systèmes distribués, il n'est pas nécessaire d'avoir un dépot central.

Chaque intervenant dispose d'une copie complète du dépot
avec tout l'historique et
peut effectuer autant de changements locaux qu'il le souhaite,
sans devoir en référer au "serveur".

En pratique, on conserve des dépots centraux pour faciliter les
échanges et servir de référence commune.

Nous allons donc désigner un acteur qui sera chargé d'initier le dépot central.

----

Les acteurs départementaux du PCRS
----------------------------------

Aujourd'hui, dans le département, voici la liste des acteurs,
partenaires du "GT reseaux",
pouvant jouer un rôle dans la consitution,
la mise à jour et l'utilisation du PCRS :

- CDA La Rochelle
- Département
- DGFiP
- ERDF
- SDE
- SDEER
- Soluris
- Ville de La Rochelle

----

Les dépots
==========

Chaque acteur sera propriétaire (gestionnaire) d'un dépot local "PCRS".

C'est depuis ce dépot, qu'il mettra à disposition
ses données en les envoyant (*push*) vers le dépot distant, central, visible
par tous les partenaires du groupement.

----

Un acteur est maître de ce qu'il dépose
sur son dépot local et de ce qu'il envoit sur le dépot central distant,
car le partage des changements
est une opération totalement découplée de leur enregistrement.

Un acteur n'est pas contraint de partager l'ensemble de son patrimoine numérique :
il ne doit mettre dans son depot "PCRS" que les données (cases)
qu'il souhaite mettre à disposition des autres partenaires.

----

Si l'acteur décide d'utiliser geogig en interne pour controler
son Référentiel Très Grande Echelle (RTGE),
il pourra créer un deuxième dépot local qui ne sera pas partagé
avec les autres partenaires.

Un acteur peut donc posséder plusieurs dépots locaux.

Une procédure particulière doit permettre a cet acteur de passer
un extrait de plan topo (une case)
de son dépot local "RTGE" vers son autre dépot local "PCRS".

Si l'acteur n'utilise pas geogig en interne, il partagera ses données
via une operation d'import dans son depot "PCRS"

----

Un acteur peut aussi décider de mettre à dispostion ses données en ouvrant
un dépot à des collaborateurs ou des contributeurs.

La seule contrainte est de rendre ce dépot accessible sur un serveur.

Des services tels github.com (https://github.com/) et gitourious.com
proposent d'héberger des dépots git en ligne.

En existe-t'il pour des dépôts geogig ?

----

Les branches
============

Un dépot pourrait avoir ces différentes branches :

- PlanTopoControle
                        Plan Topo dont la géométrie des objets a été validée
                        par une personne qui veille à un niveau de qualité
                        et qui garantit une certaine précision
- Controle
                        Plan contenant des objets dont la position sert
                        à valider un plan topo
- PlanTopoNonControle
                        Plan de Recolement (après travaux) ou Plan Topo,
                        mais non controlé
- PlanExecution
                        Plan d'Execution (avant Travaux)
- PlanProjet
                        Plan Projet


----
