<?php
$dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=test password=admin");
$insert = "INSERT INTO pillen VALUES('test','true', 'true','false','true','false','false','false','20:00:00');";
$sql = pg_query($dbconn, $insert);

?>
