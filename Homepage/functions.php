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
    private $zeit;


    function __construct($n, $m, $d, $mi, $donnerstag, $f, $s, $so, $z){
        $this->name = $n;
        $this->montag = $m;
        $this->dienstag = $d;
        $this->mittwoch = $mi;
        $this->donnerstag = $donnerstag;
        $this->freitag = $f;
        $this->samstag = $s;
        $this->sonntag = $so;
        $this->zeit = $z;
    }

    public function add(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $fehler = false;

        if($fehler == false){
            
            $insert = "INSERT INTO pillen VALUES('$this->name','$this->montag','$this->dienstag','$this->mittwoch','$this->donnerstag','$this->freitag','$this->samstag','$this->sonntag','$this->zeit');";
            pg_query($dbconn, $insert);
            
            
            
        
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
        pg_prepare($dbconn,"myquery","INSERT INTO termine VALUES($1,$2,$3,$4,$5,$6)");
        $insertValue = array($this->name,$this->datum,$this->uhrzeit,$this->beschreibung,$this->ort,$this->hinweis);
        pg_execute($dbconn,"myquery", $insertValue);
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
            $update = "UPDATE notfallkontakt SET name = '".func_get_arg(0)."' and tel = '".func_get_arg(1)."';";
        }
        elseif (strpbrk(func_get_arg(0), '1234567890') !== FALSE){
            $update = "UPDATE notfallkontakt SET tel = '".func_get_arg(0)."';";
        }else{
            $update = "UPDATE notfallkontakt SET name = '".func_get_arg(0)."';";
        }

        pg_query($dbconn, $update);
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
