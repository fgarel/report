=========
Evolution
=========

----

Package GeoSHAPE
================

GeoSHAPE is the integration of a geospatial portal (GeoNode), a web mapping client (MapLoom), and a mobile application (Arbiter), that leverages the infrastructure provided by a geospatial server and database components (The OpenGeo Suite)

http://geoshape.org/

https://docs.google.com/document/d/1KMpk6dXuqvwfEi0pfRpaGY62j6ikoYtpYUPU0sJQAmk/edit

https://github.com/ROGUE-JCTD/rogue_geonode

https://speakerdeck.com/scottevil/distributed-versioned-editing-in-action

http://boundlessgeo.com/2014/03/geogit-and-openstreetmap-for-yolanda/

gestion des conflits

http://garnertb.io/geonode-summit-2014/template#11

----

Autres briques logicielles
==========================

Geogig et geoserver
-------------------

Geogig peut être utilisé avec geoserver (sous la forme d'un plugin)

Utilisation de geogig avec geoserver
http://geogig.org/docs/interaction/geoserver_ui.html
http://docs.geoserver.org/latest/en/user/extensions/index.html#extensions

https://github.com/boundlessgeo/geoserver-exts

A GeoServer extension is available to allow GeoServer to interact with
a GeoGig repository and use it as data store.

It enables a GeoGig repository to be exposed as a remote for cloning,
pushing and pulling as well as via OGC services (WMS/WFS/WMTS etc).

Each top level tree in a GeoGig repository corresponds to a GeoServer layer.

GeoServer treats a GeoGig repository as a store in much
the same way as it does a database.

http://dev.boundlessgeo.com/~groldan/geogig-user-manual/interaction/geoserver_ui.html

----

Geonode
-------

GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data. http://geonode.org/

http://geonode.org/

https://github.com/GeoNode/geonode

Mais poour le moment, on est en version 2.4....

la version 2.5 promet l'intégration de geogig


Geogig et geonode 2.5
.....................

On y parle aussi d'OSM...

https://github.com/GeoNode/geonode/issues/1931

MapLoom
-------

MapLoom is a web mapping client based on OpenLayers 3. It provides full-featured editing capabilities for data stores in GeoServer - including PostGIS and GeoGig. For GeoGig layers, it lets you view history, and sync with other GeoGig repositories

https://github.com/ROGUE-JCTD/MapLoom

https://vimeo.com/106852747

----

karta et geogig-py
------------------

Utilisation de karta
https://github.com/fortyninemaps/karta
ou de shapely ??
https://github.com/Toblerity/Shapely

utilisation de karta
http://fortyninemaps.com/kartadocs/tutorial.html
associé avec geogig-py
https://github.com/boundlessgeo/geogig-py

https://github.com/boundlessgeo/geogig-py/blob/master/doc/source/usage.rst
https://github.com/boundlessgeo/geogig-py/blob/master/doc/source/examples.rst

----
