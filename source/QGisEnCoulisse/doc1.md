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




# Configuration du serveur web

utilisation de nginx

1. creer un lien symbolique de
```
/var/www
```
vers notre repertoire web
```
/home/fred/Documents/report/source/QGisEnCoulisse/webServer/
```

```
sudo ln -s /home/fred/Documents/report/source/QGisEnCoulisse/webServer/ \
           /var/www/QGisEnCoulisse
```

attention, il faut aussi que l'utilisateur www-data puisse parcourir le dossier
et les sous-dossiers

```
cd /home/fred/Documents/report/source/QGisEnCoulisse/webServer/
chmod 755 bootstrap-3.3.7
```


2. faire en sorte que le serveur nginx aille au bon endroit

modification du fichier de configuation de nginx
```
sudo su

vi /etc/nginx/sites-available/default
```

il faut remplacer
```
root /var/www/gup
```
par
```
root /var/www/QGisEnCoulisse
```
et meme mieux, par
```
root /var/www/
```


```
service nginx reload
```

# Configuraiton du serveur web pour python

1. creer un lien symbolique de
```
/var/www
```
vers notre repertoire python
```
/home/fred/Documents/report/source/QGisEnCoulisse/webServer/
```

```
sudo ln -s /home/fred/Documents/report/source/QGisEnCoulisse/pythonServer/ \
           /var/www/python
```


2. creation d'un environnement virtuel python

La doc est ici :
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04



pew new myappenv
pip freeze
pip install --upgrade pip

3. installation de uwsgi

pip install uwsgi

uwsgi --version

4. installation de flask

5. Creation du fichier myProject.py

```
vi myProject.py
```

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

```
test

```
python myProject.py
```

```
http://localhost:5000/
```

6. Creation du fichier wsgi.py


```
vi wsgi.py
```

```
from myProject import app

if __name__ == "__main__":
    app.run()

```
test

```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

```
http://localhost:5000/
```

7. Creation d'un fichier de configuration

```
vi myProject.ini
```

```
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = myProject.sock
chmod-socket = 660
vacuum = true

die-on-term = true
```


8. creation d'un fichier systemd unit file


```
sudo vi /etc/systemd/system/myProject.service
```


```
[Unit]
Description=uWSGI instance to serve myProject
After=network.target

[Service]
User=fred
Group=www-data
WorkingDirectory=/home/fred/Documents/report/source/QGisEnCoulisse/pythonServer
Environment="PATH=/home/fred/.virtualenvs/myappenv/bin"
ExecStart=/home/fred/.virtualenvs/myappenv/bin/uwsgi --ini myProject.ini

[Install]
WantedBy=multi-user.target
```


enregistrement pour que le service se lance au demarrage

```
sudo systemctl start myProject
sudo systemctl enable myProject
```


```
sudo service myProject stop
sudo service myProject status

sudo service myProject start
sudo service myProject status
```


 9. Configurer nginx pour proxy vers wsgi
 ```
 sudo vi /etc/nginx/sites-available/myProject
 ```


```
server {
    listen 80;
    server_name ;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/fred/Documents/report/source/QGisEnCoulisse/pythonServer/myProject.sock;
    }
}
```

```
sudo ln -s /etc/nginx/sites-available/myProject /etc/nginx/sites-enabled
```

```
sudo nginx -t
```
