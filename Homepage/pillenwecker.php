<?php
	// ToDo: Werte aus DB lesen und in die Tabelle schreiben (PHP im Text)
	include ("functions.php");


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
		<nav class="navbar navbar-expand-sm navbar-light border border-primary rounded" style="background-color: #66CCFF;">
			<!-- Brand -->
			<!--<a class="navbar-brand" href="index.html"><img src="Assets/home.png" class="nav-img"></a>-->
			<!-- Links -->
			<div class="collapse navbar-collapse" id="nav-content">   
				<ul class="nav navbar-nav">
					<li class="nav-item px-sm-2 pt-sm-3">
						<a class="nav-link" href="index.php" style="margin-left: 36px;"><h2>Startseite</h2></a>
					</li>
					<li class="nav-item active px-sm-2 pt-sm-3">
						<a class="nav-link" href="pillenwecker.php"><h1>Pillenwecker</h1></a>
					</li>
					<li class="nav-item px-sm-2 pt-sm-3">
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
			<p><h1>Aktuelle Pillenwecker</h1></p>
		</div>
		<div class="container scroll">
			<table class="table table-hover font">
				<thead>
					<tr>
						<th scope="col"><h3>Pillenname</h3></th>
						<th scope="col"><h3>Einnahmezeit</h3></th>
						<th scope="col"><h3>Tage</h3></th>
						<th scope="col"></th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<th scope="row"><h3>Pille 1</h3></th>
						<td><h3>08:00</h3></td>
						<td><h3>MO,DI,MI,DO,FR,SA,SO</h3></td>
						<td>
							<button type="button" class="btn btn-outline-danger">Löschen</button>
						</td>
					<tr>
						<th scope="row"><h3>Pille 2</h3></th>
						<td><h3>10:00</h3></td>
						<td><h3>MO,DO</h3></td>
						<td>
							<button type="button" class="btn btn-outline-danger">Löschen</button>
						</td>
					</tr>
					<tr>
						<th scope="row"><h3>Pille 3</h3></th>
						<td><h3>20:00</h3></td>
						<td><h3>SA</h3></td>
						<td>
							<button type="button" class="btn btn-outline-danger">Löschen</button>
						</td>
					</tr>
				<tbody>
			</table>
		</div>
		<div align="center">
			<a href="neuerPillenwecker.php">
				<button type="button"  class="btn btn-outline-dark btn-lg btn-big">Neuer Pillenwecker</button>
			</a>
		</div>
	</body>
</html>