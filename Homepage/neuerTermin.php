<?php
    include('functions.php');

	if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['submit'])){
	    $name = $_POST['terminName'];
        $datum = $_POST['datum'];
        $uhrzeit = $_POST['zeit'];
        $beschreibung = $_POST['desc'];
        $ort = $_POST['ort'];
        $hinweis = $_POST['hinweis'];

		$t = new Termine($name, $datum, $uhrzeit, $beschreibung, $ort, $hinweis);
		$t->add();

	}
?>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Kuscheltier Homepage</title>
		<!-- Bootstrap -->
		<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
		<link href="myCSS.css" rel="stylesheet">
		<script src="bootstrap/js/bootstrap.min.js"></script>
	</head>
	<body>
		<br />
		<h1 align="Center">Neuen Termin hinzufügen</h1>
		<br />
		<div class="container border border-dark rounded">
			<form action="" method="post">
				<div class="form-group row">
					<label for="terminName" class="col-sm-2 col-form-label" ><h3>Terminname</h3></label>
					<div class="col-sm-10">
                        <input type="text" class="form-control form-control-lg" name="terminName" id="terminName" />
					</div>
				</div>
				<div class="form-group row">
					<label for="datum" class="col-sm-2 col-form-label"><h3>Datum</h3></label>
					<div class="col-sm-10">
					  <input class="form-control form-control-lg" type="date" id="datum" name="datum"/>
					</div>
				</div>
				<div class="form-group row">
					<label for="zeit" class="col-sm-2 col-form-label"><h3>Uhrzeit</h3></label>
					<div class="col-sm-10">
					  <input class="form-control form-control-lg" type="time" id="zeit" name="zeit"/>
					</div>
				</div>
				<div class="form-group row">
					<label for="desc" class="col-sm-2 col-form-label" ><h3>Beschreibung</h3></label>
					<div class="col-sm-10">
						<input type="text" class="form-control form-control-lg" id="desc" name="desc"/>
					</div>
				</div>
				<div class="form-group row">
					<label for="ort" class="col-sm-2 col-form-label" ><h3>Ort</h3></label>
					<div class="col-sm-10">
						<input type="text" class="form-control form-control-lg" id="ort" name="ort"/>
					</div>
				</div>
				<div class="form-group row">
					<label for="hinweis" class="col-sm-2 col-form-label" ><h3>Hinweis</h3></label>
					<div class="col-sm-10">
						<input type="text" class="form-control form-control-lg" id="hinweis" name="hinweis"/>
					</div>
				</div>
				<div class="clearfix">
					<button type="button" class="cancelbtn rounded" onclick ="window.location = 'terminplanung.php'"><h5>Abbrechen</h5></button>
					<button type="submit" name="submit" id="submit" class="addbtn rounded" onclick ="window.location = 'terminplanung.php'"><h5>Hinzufügen</h5></button>
				</div>
			</form>
		</div>
	</body>
</html>