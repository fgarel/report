#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Script permettant d'executer plusieurs commandes.



"""

import subprocess

def main():
    u"""
    Programme principal.
    
    """
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "Cadastre"], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "CadastreOrthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "CadastreOrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "CadastreReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "Orthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "OrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Paysage", "-l", "Reseaux", ], shell= True)
    
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "Cadastre"], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "CadastreOrthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "CadastreOrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "CadastreReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "Orthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "OrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A4", "-o", "Portrait", "-l", "Reseaux", ], shell= True)
    
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "Cadastre"], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "CadastreOrthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "CadastreOrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "CadastreReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "Orthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "OrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Paysage", "-l", "Reseaux", ], shell= True)
    
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "Cadastre"], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "CadastreOrthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "CadastreOrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "CadastreReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "Orthophotoplan", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "OrthophotoplanReseaux", ], shell= True)
    subprocess.call(["python", "pdfFabric.py", "-f", "A3", "-o", "Portrait", "-l", "Reseaux", ], shell= True)
    
    
if __name__ == '__main__':
    main()
