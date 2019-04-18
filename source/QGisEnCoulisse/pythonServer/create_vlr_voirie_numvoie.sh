#!/bin/sh
# script pour executer la mise à jour de la base de données à partir d'une feuille google sheet

echo "# Lancement de la requete SQL"
echo "psql -h localhost -U fred -d espu -f /home/fred/Documents/report/source/QGisEnCoulisse/pythonServer/sql/create_vlr_voirie_numvoie.sql"
      psql -h localhost -U fred -d espu -f /home/fred/Documents/report/source/QGisEnCoulisse/pythonServer/sql/create_vlr_voirie_numvoie.sql
