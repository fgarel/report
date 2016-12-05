# Une présentation

Mise en place d'une chaine pour écrire une présentation

# Les outils

## Pandoc

Installation de l'outil pandoc

`aptitude install pandoc`

## Hovercraft

# La configuration de ces outils

## Scripts à recopier

pandoc1To3.sh

modification du fichier
~/Documents/report/Makefile

`
ligne 7:
HOVERCRAFT    = hovercraft

lignes 42 et 43 :
@echo "  slideshie  to make slides, hieroglyph"
@echo "  slideshov  to make slides, hovercraft"


puis, vers la ligne 120 :
slideshie:
  $(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) $(BUILDDIR)/slideshie
	@echo "slides finished. The HTML slides are in $(BUILDDIR)/slideshie."

slideshov:
  #$(HOVERCRAFT) source/hovercraftPositions.rst $(BUILDDIR)/slideshov
	#cp $(BUILDDIR)/slideshov/index.html $(BUILDDIR)/slideshov/hovercraftPositions.html
	#$(HOVERCRAFT) source/hovercraftTutorial.rst $(BUILDDIR)/slideshov
	#cp $(BUILDDIR)/slideshov/index.html $(BUILDDIR)/slideshov/hovercraftTutorial.html
	#$(HOVERCRAFT) source/hovercraftHovercraft.rst $(BUILDDIR)/slideshov
	#cp $(BUILDDIR)/slideshov/index.html $(BUILDDIR)/slideshov/hovercraftHovercraft.html
	#$(HOVERCRAFT) source/hovercraft.rst $(BUILDDIR)/slideshov
	#cp $(BUILDDIR)/slideshov/index.html $(BUILDDIR)/slideshov/hovercraft.html
	# index ( attention  à la directive include )
	#$(HOVERCRAFT) source/index.rst $(BUILDDIR)/slideshov
	# geogig_hovercraft
	$(HOVERCRAFT) source/QGisEnCoulisse/presentation_hov.rst $(BUILDDIR)/slideshov
	cp $(BUILDDIR)/slideshov/index.html $(BUILDDIR)/slideshov/presentation_hov.html
	#$(HOVERCRAFT) source/geogig/geogig.rst $(BUILDDIR)/slideshov
	#cp $(BUILDDIR)/slideshov/index.html $(BUILDDIR)/slideshov/geogig.html
	@echo "slides finished. The HTML slides are in $(BUILDDIR)/slideshov."

    `
## Modèle de presentation


## Création des slides
pew workon ecriture_sphinx
(hovercraft)
make


## et Plantuml ?

@startuml
actor "Utilisateur A"
participant Navigateur
participant "Serveur HTTP"
actor "Utilisateur B"
participant "QGis Dektop"
participant "QGis Server"

"Utilisateur B" -> "QGis Dektop" : Préparation des\nfichiers .qgs et .tpl
"Utilisateur B" -> "QGis Server" : Le fichier .qgs\nest intégré dans\nla configuration de\nQgis Server
"Utilisateur A" -> "Navigateur" : Formulaire
"Navigateur" -> "QGis Server" : Demande d'un flux WMS
"Navigateur" <- "QGis Server" : Affichage du flux WMS
"Navigateur" -> "Serveur HTTP" : Fourniture d'une\nemprise géographique\n(POST)
"Serveur HTTP" -> "QGis Dektop" : Commandes Python
"Serveur HTTP" <- "QGis Dektop" : Fourniture de la carte\nau format pdf
"Navigateur" <- "Serveur HTTP" : Fourniture du\nfichier résultat
"Utilisateur A" <- Navigateur : Affichage de la carte
@enduml
