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

    public function del(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $del = "DELETE FROM termine WHERE name = '$this->name';";
        pg_query($dbconn, $del);
    }

    public function show(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $terminName = "SELECT name FROM termine WHERE name = '$this->name';";
        $sql = pg_query($dbconn, $terminName);
        $row = pg_fetch_row($sql);

        while ($row = pg_fetch_row($sql)) {
            $terminName = "SELECT name FROM termine WHERE name = '$row[0]';";
            $sqlname = pg_query($dbconn, $terminName);
            $ergname = pg_fetch_row($sqlname);

            $datum = "select datum from termine where name = '$row[0]';";
            $sqldatum = pg_query($dbconn, $datum);
            $ergdatum = pg_fetch_row($sqldatum);

            $uhrzeit = "select uhrzeit from termine where name = '$ergname';";
            $sqluhrzeit = pg_query($dbconn, $uhrzeit);
            $erguhrzeit = pg_fetch_row($sqluhrzeit);

            $desc = "select beschreibung from termine where name = '$ergname';";
            $sqldesc = pg_query($dbconn, $desc);
            $ergdesc = pg_fetch_row($sqldesc);

            $ort = "select ort from termine where name = '$ergname';";
            $sqlort = pg_query($dbconn, $ort);
            $ergort = pg_fetch_row($sqlort);

            $hinweis = "select hinweis from termine where name = '$ergname';";
            $sqlhinweis = pg_query($dbconn, $hinweis);
            $erghinweis = pg_fetch_row($sqlhinweis);

            echo   "<tr>
						<td scope='row'><h3><?php echo $ergname ?></h3></td>
						<td><h3><? php echo $ergdatum ?></h3></td>
						<td><h3><? php echo $erguhrzeit ?></h3></td>
						<td><h3><? php echo $ergdesc ?></h3></td>
						<td><h3><? php echo $ergort ?></h3></td>
						<td><h3><? php echo $erghinweis ?></h3></td>
						<td>
							<button type='button' class='btn btn-outline-danger'>Löschen</button>
						</td>
                    </tr>";
        }
    }

}


class Buch{

    public function getSelected(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $select = "SELECT name, genre, path FROM buch WHERE ausgewählt = true;";
        pg_query($dbconn, $select);
    }

    public function setSelected($name, $genre, $path){
        $dbconn = pg_connect("host=localhost port=5432 dbname=teddy user=vinc password=vinc");
        $set = "UPDATE buch SET ausgewählt = true WHERE name = '$name' AND genre = '$genre' AND path = '$path';";
        pg_query($dbconn, $set);
    }    

}

?>
