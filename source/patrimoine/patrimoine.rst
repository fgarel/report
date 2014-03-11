##########################################
Patrimoine Bati de la Ville de La Rochelle
##########################################

****
Plan
****

.. rst-class:: build

 * Les Données

   * Liste du patrimoine
   * Les éléments techniques rattachés
   * Les documents graphiques (plans, photos, ...)

 * Les Logiciels

   * ATAL et son paramètrage
   * Excel
   * Coriolis (Bon de Commande)


 * Les Utilisateurs

   * Liste des utilisateurs et de leurs droits
   * Les formations

.. include:: patrimoine/analyse_existant.rst
.. include:: patrimoine/propositions.rst
.. include:: source/patrimoine/analyse_existant.rst
.. include:: source/patrimoine/propositions.rst
.. include:: ./patrimoine/analyse_existant.rst
.. include:: ./patrimoine/propositions.rst

***********
Les Données
***********

Liste du patrimoine
===================

Analyse de plusieurs sources
----------------------------

La liste des batiments de la ville a été fournie par :

  - le service Maintenance Energie Sécurité
  - le service des Affaires Foncières et Immobilières
  - le service des Affaires Juridiques
  - l'analyse des données du cadastre

Proposition d'une liste unique de référence
-------------------------------------------

Cette liste doit être controlée, vérifiée par chacun


Les éléments techniques rattachés
=================================

Les éléments rattachés sont les objets techniques qui sont liés à un bien immobilier.
(Une chaudière, une alarme, une ventilation, ...)

Il y a eu un problème d'intégrité lors du transfert du logiciel GIMA vers le logiciel ATAL

Suite à donner
--------------

Les informations relatives aux éléments rattachés seront de nouveau transférées sous ATAL, mais 

 - après avoir validé la liste du patrimoine
 - après avoir "simplifié" ces informations
 - après avoir "réfléchi" à la question "Comment mettre à jour ces informations ?"

Les éléments techniques rattachés
=================================

Pour chacun des éléments, paramétrage sous ATAL d'un objet type.

L'utilisateur est invité à modifier les informations relatives à un élément.

L'utilisateur est invité à modifier les informations relatives à vingt éléments.

L'utilisateur est invité à commenter l'ergonomie du logiciel.

Les documents graphiques (plans, photos, ...)
=============================================

Les informations sur un patrimoine peuvent se présenter sous un format informatique en complément de la base de données gérée par le logiciel ATAL.

Le répertoire de travail SAN\\Projets_Transversaux est au moins divisé en 4

 - Photo
 - Plan
 - Doc_MES
 - Doc_Immo

*************
Les Logiciels
*************

ATAL et son paramètrage
=======================

 - Natures d'équipement
 - Natures d'activité
 - Types d'activité


ATAL et paramètres : Natures d'Equipement
=========================================

Références/Equipements/Natures d'Equipement

Les anciennes natures, pour les batiments, étaient :
 - Affaires Culturelles
 - Affaires Sociales
 - Associatifs
 - Bâtiments divers 2
 - Economat
 - Etablissements Cultuels
 - Etablissements Scolaires

ATAL et paramètres : Natures d'Equipement
=========================================

 - Etablissements Sportifs
 - Jeunesse et Loisirs
 - Locaux Administratifs
 - Magasin Général
 - Salle de prêt
 - services techniques
 - Usage Multiple
 - Véhicules

ATAL et paramètres : Natures d'Equipement
=========================================
Les nouvelles natures sont :

 - Fonction Budgétaire ?

ATAL et paramètres : Natures d'Activité
=======================================

Références/Interventions/Natures d'activité

Aductis préconise que les Natures d'activité servent à répondre à la question
"Pourquoi fait-on cette Intervention ?"

La liste des Natures d'activités préconisée par aductis est donc :
 - Entretien/Maintenance Périodique
 - Dépannage/Réparation
 - Travaux Neufs
 - Sinistre


