from cgi import parse_qs, escape
import json
#import sys, os

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

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    layers = d.get('layers', [''])[0] # Returns the first geojson.
    orientation = d.get('orientation', [''])[0] # Returns the first geojson.
    format = d.get('format', [''])[0] # Returns the first geojson.
    geojson = d.get('geojson', [''])[0] # Returns the first geojson.

    # Always escape user input to avoid script injection
    layers = escape(layers)
    orientation = escape(orientation)
    format = escape(format)
    geojson = escape(geojson)

    
    response_body = html % { # Fill the above html template in
        'layers': layers or 'Empty',
        'orientation': orientation or 'Empty',
        'format': format or 'Empty',
        'geojson': geojson or 'Empty'
    }
    #response_body = 'Contenu du post  :' + ' layers = ' + str(layers) + ' ; orientation = ' + str(orientation) + ' ; format = ' + str(format)
    
    status = '200 OK'
    response_body=json.dumps({'pdfurl':'http://localhost/QGisEnCoulisse/pdf/centre_ville.pdf'})
    response_headers = [('Content-type', 'application/json'),('Content-Length', str(len(response_body)))]
    #response_headers = [('Content-type', 'application/pdf')]
    start_response(status, response_headers)
    #fin = open('centre_ville.pdf', "rb")
    #return fin.read()

    return [response_body]
    
    


