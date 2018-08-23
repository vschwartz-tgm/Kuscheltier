<?php

$name = $_GET['id'];
$author = $_GET['id2'];

$dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
$set = "UPDATE buch SET ausgewaehlt = true WHERE name = '$name' and author = '$author';";
pg_query($dbconn, $set);

header('location:neuesBuch.php');
?>