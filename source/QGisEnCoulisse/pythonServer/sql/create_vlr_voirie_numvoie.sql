-- pour se connecter, on utilise multicorn
CREATE EXTENSION IF NOT EXISTS multicorn;

-- Pour faire le rafraîchissement des données, on pensait pouvoir utiliser pg_cron
-- (l'installation de pg_cron necessite de modifier postgresql.conf)
--CREATE EXTENSION IF NOT EXISTS pg_cron;

DROP SERVER IF EXISTS multicorn_gspreadsheet CASCADE;
CREATE SERVER IF NOT EXISTS multicorn_gspreadsheet FOREIGN DATA WRAPPER multicorn
options (
  wrapper 'gspreadsheet_fdw.GspreadsheetFdw' );

DROP FOREIGN TABLE IF EXISTS "voirie_administratif"."numvoie_gspreadsheet" CASCADE;
CREATE FOREIGN TABLE IF NOT EXISTS "voirie_administratif"."numvoie_gspreadsheet" (
  "code_demande"                                character varying,
  "demande_date"                                character varying,
  "demande_type_numerotage"                     character varying,
  "demande_type_alignement"                     character varying,
  "demandeur_telephone"                         character varying,
  "demandeur_courriel"                          character varying,
  "demandeur_ligne1_raison_sociale_ou_identite" character varying,
  "demandeur_ligne2_identite_ou_complement"     character varying,
  "demandeur_ligne3_complement"                 character varying,
  "demandeur_ligne4_numvoie_nomvoie"            character varying,
  "demandeur_ligne5_boite_postal_ou_lieu_dit"   character varying,
  "demandeur_ligne6_code_postal_ville_cedex"    character varying,
  "bienImmo_vosrefs_ligne1"                     character varying,
  "bienImmo_vosrefs_ligne2"                     character varying,
  "bienImmo_proprietaire"                       character varying,
  "numero"                                      character varying,
  "suffixe"                                     character varying,
  "voie_nom"                                    character varying,
  "observation"                                 character varying,
  "ccosec"                                      character varying,
  "parcelle"                                    character varying,
  "ident"                                       character varying,
  "codeident"                                   character varying,
  "code_fantoir"                                character varying,
  "fin_cle_interop"                             character varying,
  "cle_interop"                                 character varying
) server multicorn_gspreadsheet options(
  gskey   '1tqbwCCnLioPfEe1xNq00vKlF7H-fZ6cJdHJxFsYWAJQ',
  headrow '1',
  keyfile '/var/lib/postgresql/11/main/debianpaquetmapnik-e8255c38290e.json'
);

--SELECT * from "voirie_administratif"."numvoie_gspreadsheet" ;

-- Oh, you want it faster?  use a materialized view to cache it:
DROP MATERIALIZED VIEW IF EXISTS "voirie_administratif"."mv_numvoie_gspreadsheet";
CREATE MATERIALIZED VIEW IF NOT EXISTS "voirie_administratif"."mv_numvoie_gspreadsheet" AS SELECT * FROM "voirie_administratif"."numvoie_gspreadsheet";

--SELECT * from "voirie_administratif"."mv_numvoie_gspreadsheet";

-- Periodically refresh (use a trigger or something)
--REFRESH MATERIALIZED VIEW "voirie_administratif"."mv_numvoie_gspreadsheet";

-- Pour faire ce rafraîchissement on pensait pouvoir utiliser pg_cron
-- (l'installation de pg_cron necessite de modifier postgresql.conf)
--CREATE EXTENSION IF NOT EXISTS pg_cron;

--select cron.unschedule(1);
--select cron.unschedule(2);
--select cron.unschedule(3);
--SELECT cron.schedule('*/5 * * * *', $$SELECT * FROM "voirie_administratif"."numvoie_gspreadsheet";$$);
--SELECT cron.schedule('*/5 * * * *', $$REFRESH MATERIALIZED VIEW "voirie_administratif"."mv_numvoie_gspreadsheet";$$);
--SELECT cron.schedule('*/5 * * * *', $$SELECT * FROM "voirie_administratif"."mv_numvoie_gspreadsheet";$$);

--SELECT * from "voirie_administratif"."mv_numvoie_gspreadsheet";
