==========================
Le serveur web avec python
==========================

Un serveur Web avec un script python pour piloter QGis
======================================================

Les outils : Apache + mod_wsgi
------------------------------

Le serveur Apache va etre le serveur HTTP

Il est configuré avec le module **mod_wsgi** afin de pouvoir utiliser python
comme langage de script.


----



todo :
2 sources d'inspiration a travailler :

 - youtube youtube deploying flask apps to an ubuntu server
   https://www.youtube.com/watch?v=kDRRtPO0YPA

 - https://www.codementor.io/uditagarwal/tutorials/how-to-deploy-a-django-application-on-digitalocean-du1084ylz

# resume de la premiere source, la video




# resume de la seconde source, le tuto

# synthese des deux sources



----


Prerequisites

    A fresh DigitalOcean droplet running Ubuntu 14.04
    A Git Repository (on Bitbucket or Github) which you use with your Django Application
    You should have a local Django app setup using Postgres setup neatly in a virtualenv
    Local computer running OSX or Linux

Introduction

Django is an 11-year-old web-framework written in the Python language. It is an extremely mature and extensively used framework because of its large support for Python libraries. It’s meant to code and deploy changes, fast, because it was originally developed for a news publishing website. The support from the Python ecosystem is huge and you can make any sort, and getting them to work together.

All web applications require a database to store all the data that’s going to be used. PostgreSQL is an object-relational Database Management System (ORDBMS). It works great with Django and has a very active developer community. The database has great support for spatial (geographical) & unstructured data as well, which makes working with Longitudes and Latitudes in Django a breeze. (see Postgis)

Once you have your Django app running, you’d want to run it behind a web server. Think of a web server as a computer program that runs your Django application and opens it to the web. While testing, Django runs its own server, but it’s not recommended to do this in actual production. Using a web server like Nginx is a great choice. Millions of websites across the world run on Nginx (Apache is another webserver which can run Django apps). It is free and open source software that can act as a reverser-proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols.

To make it all come together, we need to setup a bridge between our Django app and the Web server. Gunicorn is a gateway interface (WSGI) that acts as a bridge between the web server and the web application. We configure Gunicorn to run our Django application, restart it if a crash happens, and set other configuration options for our Django application.

On the other hand, DigitalOcean is a web-service where you can rent out a server for your application to deploy to the web. Coupled with an online Git account, it makes it very easy to deploy a Django web-app from your local machine to your DigitalOcean server.
Target

    For this tutorial, we will deploy a local Django app called myproject and deploy it to our DigitalOcean server after configuring Postgres, Nginx, and Gunicorn on it
    Let’s Go!

Local File Directory Structure

We are going to be deploying a Django Application called myproject to our servers. Our directory is structured this way: the root of our django application is myproject.

    myproject
        manage.py
        myproject
            \_init__.py_
            settings.py
            urls.py
            wsgi.py

Our settings file looks like this. We have our database set to the postgresql adapter, with a DATABASES setting configured as shown. We are connecting to a postgres database called mydb which has privileges from myuser with a password set and running on a localhost on the default port.

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'mydb',
      'USER': 'myuser',
      'PASSWORD': 'password',
      'HOST': 'localhost',
      'PORT': '',
  }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'
STATICFILES_DIRS = [..DIRS..]

Serving static files from Django depends on the STATIC_URL, STATIC_ROOT, and STATICFILES_DIRS

    The STATICFILES_DIRS gives a list of all the folders on our computer where we have the static files stored. This can be across different apps you’ve created.
    The STATIC_ROOT folder is where Django collects all these files after you’ve run the collectstatic command. Django takes a look at all the directories and copies them to your STATIC_ROOT folder.
    The STATIC_ROOT folder is connected to our STATIC_URL, and the web server uses these files to serve them to the browser.

After setting the correct values, we will initialize a git repository and push it online to github. Go to your root directory and run the following commands. Make sure you created an empty repository on your github account.

git init # Initialize the empty git repository

vim .gitignore # Create a gitignore file for Django and save it

git add . # Add files to the git repository
git commit -m "First commit" # Add the first commit
git log # Check the logs to see if the git has been committed

git remote add origin # add the remote repository locally called 'origin'
git push origin master # push it to the master branch on your 'origin' repository on the web

Now, we are ready to get ahead and put our django application on our DigitalOcean server.
Deploying on DigitalOcean Server
SSH and Package Installation

Open the terminal and type the command to go to your digital ocean server

ssh -l root

The ssh commands logs you into the root user of the Digitalocean Ubuntu server. This is generally considered bad practice and you should create another non-root user and run your Django application using it. For the sake of this tutorial, we are going to use the root user, but all the steps should even work when you’ve created a non-root user with sudo privileges on your Ubuntu machine. Once we are in our ssh server, we run the following commands:

sudo apt-get update
sudo apt-get install python-pip

We update our package manager and then install pip to manage our python libraries. Once installed, you can check the pip version using:

pip --version

django application

Next, we install all the necessary packages on our server to run our application. The python libraries, the postgresql packages, and the Nginx server.

# Python and Debian package, python headers and postgresql library for python
sudo apt-get install python-dev libpq-dev

# Postgresql Package
sudo apt-get install postgresql postgresql-contrib

# Nginx Package
sudo apt-get install nginx

sudo apt-get install git

sudo apt-get install gunicorn

Create a PostgreSQL Database

