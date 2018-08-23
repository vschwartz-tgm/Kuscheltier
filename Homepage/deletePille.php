<?php

$id = $_GET['id'];

$dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
$del = "DELETE FROM pillen WHERE name = '$id';";
pg_query($dbconn, $del);

header('location:pillenwecker.php');
?>