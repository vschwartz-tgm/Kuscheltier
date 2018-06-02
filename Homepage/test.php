<?php
$dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=admin password=password");
$fehler = false;

if($fehler == false){

	$insert = "INSERT INTO pillen VALUES('test','true', 'true','false','true','false','false','false','20:00:00');";
	$sql = pg_query($dbconn, $insert);

}

?>
