<?php
	include('functions.php');

	if($_SERVER['REQUEST_METHOD'] == 'POST' and isset($_POST['submit'])){
        if (isset($_POST['Montag']) and $_POST['Montag'] == '1'){
            // Montag angeklickt
            $m = 't';
        }else{
            $m = 'f';
        }
        if (isset($_POST['Dienstag']) and $_POST['Dienstag'] == '1'){
            // Dienstag angeklickt
            $d = 't';
        }else{
            $d = 'f';
        }
        if (isset($_POST['Mittwoch']) and $_POST['Mittwoch'] == '1'){
            // Mittwoch angeklickt
            $mi = 't';
        }else{
            $mi = 'f';
        }
        if (isset($_POST['Donnerstag']) and $_POST['Donnerstag'] == '1'){
            // Donnerstag angeklickt
            $do = 't';
        }else{
            $do = 'f';
        }
        if (isset($_POST['Freitag']) and $_POST['Freitag'] == '1'){
            // Freitag angeklickt
            $fr = 't';
        }else{
            $fr = 'f';
        }
        if (isset($_POST['Samstag']) and $_POST['Samstag'] == '1'){
            // Samstag angeklickt
            $sa = 't';
        }else{
            $sa = 'f';
        }
        if (isset($_POST['Sonntag']) and $_POST['Sonntag'] == '1'){
            // Sonntag angeklickt
            $so = 't';
        }else{
            $so = 'f';
        }

	    $name = $_POST['pillenName'];
        $anz = $_POST['anzahl'];
	    $zeit = $_POST['zeit'];

		$p = new Pillenwecker($name,$m,$d,$mi,$do,$fr,$sa,$so, $anz, $zeit);
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
						  <input type="text" class="form-control form-control-lg" name="pillenName" id="pillenName" required/>
					</div>
				</div>
				<div class="form-group row">
					<div class="col-form-label col-sm-2"><h3>Tage</h3></div>
					<div class="col-sm-10">
						<div class="form-check" style="padding-top: 20px;">
							<input class="form-check-input" type="checkbox" value="1" name="Montag" id="checkBox1" />
							<label class="form-check-label" for="checkBox1"><h4>Montag</h4></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="1" name="Dienstag" id="checkBox2" />
							<label class="form-check-label" for="checkBox2"><h4>Dienstag</h4></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="1" name="Mittwoch" id="checkBox3" />
							<label class="form-check-label" for="checkBox3"><h4>Mittwoch</h4></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="1" name="Donnerstag" id="checkBox4" />
							<label class="form-check-label" for="checkBox4"><h4>Donnerstag</h4></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="1" name="Freitag" id="checkBox5"/>
							<label class="form-check-label" for="checkBox5"><h4>Freitag</h4></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="1" name="Samstag" id="checkBox6"/>
							<label class="form-check-label" for="checkBox6"><h4>Samstag</h4></label>
						</div>
						<div class="form-check">
							<input class="form-check-input" type="checkbox" value="1" name="Sonntag" id="checkBox7"/>
							<label class="form-check-label" for="checkBox7"><h4>Sonntag</h4></label>
						</div>
					</div>
				</div>
				<br />
                <div class="form-group row">
                    <label for="anzahl" class="col-sm-2 col-form-label"><h3>Anzahl</h3></label>
                    <div class="col-sm-10">
                        <input class="form-control form-control-lg" type="number" id="anzahl" name="anzahl" required/>
                    </div>
                </div>
                <br />
				<div class="form-group row">
					<label for="zeit" class="col-sm-2 col-form-label"><h3>Uhrzeit</h3></label>
					<div class="col-sm-10">
					  <input class="form-control form-control-lg" type="time" id="zeit" name="zeit" required/>
					</div>
				</div>
				<div class="clearfix">
					<button type="button" class="cancelbtn rounded" onclick ="window.location = 'pillenwecker.php'"><h5>Abbrechen</h5></button>
					<button type="submit" name="submit" id="submit" class="addbtn rounded" onclick ="window.location = 'pillenwecker.php'"><h5>Hinzufügen</h5></button>
				</div>
			</form>
		</div>
	</body>
</html>