We switch to the postgres user and run the psql command. This logs us into the postgresql command line interface. Here we can interact with our Postgres server, create a new database, make a user and grant privileges to it to create, and modify tables on our database. Django connects to the database as this user and runs these commands for us.

sudo su postgres

psql

django application Create a database named mydb for your application

CREATE DATABASE mydb;

django application Create a user to access the database

CREATE USER myuser WITH PASSWORD 'password';

django application

Give database access to the user

GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

django application

\q;
exit

Exit out of psql and postgres!
Create a Python Virtual Environment for your project

Install virtualenv to create a virtual environment

sudo pip install virtualenv

django application

Create a directory for your project and switch over to it

mkdir ~/myproject
cd ~/myproject

django application

Create a virtualenv in your project’s directory

virtualenv myprojectenv

django application

If you check your project directory, a new directory is created inside it which contains the local version of python and local version pip.

Activate virtual environment before installing required packages

source myprojectenv/bin/activate

django application

Now you can install Django, Gunicorn, and Psycopg2.

Psycopg2 is a postgreSQL database adapter for Python. It is used to integrate postgreSQL with the Python. Gunicorn is the interface for our Nginx server

pip install django
pip install psycopg2

django application

django application

Before we test the Gunicorn, we need to import our repository locally from github
Pulling our Git Repository

We need to pull our git repository from github and pull our updated code on the server.

Navigate to the virtualenv directory and clone the git repository

cd ~/myproject
git clone

This will pull and create all the folders of your Django app on the Ubuntu server. You can now go ahead and setup your app to run with Gunicorn
Unleash the Gunicorn

If you followed the steps properly, you should have a Django project running correctly at this point. But now we will test the Gunicorn with our app. Start Gunicorn on the same interface your Django development server is running.

gunicorn --bind 0.0.0.0:8000 mydjangoproject.wsgi:application

django application

Open the url as http://>:8000 and you’d see the Welcome to Django! Page. If you’ve come this far, your app should work fine on your server. And now it’s time to configure Nginx to run it.

After you finish testing, hit CTRL-C

We are now finished creating our app and we can exit from our virtual environment

deactivate

django application
Create a Gunicorn Upstart File

Gunicorn can be used to interact with our app, but instead of starting up our server this way, we will make an upstart script to start and stop the server.

Create and open a file

sudo nano /etc/init/gunicorn.conf

django application

Type the following lines in it.

description "Gunicorn application server handling mydjangoproject"

start on runlevel [2345]
stop on runlevel [!2345]

django application

Here, the first line tells what our file is for i.e. the description of our file. Next we will define the system runlevel where the service should be automatically started and stopped. Linux runlevels are numbered from 0 to 6.
0 : System Halt
1 : Single User
2-5 : Full multiUser mode
6 : System reboot

So our service will run when system is on any of 2, 3, 4, and 5. And it will stop when it is on any other level apart from these.

Add the following lines to protect it from failure

respawn
setuid root
setgid www-data
chdir /root/myproject

django application

Here, respawn commands automatically restarts the service if it fails. We also specify the user and group to run under. Since we are just using the root user, we will set the uid to root but gid (groupid) to www-data as that is what Nginx is ran under; although it’s never a good practice to run the directory under root, and you should run it under another user for security purposes.

Add the command to start our Gunicorn service.

exec gunicorn --workers 3 --bind unix://mydjangoproject.sock mydjangoproject.wsgi:application

Here, first we give the path to Gunicorn executable, which is stored inside our virtual environment. We will tell it to use a network socket instead of a network port to communicate with Nginx.

sudo service gunicorn start

django application

If everything succeeded thus far, we just have to setup Nginx to proxy instances to our Gunicorn socket file. Be mindful when using the right paths so that everything works correctly.
Configure Nginx to Pass traffic to the Processes

Now that our Gunicorn is setup, we can configure Nginx to proxy web requests to it.

Step 1: We will first create a site called myproject under our nginx sites-available directory

sudo nano /etc/nginx/sites-available/myproject

django application

Step 2: Add the following lines of code to the myproject file

server {
    listen 80;
    server_name Your server name or your IP address;
}

Here, it will listen on the normal port 80 and we specify our server name as IP address. You can also specify this server name as your server domain name.

Step 3: Ignore all problems on finding favicon

location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
      root /root/myproject;
}

Here, we tell it to point to our static files, which is in the myproject/static directory

Step 4: Create a new location block to match all the requests.

location / {
     include proxy_params;
     proxy_pass http://unix:/mydjangoproject.sock;
}

django application

Here we included the standard proxy_params included with the Nginx installation. We pass the traffic to the Gunicorn socket we created previously.

Note: The paths mentioned in the files may vary from machine to machine. So check your paths and make the changes correspondingly.

Save and close the file.

Step 5: Enable the file.

sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled

django application

We can test the syntax errors by

sudo nginx -t

django application

Step 6: If no syntax errors are reported restart Nginx

sudo service nginx restart

django application

Go to your server_address/admin and you will see your Django app running

django application
Conclusion

This brings us to the end of this tutorial! We now have a DigitalOcean server running Django, NGINX, and Gunicorn. Every time we want to update our repository on DigitalOcean, we can ssh into it and do a git pull to fetch the latest updates from a Git repository! The entire process to deploy after the initial setup can be automated using a Fabric script. But that’s a part of another tutorial. If you have any suggestions to make this better, please put it in the comments below!
