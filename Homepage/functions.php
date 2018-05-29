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
        $dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier user=christoph password=admin");
        $fehler = false;

        if($fehler == false){
            
            $insert = "INSERT INTO pillen VALUES('$this->name','$this->montag','$this->dienstag','$this->mittwoch','$this->donnerstag','$this->freitag','$this->samstag','$this->sonntag','$this->zeit');";
            $sql = pg_query($dbconn, $insert);
            
            
            
        
        }
    }
    public function del(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier user=christoph password=admin");
        $fehler = false;

        if($fehler == false){
            $del = "DELETE FROM pillen WHERE name = '$this->name';";
            $sql = pg_query($dbconn, $del); 
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
        $this->urzeit = $u;
        $this->beschreibung = $b;
        $this->ort = $o;
        $this-> hinweis = $h;
    }

    public function add(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier user=christoph password=admin");
        $insert = "INSERT INTO termine VALUES('$this->datum','$this->uhrzeit','$this->beschreibung','$this->ort','$this->hinweis');";
        $sql = pg_query($dbconn, $insert);
    }

    public function del(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier user=christoph password=admin");
        $del = "DELETE FROM termine WHERE name = '$this->name';";
        $sql = pg_query($dbconn, $del);
    }
}


class Buch{

    public function getSelected(){
        $dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier user=christoph password=admin");
        $select = "SELECT name, genre, path FROM buch WHERE ausgewählt = true;";
        $sql = pg_query($dbconn, $select);
    }

    public function setSelected($name, $genre, $path){
        $dbconn = pg_connect("host=localhost port=5432 dbname=kuscheltier user=christoph password=admin");
        $set = "UPDATE buch SET ausgewählt = true WHERE name = '$name' AND genre = '$genre' AND path = '$path';";
        $sql = pg_query($dbconn, $set);
    }    

}

?>
