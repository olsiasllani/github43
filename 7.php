<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title></title>
</head>
<body>

  <?php
$host = "localhost";
$user = "root";
$password = "";
$db = "databaza10A";
/*
 SQL - Structured Query Language
   PDO - Php Data Object
Create Databaze

try{

  $con = new PDO("mysql:host=$host;", $user, $password);

     $sql = "CREATE DATABASE databaza10A";  
     
     $con->exec($sql);
     echo "Connected to the server!";



} catch (Exception $e){
  echo "Eshte Paraqit Error!".$e;
}

  
*/

// Create Table using PDO


/*
try{
  $con = new PDO("mysql:host=$host; dbname=$db", $user, $password);
$sql = "CREATE table users(id int NOT NULL AUTO_INCREMENT, name VARCHAR(20), surname VARCHAR(20),  email VARCHAR(30), password VARCHAR(255), PRIMARY KEY(id))";
  
  $con->exec($sql);

  echo "Tabela u krijua me sukses!";
} catch (Exception$e){
  echo $e;
}

*/

// Popullimi i tabelses (Vendosja e te dhanave ne tabele)

 try{

  $con= new PDO("mysql:host=$host; dbname=$db", $user, $password);

   $sql "INSERT INTO users(name,surname,email,password)value("Filan","Fisteku","filanfisteku@gmail.com","12345678")";

   $con->exec($sql);

   echo "Te dhenat u shtuan me sukses";


 }catch(Exeption $e){
  echo $e->getMessage();
 }

  ?>

</body>
</html>