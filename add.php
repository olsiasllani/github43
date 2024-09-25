<?php

  include_once 'conection.php';
 // include_once('conection.php');
 // include 'file';
 // require 'file';


$username = $_GET['username'];
$email = $_GET['email'];
$password = $_GET['password'];



$sql = "INSERT INTO users(username,email,password)VALUES (:username, :email, :password)";

   $sqlQuery = $con->prepare($sql);

   $sqlQuery->bindParam(":username",$username);
     $sqlQuery->bindParam(":email",$email);

       $sqlQuery->bindParam(":password",$password);

       $sqlQuery->execute();

       echo "The user was added successfully";


?>