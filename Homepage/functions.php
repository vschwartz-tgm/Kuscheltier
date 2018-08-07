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
    function __construct(){

    }

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
                            <button type='button' class='btn btn-outline-danger' onclick='".$this->del($termin['name'])."'>Löschen</button>
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
