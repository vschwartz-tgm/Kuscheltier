<?php
	include("functions.php");

	$nk = new Notfallkontakt();
	$kn = new Kuscheltiernutzer();


    if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['submit'])){
        $kname = $_POST['nameKontakt'];
        $ktel = $_POST['nrKontakt'];
        $nk->update($kname, $ktel);

        $nname = $_POST['nameNutzer'];
        $nadresse = $_POST['adresseNutzer'];
        $ntel = $_POST['nrNutzer'];
        $kn->update($nname, $nadresse, $ntel);
    }
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
		<div class="container">
            <button type="button" class="btn btn-outline-dark btn-lg" style="float: left;" onclick ="window.location = 'notfallsignal.php'">Zurück</button>
            <form action="" method="post">
                <div class="row">
                    <div class="col-sm-6">
                        <div class="card">
                            <div class="card-header">
                                <h4>Daten des Kuscheltiernutzers</h4>
                            </div>
                            <div class="card-body">
                                <p class="card-text">Name: <input type="text" id="nameNutzer" name="nameNutzer" value="<?php $kn->getName()?>"/></p>
                                <p class="card-text">Adresse: <input type="text" id="adresseNutzer" name="adresseNutzer" value="<?php $kn->getAdress()?>"/></p>
                                <p class="card-text">Telefon: <input type="text" id="nrNutzer" name="nrNutzer" value="<?php $kn->getTel()?>"/></p>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="card">
                            <div class="card-header">
                                <h4>Daten des Notfallkontaktes</h4>
                            </div>
                            <div class="card-body">
                                <p class="card-text">Name: <input type="text" id="nameKontakt" name="nameKontakt" value="<?php $nk->getName()?>"/></p>
                                <p class="card-text">Telefon: <input type="text" id="nrKontakt" name="nrKontakt" value="<?php $nk->getTel()?>" /></p>
                                <br />
                                <p class="card-text"></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div align="center">
                <button type="submit" class="btn btn-outline-success btn-lg btn-big" name="submit">Änderungen speichern</button>
            </div>
        </form>
	</body>
</html>