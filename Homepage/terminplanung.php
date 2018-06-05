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
		<div class="container scroll">
			<table class="table table-hover font">
				<thead>
					<tr>
						<th scope="col"><h3>Datum</h3></th>
						<th scope="col"><h3>Uhrzeit</h3></th>
						<th scope="col"><h3>Termin</h3></th>
						<th scope="col"><h3>Ort</h3></th>
						<th scope="col"><h3>Hinweis</h3></th>
						<th scope="col"></th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td scope="row"><h3>1.5.2018</h3></td>
						<td><h3>12:00</h3></td>
						<td><h3>Zahnarzt</h3></td>
						<td><h3>Meidling</h3></td>
						<td><h3>E-Card</h3></td>
						<td>
							<button type="button" class="btn btn-outline-danger">Löschen</button>
						</td>
					<tr>
						<td scope="row"><h3>6.5.2018</h3></td>
						<td><h3>13:00</h3></td>
						<td><h3>Familienessen</h3></td>
						<td><h3>Gumpendorferstraße 8</h3></td>
						<td></td>
						<td>
							<button type="button" class="btn btn-outline-danger">Löschen</button>
						</td>
					</tr>
					<tr>
						<td scope="row"><h3>7.7.2018</h3></td>
						<td><h3>12:00</h3></td>
						<td><h3>Zahnarzt</h3></td>
						<td><h3>Meidling</h3></td>
						<td><h3>E-Card</h3></td>
						<td>
							<button type="button" class="btn btn-outline-danger">Löschen</button>
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