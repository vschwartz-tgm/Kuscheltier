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
		<div align="center">
			<button type="button" class="btn btn-outline-dark btn-lg" style="float: left;" onclick ="window.location = 'buechervorlesen.php'">Zurück</button>
			<p><h1>Vorhandene Bücher</h1></p>
		</div>
		<div class="container scroll font">
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">Titel</th>
						<th scope="col">Genre</th>
						<th scope="col">Dauer</th>
						<th scope="col"></th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td scope="row">Herr der RInge</td>
						<td>Fantasy</td>
						<td>3:00:00</td>
						<td>
							<button type="button" class="btn btn-outline-success">Hinzufügen</button>
						</td>
					</tr>
					<tr>
						<td scope="row">Herr der RInge</td>
						<td>Fantasy</td>
						<td>3:00:00</td>
						<td>
							<button type="button" class="btn btn-outline-success">Hinzufügen</button>
						</td>
					</tr>
					<tr>
						<td scope="row">Herr der RInge</td>
						<td>Fantasy</td>
						<td>3:00:00</td>
						<td>
							<button type="button" class="btn btn-outline-success">Hinzufügen</button>
						</td>
					</tr>
					<tr>
						<td scope="row">Herr der RInge</td>
						<td>Fantasy</td>
						<td>3:00:00</td>
						<td>
							<button type="button" class="btn btn-outline-success">Hinzufügen</button>
						</td>
					</tr>
					<tr>
						<td scope="row">Herr der RInge</td>
						<td>Fantasy</td>
						<td>3:00:00</td>
						<td>
							<button type="button" class="btn btn-outline-success">Hinzufügen</button>
						</td>
					</tr>
				<tbody>
			</table>
		</div>
	</body>
</html>