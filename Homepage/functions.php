<?php

class Pillenwecker(){

    private $name;
    private $montag;
    private $dienstag;
    private $mittwoch;
    private $donnerstag;
    private $freitag;
    private $samstag;
    private $sonntag;
    private $zeit;


    function __construct($n, $m, $d, $mi, $do, $f, $s, $so, $z){
        $this->name = n;
        $this->montag = $m;
        $this->dienstag = d;
        $this->mittwoch = mi;
        $this->donnerstag = do;
        $this->freitag = f;
        $this->samstag = s;
        $this->sonntag = so;
        $this->zeit = z;
    }

    public function add(){
        $dbconn = pg_connect("");
        $fehler = false;

        if($fehler == false){
            
            $insert = "INSERT INTO Pillen VALUES('$this->name','$this->montag','$this->dienstag','$this->mittwoch','$this->donnerstag','$this->freitag','$this->samstag','$this->sonntag','$this->zeit');";
            $sql = pg_query($dbconn, $insert);
            
            
            
        
        }
    }
    public function add(){
        $dbconn = pg_connect("");
        $fehler = false;

        if($fehler == false){
            $del = "DELETE FROM Pillen WHERE name = '$this->name';";
            $sql = pg_query($dbconn, $del); 
        } 
    }     
}


?>
