
-- 1er etape : on va chercher les infos du google spreadsheet
--SELECT * from "voirie_administratif"."numvoie_gspreadsheet";
REFRESH MATERIALIZED VIEW "voirie_administratif"."mv_numvoie_gspreadsheet";


-- 2ème etape : on fait le rapprochement entre une demande et une parcelle
DROP TABLE if exists voirie_administratif.parcelle_tab2;
CREATE TABLE voirie_administratif.parcelle_tab2
AS
  select
    nextval('voirie_administratif.parcelle_tab_id_seq'::regclass) as id, -- Identifiant
    voirie_administratif.mv_numvoie_gspreadsheet.code_demande,
    voirie_administratif.parcelle_vue.codcomm,
    voirie_administratif.parcelle_vue.ccosec,
    voirie_administratif.parcelle_vue.ident,
    voirie_administratif.parcelle_vue.parcelle,
    voirie_administratif.parcelle_vue.codeident,
    voirie_administratif.parcelle_vue.shape,
    --voirie_administratif.mv_numvoie_gspreadsheet.Numero_attribue,
    --voirie_administratif.mv_numvoie_gspreadsheet.Alignement_concerne,
    voirie_administratif.mv_numvoie_gspreadsheet.demande_date,
    voirie_administratif.mv_numvoie_gspreadsheet.demande_type_numerotage,
    voirie_administratif.mv_numvoie_gspreadsheet.demande_type_alignement,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_telephone,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_courriel,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne1_raison_sociale_ou_identite,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne2_identite_ou_complement,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne3_complement,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne4_numvoie_nomvoie,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne5_boite_postal_ou_lieu_dit,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne6_code_postal_ville_cedex,
    voirie_administratif.mv_numvoie_gspreadsheet."bienImmo_vosrefs_ligne1",
    voirie_administratif.mv_numvoie_gspreadsheet."bienImmo_vosrefs_ligne2",
    voirie_administratif.mv_numvoie_gspreadsheet."bienImmo_proprietaire",
    --voirie_administratif.mv_numvoie_gspreadsheet.bienImmo_commune,
    voirie_administratif.mv_numvoie_gspreadsheet.numero,
    voirie_administratif.mv_numvoie_gspreadsheet.suffixe,
    voirie_administratif.mv_numvoie_gspreadsheet.voie_nom,
    voirie_administratif.mv_numvoie_gspreadsheet.observation,
    --voirie_administratif.mv_numvoie_gspreadsheet.ccosec,
    --voirie_administratif.mv_numvoie_gspreadsheet.parcelle,
    --voirie_administratif.mv_numvoie_gspreadsheet.ident,
    --voirie_administratif.mv_numvoie_gspreadsheet.codeident,
    voirie_administratif.mv_numvoie_gspreadsheet.code_fantoir,
    voirie_administratif.mv_numvoie_gspreadsheet.fin_cle_interop,
    voirie_administratif.mv_numvoie_gspreadsheet.cle_interop
  from
    voirie_administratif.parcelle_vue,
    voirie_administratif.mv_numvoie_gspreadsheet
  where
    voirie_administratif.parcelle_vue.codeident = voirie_administratif.mv_numvoie_gspreadsheet.codeident;
ALTER TABLE voirie_administratif.parcelle_tab2
  ADD constraint id_parcelle_tab2_pk PRIMARY KEY (id);
ALTER TABLE voirie_administratif.parcelle_tab2
  ADD CONSTRAINT enforce_geotype_geom CHECK (geometrytype(shape) = 'POLYGON'::text OR geometrytype(shape) = 'MULTIPOLYGON'::text OR shape IS NULL);
ALTER TABLE voirie_administratif.parcelle_tab2
  ADD CONSTRAINT enforce_srid_geom CHECK (st_srid(shape) = 3946);
ALTER TABLE voirie_administratif.parcelle_tab2
  OWNER TO fred;
COMMENT ON TABLE voirie_administratif.parcelle_tab2
  IS 'Table Parcelle rapprochée avec table mv_numvoie_gspreadsheet';


