#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
import json
#import sys, os
import subprocess
import time
#import pdfFabric

html = """
%(layers)s
%(orientation)s
%(format)s
%(geojson)s

"""



def application(environ, start_response):
    
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    
    # Recupération des données passées via la méthode POST
    # ####################################################
    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)
    
    format = d.get('format', [''])[0] # Returns the first geojson.
    orientation = d.get('orientation', [''])[0] # Returns the first geojson.
    layers = d.get('layers', [''])[0] # Returns the first geojson.
    geojson = d.get('geojson', [''])[0] # Returns the first geojson
    
    # Always escape user input to avoid script injection
    format = escape(format)
    orientation = escape(orientation)
    layers = escape(layers)
    geojson = escape(geojson)
    
    # Enregistrement du geojson sur le disque
    # #######################################
    file=open('c:/osgeo4w/apache/htdocs/python/geojson.geojson', 'w')
    file.write(geojson)
    file.close()
    
    # Lancement de l' utilitaire pdfFabric.py
    # #######################################
    #subprocess.call("start python pdfFabric.py")
    path = '../QGisEnCoulisse/pdf/plan.pdf'
    output = subprocess.check_output(['dir'], shell=True)
    output = subprocess.check_output(['dir', '*.*'], shell=True)
    output = subprocess.check_output(['python', '--version'], shell=True)
    
    output = subprocess.call(['python', 'pdfFabric.py', '-f', 'format', '-o', 'orientation', '-l', 'layers'], shell=True)
    file=open('c:/osgeo4w/apache/htdocs/python/do_one.py', 'w')
    file.write("import subprocess\n")
    file.write("subprocess.call([" + 
               '"' + "python" + '", ' +
               '"' + "pdfFabric.py" + '", ' +
               '"' + "-f" + '", ' +
               '"' + format + '", ' +
               '"' + "-o" + '", ' +
               '"' + orientation + '", ' +
               '"' + "-l" + '", ' +
               '"' + layers + '", ' +
               "], shell= True)\n")
    file.close()
    #os.system("dir")
    #os.system('python --version')
    #os.system('dir')
    #print output
    
    
    # renvoi la reponse au client
    response_body = html % { # Fill the above html template in
        'format': format or 'Empty',
        'orientation': orientation or 'Empty',
        'layers': layers or 'Empty',
        'geojson': geojson or 'Empty'
    }
    #response_body = 'Contenu du post  :' + ' layers = ' + str(layers) + ' ; orientation = ' + str(orientation) + ' ; format = ' + str(format)
    
    status = '200 OK'
    response_body=json.dumps({'pdfurl':'http://qgis/QGisEnCoulisse/pdf/plan.pdf'})
    response_headers = [('Content-type', 'application/json'),('Content-Length', str(len(response_body)))]
    #response_headers = [('Content-type', 'application/pdf')]
    start_response(status, response_headers)
    #fin = open('centre_ville.pdf', "rb")
    #return fin.read()
    return [response_body]


#if __name__ == '__main__':
#    application('', '')