ATAL et paramètres : Natures d'Activité
=======================================
Or, la liste actuelle des natures d'activité est la suivante :
 - Bâtiments
 - Carburant
 - Contrôle sécurité obligatoire
 - Contrôle technique obligatoire
 - Garage- Accident non responsable
 - Garage- Accident responsable
 - Garage- Entretien Normal
 - Garage Franchise-Assurance
 - Garage- Mauvaise Utilisation/Casse

ATAL et paramètres : Natures d'Activité
=======================================
 - Gestion du service
 - Magasin
 - Parc automobile
 - Petits Travaux
 - Signalisation
 - Transport
 - Voirie


Il faut établir une table de correspondance entre les éléments de la liste utilisée actuellement et les éléments de la liste préconisée par aductis

ATAL et paramètres : Types d'Activité
=====================================

Références/Interventions/Types d'activité

Le but est de pouvoir avoir des statistiques pertinentes :

Pour obtenir le nombre de bons par Atelier et par type d'activité, le rapport à construire est le suivant :

Statistiques/Travaux/Statistiques des Travaux en régie
Dans l'onglet recherche, décocher ordre de réparation (parc auto)
Date comprise entre le 01/01/2013 et le 31/12/2013
Premier critère de regroupement : Atelier exécutant
Second critère de regroupement : Type d'activité
puis cliquer sur recherche

ATAL et paramètres : Types d'Activité
=====================================

Dans l'onglet Statistiques des travaux en régie, faire un clic droit, menu contextuel, edition d'un rapport
Affichage d'une nouvelle fenêtre "edition d'un rapport"
dans l'onglet "Edition personnalisé", choisir imprimer graphique, puis aller dans le sous-onglet graphique
dans cet onglet graphique, choisir les colonnes à utiliser
valeurs : Nb de bons*
par : Atelier | Type d'activité

ATAL et paramètres : Types d'Activité
=====================================

Type de graphique : camembert
Cocher Afficher le détail
Style des valeurs sur le graphiques : 2 colonnes
Type des valeurs sur le graphique : Valeur - Argument
Nbre de lignes pour la légende : 0
Pourcentage minimum pour l'affichage : 2


ATAL et paramètres : Types d'Activité
=====================================

 ...

Excel
=====

L'utilisateur a la possibilité de mettre à jour les données d'ATAL à partir d'un fichier Excel

Excel
=====

Sous ATAL, il y a deux procédures pour ajouter une information à un objet :
  - La méthode "Classification"
  - La méthode "Catégorie"

Excel Classification
====================
Un attribut de type "Classification" est accessible dans l'onglet "Informations Générales"
La configuration de ces attributs se fait dans :
 - Références/Equipements/Quartier
 - Références/Equipements/Secteur
 - Patrimoine/Références/Classifications


Excel Catégorie
===============
Un attribut de type "Catégorie" est accessible dans l'onglet "Infos complémentaires"
La configuration de ces attributs se fait dans :
 - Batiments/Références/Caractéristiques des bâtiments

Excel Avantage du type Catégorie
================================
On peut faire des imports et des exports excel avec les caractéristiques d'un batiment (c'est à dire les attributs de type "Catégorie"),
mais on ne peut pas le faire avec les attributs de type "Classification".




Coriolis (Bon de Commande)
==========================

L'utilisateur a la possibilité d'émettre un bon de commande à partir d'ATAL.


****************
Les Utilisateurs
****************

Liste des utilisateurs et de leurs droits
=========================================

Droits sur la gestion de la liste du patrimoine

 - ajout
 - suppression
 - modification

Droits sur les éléments rattachés (Chaudière, extincteurs, ....)

Liste des utilisateurs et de leurs droits
=========================================

Droits sur le repertoire de travail SAN/Projets_Transversaux
(lecture/ecriture sur les sous-répertoires)

  - photos
  - plans
  - doc_mes
  - doc_immo

Les formations
==============

Les modules d'ATAL que nous ne possédons pas :

 - Module MC3 : Contrat (Contrat de Maintenance)
 - Module MC4 : Travaux Neufs
 - Module MC5 : Fluides
 - Module MC6 : Clefs
 - Module MC7 : ODP (Occupation du domaine public : arrêtés permanents)
 - Module MC9 : Locations et Baux
 - Module SIG : SIG (lien avec cartographie)

