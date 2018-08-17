<?php
	include("functions.php");
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
						<a class="nav-link" href="notfallsignal.php"><h1>Notfallsignal<h1></a>
					</li>
				</ul>
			</div>
		</nav>

		<div align="center">
			<p><h1>Aktuelle Notfalldaten</h1></p>
		</div>
		<div class="container font">
			<div class="row">
				<div class="col-sm">
					<div class="card">
						<div class="card-header">
							<h4>Daten des Kuscheltiernutzers</h4>
						</div>
						<div class="card-body">
                            <?php
                            $s = new Kuscheltiernutzer();
                            $s->show();
                            ?>
						</div>
					</div>
				</div>
				<div class="col-sm">
					<div class="card">
						<div class="card-header">
							<h4>Daten des Notfallkontaktes</h4>
						</div>
						<div class="card-body">
                            <?php
                            $s = new Notfallkontakt();
                            $s->show();
                            ?>
							<br />
							<p class="card-text"></p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div align="center">
			<button type="button" class="btn btn-outline-dark btn-lg btn-big" onclick ="window.location = 'notfallsignal_login.php'">Daten ändern</button>
		</div>
	</body>
</html>