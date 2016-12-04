===========================
La documentation officielle
===========================

----

Dans cette annexe, nous décrivons où se trouve la documentation en ligne.

Le manuel geogig
================

Récupération du manuel sur le site geogig.org
http://geogit.org/docs/

Nous allons telecharger les pages, puis nous allons l'adpader

Ligne de commande pour telecharger un site

.. code::

  rm -r geogit.org
  wget -H -N -k -p http://geogit.org/docs/
  wget -N -k -p http://geogit.org/docs/

  rm -r geogit.org ; wget -N -k -p http://geogit.org/docs/ ; wget -x -r http://geogit.org/docs/img/

-H = Allows wget to go to span a foreign host. Required since tumblr does not have its images on the front page on the same address, they are using secure.assets.tumblr.com see note on excluding domains

-N = will grab only files that are newer that what you currently have, in case you are downloading the same page again over time

-k = convert your links to view it offline properly

-p = grabs all required elements to view it correctly (css, images, etc)

----

Traduction des pages
--------------------

Une fois que le manuel est téléchargé, nous avons aussi la possibilité de le traduire

----

La documentation avancée
========================


La documentation avancée, avec diagramme uml (cas d'utilisation) est ici.
https://github.com/boundlessgeo/GeoGit/wiki/use-case-worksheet
Le plus simple est de cloner le wiki

.. code::

  #wget -N -k -p https://github.com/boundlessgeo/GeoGit/wiki/use-case-worksheet
  git clone https://github.com/boundlessgeo/GeoGit.wiki.git

----
