<?php

class Pillenwecker{

    private $name;
    private $montag;
    private $dienstag;
    private $mittwoch;
    private $donnerstag;
    private $freitag;
    private $samstag;
    private $sonntag;
    private $anzahl;
    private $zeit;


    function __construct($n, $m, $d, $mi, $do, $f, $s, $so, $anz, $z){
        $this->name = $n;
        $this->montag = $m;
        $this->dienstag = $d;
        $this->mittwoch = $mi;
        $this->donnerstag = $do;
        $this->freitag = $f;
        $this->samstag = $s;
        $this->sonntag = $so;
        $this->anzahl = $anz;
        $this->zeit = $z;
    }

    public function add(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $fehler = false;

        if($fehler == false){
            pg_prepare($dbconn,"addPille","INSERT INTO pillen VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10)");
            $insertValue = array($this->name,$this->montag,$this->dienstag,$this->mittwoch,$this->donnerstag,$this->freitag,$this->samstag,$this->sonntag,$this->anzahl,$this->zeit);
            pg_execute($dbconn,"addPille", $insertValue);
            //SELECT relfilenode FROM pg_class WHERE  relname = 'pg_prepared_statements'; should list all prep statements
        }
    }
    public function del(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $fehler = false;

        if($fehler == false){
            $del = "DELETE FROM pillen WHERE name = '$this->name';";
            pg_query($dbconn, $del);
        } 
    }     
}

class showPillen{
    function __construct(){}

    public function show(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $pillen = "SELECT * FROM pillen WHERE name is not null;";
        $sql = pg_query($dbconn, $pillen);
        $pillenArr = pg_fetch_all($sql);


        foreach($pillenArr as $pille){ //zwischen zeit und anzahl die Tage ausgeben
            $tage = $this->showDays($pille['name']);
            echo   "<tr>
                        <td scope='row'><h3>".$pille['name']."</h3></td>
                        <td><h3>".$pille['zeit']."</h3></td>
                        <td><h3>".$this->showDays($pille['name'])."</h3></td>
                        <td><h3>".$pille['anzahl']."</h3></td>
                        <td>
                            <button type='button' class='btn btn-outline-danger' >Löschen</button>
                        </td>
                    </tr>";
        }
    }

    public function showDays($name){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $days = "SELECT mo,di,mi,donnerstag,fr,sa,so FROM pillen WHERE name = '$name';";
        $sql = pg_query($dbconn, $days);
        $i = pg_num_fields($sql);
        $row = pg_fetch_row($sql);
        $string = "";


        for ($j = 0; $j < $i; $j++){
            $fieldname = pg_field_name($sql, $j);
            if($row[$j] == 't'){
                $string .= $fieldname.",";
            }
        }

        return $string;
    }
}

class Termine{
    private $name;
    private $datum;
    private $uhrzeit;
    private $beschreibung;
    private $ort;
    private $hinweis;

    function __construct($n, $d, $u, $b, $o, $h){
        $this->name = $n;
        $this->datum = $d;
        $this->uhrzeit = $u;
        $this->beschreibung = $b;
        $this->ort = $o;
        $this-> hinweis = $h;
    }

    public function add(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        pg_prepare($dbconn,"addTermin","INSERT INTO termine VALUES($1,$2,$3,$4,$5,$6)");
        $insertValue = array($this->name,$this->datum,$this->uhrzeit,$this->beschreibung,$this->ort,$this->hinweis);
        pg_execute($dbconn,"addTermin", $insertValue);
    }

}

class ShowTermine{
    function __construct(){}

    public function del($name){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $del = "DELETE FROM termine WHERE name = '$name';";
        pg_query($dbconn, $del);
    }

    public function show(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $termine = "SELECT * FROM termine WHERE name is not null;";
        $sql = pg_query($dbconn, $termine);
        $termineArr = pg_fetch_all($sql);

        foreach($termineArr as $termin){
            echo   "<tr>
                        <td scope='row'><h3>".$termin['name']."</h3></td>
                        <td><h3>".$termin['datum']."</h3></td>
                        <td><h3>".$termin['uhrzeit']."</h3></td>
                        <td><h3>".$termin['beschreibung']."</h3></td>
                        <td><h3>".$termin['ort']."</h3></td>
                        <td><h3>".$termin['hinweis']."</h3></td>
                        <td>
                            <button type='button' class='btn btn-outline-danger' >Löschen</button>
                        </td>
                    </tr>";
        }
    }
}

class Kuscheltiernutzer{
    function __construct(){}

    function getName(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $nname = "SELECT name FROM kuscheltiernutzer WHERE name is not null;";
        $sql = pg_query($dbconn, $nname);
        $nname = pg_fetch_row($sql);

        echo "$nname[0]";
    }

