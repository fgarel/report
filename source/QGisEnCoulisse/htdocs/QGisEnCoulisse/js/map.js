/**
*
*
**/
var map,source;
function initMap(){
	var style = new ol.style.Style({
	  fill: new ol.style.Fill({
		color: 'rgba(255, 255, 255, 0.8)'
	  }),
	  stroke: new ol.style.Stroke({
		color: '#cdcdcd',
		width: 2
	  })
	});
	var projectionCC46 = new ol.proj.Projection({
	  code: 'EPSG:3946',
	  // The extent is used to determine zoom level 0. Recommended values for a
	  // projection's validity extent can be found at http://epsg.io/.
	  extent: [1372000.0,5207000.0,1403020.0000000002 , 5238000.0],
	  units: 'm'
	});	
	var ortho2013Extend =projectionCC46.getExtent();// [1372000,5207000,1405000, 5240000]
	var matrixIds = new Array(11);
	var resolutions = new Array(11);
	var size = ol.extent.getWidth(ortho2013Extend) / 302;
	for (var z = 0; z < 11; ++z) {
	  // generate resolutions and matrixIds arrays for this WMTS
	  resolutions[z] = size / Math.pow(2, z);
	  matrixIds[z] = z;
	}
	var ortho2013=new ol.layer.Tile({
      opacity: 0.7,
      extent:ortho2013Extend,
      source: new ol.source.WMTS({
        url: 'https://sigar.agglo-larochelle.fr/CeramikServer/rest/wmts/cdalr/ortho2013?',
        layer: 'ortho2013',
        matrixSet: 'EPSG:3946',
        format: 'image/jpag',
		transparente:true,
		transparent:true,
        projection: projectionCC46,
        tileGrid: new ol.tilegrid.WMTS({
          origin: ol.extent.getTopLeft(ortho2013Extend),
          resolutions: resolutions,
          matrixIds: matrixIds,
		  tileSize:302
        }),
        style: 'default'
      })
    })
	source = new ol.source.Vector({wrapX: false});
    var printExtentLayer = new ol.layer.Vector({source: source});
    //layer QGis
    var qgisEnCoulisse = new ol.layer.Image({
					title: 'Reseaux',
					source: new ol.source.ImageWMS({
                        url: 'http://localhost/qgis-ltr/qgis_mapserv.fcgi.exe?map=QGisEnCoulisse.qgs',
						params: {'LAYERS': 'ortho2013,cadastre','FORMAT': 'image/png', 'CRS':'EPSG:3946'}})
					}),
	
	map = new ol.Map({
		layers:[qgisEnCoulisse,printExtentLayer],
		target: 'map',
		controls:[],
		/*controls: ol.control.defaults().extend([
			new ol.control.MousePosition()
		]),*/
		view: new ol.View({
			projection: projectionCC46,
			center: [1377000,5227000],
			extent: ortho2013Extend,
			zoom:4
		})
	});
    var draw = new ol.interaction.Draw({
        source: source,
        type: "Polygon"
    });
    map.addInteraction(draw);

    draw.on('drawend', function (e) {
        countFeatureForBadge();
    });
}
function countFeatureForBadge(){
    var badge = $("#badge");
    var count = source.getFeatures().length;
    badge.text(count);
}

function createShape(){
        var mapExtent = map.getView().calculateExtent(map.getSize());
        //var coordinates = [2 * e * Math.random() - e, 2 * e * Math.random() - e];
        var feature = new ol.Feature(new ol.geom.Polygon.fromExtent(mapExtent));
        source.clear();
        source.addFeature(feature);
        
}
function eraseDraw(){
    source.clear();
    countFeatureForBadge();
}
function getMaps(){
    var badge = $("#badge");
    var nmbr= badge.text();
    if(nmbr=="0"){
        alert("Aucune géométrie saisie");
        $('#myModal').modal('hide');
    }else{
        $('#myModal').modal({show:true, backdrop:'static', keyboard:false});
        var paramsLayer = "CadastreReseaux";
        var paramOrientation = $("#comboOrientation").val();
        var paramFormat = $("#comboFormat").val();
        //creation d'un geojson
        var geojson  = new ol.format.GeoJSON();
        var  json = geojson.writeFeatures(source.getFeatures());
		//alert(paramsLayer);
		//alert(paramOrientation);
		//alert(paramFormat);
		//alert(json);
        $.ajax({
            type: "POST",
            url: "../python/getMap.py",
            data: "layers=" + paramsLayer + "&orientation=" + paramOrientation + "&format=" + paramFormat+ "&geojson=" + json,
            dataType: "json",
            success : function(res, statut){
                if (statut == "success"){
                     if (res.pdfurl) {
                        //window.open(res.pdfurl, '_blank');
						getMapsPhp();
                    }
                }
            },
            error :function(resultat, statut, erreur){
                alert("Error");
            },
            complete : function(resultat, statut){
                $('#myModal').modal('hide');
            }
        });
    }
   
}
function getMapsPhp(){
	$.ajax({
	type: "POST",
	url: "php/getMap.php",
	dataType: "json",
	success : function(res, statut){
		if (statut == "success"){
			 if (res.pdfurl) {
				window.open(res.pdfurl, '_blank');
			}
		}
	},
	error :function(resultat, statut, erreur){
		alert("Error");
	},
	complete : function(resultat, statut){
		$('#myModal').modal('hide');
	}
});
}
initMap();
