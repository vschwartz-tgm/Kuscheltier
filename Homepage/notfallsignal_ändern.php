<?php
	// ToDo: Werte aus DB lesen und in die Tabelle schreiben (PHP im Text)
?>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Kuscheltier Homepage</title>
		<!-- Bootstrap -->
		<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
		<script src="bootstrap/js/bootstrap.min.js"></script>
		<link href="myCSS.css" rel="stylesheet">
	</head>
	<body>
		<nav class="navbar navbar-expand-sm navbar-light bg-light border border-dark rounded">
			<!-- Brand -->
			<a class="navbar-brand" href="index.html"><img src="Assets/home.png" class="nav-img"></a>

			<!-- Links -->
			<div class="collapse navbar-collapse" id="nav-content">   
				<ul class="nav navbar-nav">
					<li class="nav-item px-sm-2 pt-sm-3">
						<a class="nav-link" href="index.html"><h2>Startseite</h2></a>
					</li>
					<li class="nav-item px-sm-2 pt-sm-3">
						<a class="nav-link" href="pillenwecker.php"><h2>Pillenwecker</h2></a>
					</li>
					<li class="nav-item px-sm-2 pt-sm-3">
						<a class="nav-link" href="terminplanung.php"><h2>Terminplanung</h2></a>
					</li>
					<li class="nav-item px-sm-2 pt-sm-3">
						<a class="nav-link" href="buechervorlesen.php"><h2>Bücher vorlesen</h2></a>
					</li>
					<li class="nav-item active pt-sm-3">
						<a class="nav-link" href="notfallsignal.php"><h2>Notfallsignal<h2></a>
					</li>
				</ul>
			</div>
		</nav>
		<div class="container">
			<div class="row">
				<div class="col-sm">
					<div class="card">
						<div class="card-header">
							<h4>Daten des Kuscheltiernutzers</h4>
						</div>
						<div class="card-body">
							<p class="card-text">Name: <input type="text" id="nameNutzer" name="nameNutzer" value="Max Mustermann"/></p>
							<p class="card-text">Adresse: <input type="text" id="adresseNutzer" name="adresseNutzer" value="Musterstraße 88"/></p>
							<p class="card-text">Telefon: <input type="number" id="nrNutzer" name="nrNutzer" value="06501234567"/></p>
						</div>
					</div>
				</div>
				<div class="col-sm">
					<div class="card">
						<div class="card-header">
							<h4>Daten des Notfallkontakts</h4>
						</div>
						<div class="card-body">
							<p class="card-text">Name: <input type="text" id="nameKontakt" name="nameKontakt" value="Leo Musterfrau"/></p>
							<p class="card-text">Telefon: <input type="number" id="nrKontakt" name="nrKontakt" value="06501223267" /></p>
							<br />
							<p class="card-text"></p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div align="center">
			<button type="button" class="btn btn-outline-success btn-lg btn-big" onclick ="window.location = 'notfallsignal.php'">Änderungen speichern</button>
		</div>
	</body>
</html>