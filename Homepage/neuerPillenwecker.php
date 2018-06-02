<?php
	include("functions.php");

	if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['submit'])){
		// ToDo: Werte rauslesen & in DB speichern
		$p = new Pillenwecker($name,$m,$d,$mi,$do,$fr,$sa,$so, $zeit);
		$p->add();
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
		<h1 align="Center">Neuen Pillenwecker hinzufügen</h1>
		<br />
		<div class="container border border-dark rounded">
			<form action="" method="post">
				<div class="form-group row">
					<label for="pillenName" class="col-sm-2 col-form-label" ><h3>Pillenname</h3></label>
					<div class="col-sm-10">
						  <input type="text" class="form-control form-control-lg" id="pillenName" />
					</div>
				</div>
				<div class="form-group row">
					<div class="col-form-label col-sm-2"><h3>Tage</h3></div>
					<div class="col-sm-10">
						<div class="form-check" style="padding-top: 20px;">
							<input class="form-check-input" type="checkbox" value="" id="checkBox1" />
							<label class="form-check-label" for="checkBox1"><h5>Montag</h5></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="" id="checkBox2" />
							<label class="form-check-label" for="checkBox2"><h5>Dienstag</h5></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="" id="checkBox3" />
							<label class="form-check-label" for="checkBox3"><h5>Mittwoch</h5></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="" id="checkBox4" />
							<label class="form-check-label" for="checkBox4"><h5>Donnerstag</h5></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="" id="checkBox5"/>
							<label class="form-check-label" for="checkBox5"><h5>Freitag</h5></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="" id="checkBox6"/>
							<label class="form-check-label" for="checkBox6"><h5>Samstag</h5></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="" id="checkBox7"/>
							<label class="form-check-label" for="checkBox7"><h5>Sonntag</h5></label>
						</div>
					</div>
				</div>
				<br />
				<div class="form-group row">
					<label for="zeit" class="col-sm-2 col-form-label"><h3>Uhrzeit</h3></label>
					<div class="col-sm-10">
					  <input class="form-control form-control-lg" type="time" id="zeit" name="zeit"/>
					</div>
				</div>
				<div class="clearfix">
					<button type="button" class="cancelbtn rounded" onclick ="window.location = 'pillenwecker.php'"><h5>Abbrechen</h5></button>
					<button type="submit" name="submit" id="submit" class="addbtn rounded"><h5>Hinzufügen</h5></button>
				</div>
			</form>
		</div>
	</body>
</html>
