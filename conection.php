<?php


  $server = "localhost";
  $username = "root";
  $password = "";
  $dnamwe = "dtabaza10a";

  try{
  	$con = new PDO("mysql:host=$server;dbname=$dbname", $username,$password);
  }catch (Exception $e){
  	echo "Something went wrong!Server not conected!".$e;
  }







?>