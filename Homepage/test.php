<?php
$dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier       user=christoph password=admin");
$del = "DELETE FROM termine WHERE name = 'test';";
$sql = pg_query($dbconn, $del);
?>
