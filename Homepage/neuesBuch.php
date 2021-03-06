<?php
    include('functions.php');

    if($_SERVER['REQUEST_METHOD'] == 'POST' and isset($_POST['submit'])){
        $name = $_POST['name'];
        $autor = $_POST['author'];
        $genre = $_POST['genre'];
        $path = $_POST[''];
        echo "$name,$genre,$autor,$path";
        $b = new Buch();
        $b->setSelected($name, $autor);
    }
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
                <li class="nav-item active px-sm-2 pt-sm-3">
                    <a class="nav-link" href="buechervorlesen.php"><h1>Bücher vorlesen</h1></a>
                </li>
                <li class="nav-item pt-sm-3">
                    <a class="nav-link" href="notfallsignal.php"><h2>Notfallsignal<h2></a>
                </li>
            </ul>
        </div>
    </nav>
		<div align="center">
			<button type="button" class="btn btn-outline-dark btn-lg" style="float: left;" onclick ="window.location = 'buechervorlesen.php'">Zurück</button>
			<p><h1>Vorhandene Bücher</h1></p>
		</div>
		<div class="container scroll font">
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col"><h3>Titel</h3></th>
						<th scope="col"><h3>Autor</h3></th>
						<th scope="col"><h3>Genre</h3></th>
						<th scope="col"></th>
					</tr>
				</thead>
				<tbody>
					<?php
						$b = new Buch();
						$b->getNotSelected();
					?>
				<tbody>
			</table>
		</div>
	</body>
</html>