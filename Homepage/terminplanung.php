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
					<li class="nav-item active px-sm-2 pt-sm-3">
						<a class="nav-link" href="terminplanung.php"><h2>Terminplanung</h2></a>
					</li>
					<li class="nav-item px-sm-2 pt-sm-3">
						<a class="nav-link" href="buechervorlesen.php"><h2>Bücher vorlesen</h2></a>
					</li>
					<li class="nav-item pt-sm-3">
						<a class="nav-link" href="notfallsignal.php"><h2>Notfallsignal<h2></a>
					</li>
				</ul>
			</div>
		</nav>

		<div align="center">
			<p><h1>Zukünftige Termine</h1></p>
		</div>
		<div class="container scroll font">
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">Datum</th>
						<th scope="col">Uhrzeit</th>
						<th scope="col">Termin</th>
						<th scope="col">Ort</th>
						<th scope="col">Hinweis</th>
						<th scope="col"></th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td scope="row">1.5.2018</td>
						<td>12:00</td>
						<td>Zahnarzt</td>
						<td>Meidling</td>
						<td>E-Card</td>
						<td>
							<button type="button" class="btn btn-outline-dark">Löschen</button>
						</td>
					<tr>
						<td scope="row">6.5.2018</td>
						<td>13:00</td>
						<td>Familienessen</td>
						<td>Gumpendorferstraße 8</td>
						<td></td>
						<td>
							<button type="button" class="btn btn-outline-dark">Löschen</button>
						</td>
					</tr>
					<tr>
						<td scope="row">7.7.2018</td>
						<td>12:00</td>
						<td>Zahnarzt</td>
						<td>Meidling</td>
						<td>E-Card</td>
						<td>
							<button type="button" class="btn btn-outline-dark">Löschen</button>
						</td>
					</tr>
				<tbody>
			</table>
		</div>
		<div align="center">
			<button type="button" class="btn btn-outline-dark btn-lg btn-big" onclick ="window.location = 'neuerTermin.php'">Neuen Termin hinzufügen</button>
		</div>

	</body>
</html>