    function getAdress(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $nadress = "SELECT adresse FROM kuscheltiernutzer WHERE name is not null;";
        $sql = pg_query($dbconn, $nadress);
        $nadress = pg_fetch_row($sql);

        echo "$nadress[0]";
    }

    function getTel(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $ntel = "SELECT tel FROM kuscheltiernutzer WHERE name is not null;";
        $sql = pg_query($dbconn, $ntel);
        $ntel = pg_fetch_row($sql);

        echo "$ntel[0]";
    }

    function update(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");

        if(func_num_args() == 3){
            $del = "DELETE FROM kuscheltiernutzer WHERE name is not null;";
            pg_query($dbconn, $del);
            pg_prepare($dbconn,"updateNutzer","INSERT INTO kuscheltiernutzer VALUES($1,$2,$3)");
            $insertValue = array(func_get_arg(0), func_get_arg(1),func_get_arg(2));
            pg_execute($dbconn,"updateNutzer", $insertValue);
        }
    }

    function show(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $nname = "SELECT name FROM kuscheltiernutzer WHERE name is not null;";
        $sql = pg_query($dbconn, $nname);
        $nname = pg_fetch_row($sql);

        $nadresse = "SELECT adresse FROM kuscheltiernutzer WHERE name is not null;";
        $sql = pg_query($dbconn, $nadresse);
        $nadresse = pg_fetch_row($sql);

        $ntel = "SELECT tel FROM kuscheltiernutzer WHERE name is not null;";
        $sql = pg_query($dbconn, $ntel);
        $ntel = pg_fetch_row($sql);

            echo   "<p class=\'card-text\'><h3>Name: $nname[0]</h3></p>
			        <p class=\'card-text\'><h3>Adresse: $nadresse[0]</h3></p>
				    <p class=\'card-text\'><h3>Telefon: $ntel[0]</h3></p>";
    }
}


class Notfallkontakt{
    private $update;
    function __construct(){}

    function getName(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $nname = "SELECT name FROM notfallkontakt WHERE name is not null;";
        $sql = pg_query($dbconn, $nname);
        $nname = pg_fetch_row($sql);

        echo "$nname[0]";
    }

    function getTel(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $ntel = "SELECT tel FROM notfallkontakt WHERE name is not null;";
        $sql = pg_query($dbconn, $ntel);
        $ntel = pg_fetch_row($sql);

        echo "$ntel[0]";
    }

    function show(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $nname = "SELECT name FROM notfallkontakt WHERE name is not null;";
        $sql = pg_query($dbconn, $nname);
        $nname = pg_fetch_row($sql);

        $ntel = "SELECT tel FROM notfallkontakt WHERE name is not null;";
        $sql = pg_query($dbconn, $ntel);
        $ntel = pg_fetch_row($sql);

        echo    "<p class=\'card-text\'><h3>Name: $nname[0]</h3></p>
			    <p class=\'card-text\'><h3>Telefon: $ntel[0]</h3></p>";

    }

    function update(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");

        if(func_num_args() == 2){
            $del = "DELETE FROM notfallkontakt WHERE name is not null;";
            pg_query($dbconn, $del);
            pg_prepare($dbconn,"updateKontakt","INSERT INTO notfallkontakt VALUES($1,$2)");
            $insertValue = array(func_get_arg(0), func_get_arg(1));
            pg_execute($dbconn,"updateKontakt", $insertValue);
        }
    }

}


class Buch{

    public function getSelected(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $select = "SELECT name, genre, author, path FROM buch WHERE ausgewaehlt = true;";
        $sql = pg_query($dbconn, $select);
        $buchArr = pg_fetch_all($sql);

        foreach($buchArr as $buch){
            echo "<tr>
						<td scope='row'><h3>".$buch['name']."</h3></td>
						<td><h3>".$buch['author']."</h3></td>
						<td><h3>".$buch['genre']."</h3></td>
						<td>
							<button type='button' class='btn btn-outline-danger'>Löschen</button>
						</td>
					</tr>";
        }
    }

    public function getNotSelected(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $select = "SELECT name, genre, author, path FROM buch WHERE ausgewaehlt = false;";
        $sql = pg_query($dbconn, $select);
        $buchArr = pg_fetch_all($sql);

        foreach($buchArr as $buch){
            echo "<tr>
						<td scope='row'><h3>".$buch['name']."</h3></td>
						<td><h3>".$buch['author']."</h3></td>
						<td><h3>".$buch['genre']."</h3></td>
						<td>
						    <form action='' method='post'>
							    <input type='submit' class='btn btn-outline-success' name='add' value='Hinzufügen' />
						    </form>
						</td>
					</tr>";
        }
    }

    public function setSelected($name, $author){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $set = "UPDATE buch SET ausgewählt = true WHERE name = '$name' and author = '$author';";
        pg_query($dbconn, $set);
    }    

}

?>