-- 3ème etape : on fait le rapprochement entre une demande et un numero de voirie
DROP TABLE if exists voirie_administratif.numvoie_tab2;
CREATE TABLE voirie_administratif.numvoie_tab2
AS
  select
    nextval('voirie_administratif.parcelle_tab_id_seq'::regclass) as id, -- Identifiant
    voirie_administratif.mv_numvoie_gspreadsheet.code_demande,
    voirie_administratif.numvoie_vue.id_vo_adresse,
    voirie_administratif.numvoie_vue.id_cleabs,
    voirie_administratif.numvoie_vue.numvoie,
    voirie_administratif.numvoie_vue.batiment,
    voirie_administratif.numvoie_vue.angle,
    voirie_administratif.numvoie_vue.shape,
    --voirie_administratif.mv_numvoie_gspreadsheet.Numero_attribue,
    --voirie_administratif.mv_numvoie_gspreadsheet.Alignement_concerne,
    voirie_administratif.mv_numvoie_gspreadsheet.demande_date,
    voirie_administratif.mv_numvoie_gspreadsheet.demande_type_numerotage,
    voirie_administratif.mv_numvoie_gspreadsheet.demande_type_alignement,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_telephone,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_courriel,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne1_raison_sociale_ou_identite,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne2_identite_ou_complement,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne3_complement,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne4_numvoie_nomvoie,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne5_boite_postal_ou_lieu_dit,
    voirie_administratif.mv_numvoie_gspreadsheet.demandeur_ligne6_code_postal_ville_cedex,
    voirie_administratif.mv_numvoie_gspreadsheet."bienImmo_vosrefs_ligne1",
    voirie_administratif.mv_numvoie_gspreadsheet."bienImmo_vosrefs_ligne2",
    voirie_administratif.mv_numvoie_gspreadsheet."bienImmo_proprietaire",
    --voirie_administratif.mv_numvoie_gspreadsheet.bienImmo_commune,
    voirie_administratif.mv_numvoie_gspreadsheet.numero,
    voirie_administratif.mv_numvoie_gspreadsheet.suffixe,
    voirie_administratif.mv_numvoie_gspreadsheet.voie_nom,
    voirie_administratif.mv_numvoie_gspreadsheet.observation,
    --voirie_administratif.mv_numvoie_gspreadsheet.ccosec,
    --voirie_administratif.mv_numvoie_gspreadsheet.parcelle,
    --voirie_administratif.mv_numvoie_gspreadsheet.ident,
    --voirie_administratif.mv_numvoie_gspreadsheet.codeident,
    voirie_administratif.mv_numvoie_gspreadsheet.code_fantoir,
    voirie_administratif.mv_numvoie_gspreadsheet.fin_cle_interop,
    voirie_administratif.mv_numvoie_gspreadsheet.cle_interop
  from
    voirie_administratif.numvoie_vue,
    voirie_administratif.mv_numvoie_gspreadsheet
  where
    voirie_administratif.numvoie_vue.numvoie_num::varchar = voirie_administratif.mv_numvoie_gspreadsheet.numero
	and voirie_administratif.numvoie_vue.numvoie_complement = voirie_administratif.mv_numvoie_gspreadsheet.suffixe
	and voirie_administratif.numvoie_vue.nomvoie = voirie_administratif.mv_numvoie_gspreadsheet.voie_nom;
ALTER TABLE voirie_administratif.numvoie_tab2
  ADD constraint id_numvoie_tab2_pk PRIMARY KEY (id);
ALTER TABLE voirie_administratif.numvoie_tab2
  ADD CONSTRAINT enforce_geotype_geom CHECK (geometrytype(shape) = 'POINT'::text OR geometrytype(shape) = 'MULTIPOINT'::text OR shape IS NULL);
ALTER TABLE voirie_administratif.numvoie_tab2
  ADD CONSTRAINT enforce_srid_geom CHECK (st_srid(shape) = 3946);
ALTER TABLE voirie_administratif.numvoie_tab2
  OWNER TO fred;
COMMENT ON TABLE voirie_administratif.numvoie_tab2
  IS 'Table Numvoie rapprochée avec table mv_numvoie_gspreadsheet';
