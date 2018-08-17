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
			<p><h1>Code eingeben</h1></p>
		</div>
		<br />
		<div class="container">
			<div class="input-group input-group-lg">
	  			<div class="input-group-prepend">
	    			<p class="input-group-text" id="inputGroup-sizing-lg">Code</p>
	  			</div>
	  			<input type="text" class="form-control" id="codeInput" name="codeInput" aria-label="Code" aria-describedby="inputGroup-sizing-sm">
			</div>
			<br />
			<br />
			<div align="center">
				<button type="button" class="btn btn-outline-danger btn-lg btn-big"  style="float: left;" onclick ="window.location = 'notfallsignal.php'">Zurück</button>
				<button type="button" class="btn btn-outline-success btn-lg btn-big" style="" onclick ="window.location = 'notfallsignal_ändern.php'">Einloggen</button>
			</div>
		</div>
	</body>
</html>