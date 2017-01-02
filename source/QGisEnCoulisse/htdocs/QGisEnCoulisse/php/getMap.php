<?php
sleep(3);
#$command = escapeshellcmd('python C:\\OSGeo4W\\apache\\htdocs\\python\\do_one.py');
echo exec('python C:\\OSGeo4W\\apache\\htdocs\\python\\do_one.py');
// We'll be outputting a PDF
header('Content-type: application/pdf');
#sleep(3);
// The PDF source is in original.pdf
$result = array('pdfurl' => 'http://qgis/QGisEnCoulisse/pdf/' . 'plan.pdf');
echo json_encode($result);

?>