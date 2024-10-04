<?php

 incude_once 'config.php';


 $id = $_GET['id'];

 $sql = "SELECT * FROM users WHERE id=:id";

$prep = $con ->prepare($sql);

$prep->bindParam(':id , $id');
$prep->execute();

$data = $prep->fetch();

?>






<!DOCTYPE html>
<html>
<head>
	<title>Update Form</title>
</head>
<body>
	<form>

	<label for="username">Username:</label><br>
		<input type="text" name="username" id="username" placeholder="Username" value="<?php echo $data['username'] ?>"> <br><br>

		<label for="email">Email:</label><br>
		<input type="email" name="email" id="email" placeholder="filan@gmail.com" value="<?php echo $data['email'] ?>"><br><br>

		<label for="password">Password:</label><br>
		<input type="password" name="password" id="password" placeholder="Password"><br><br>

		<input type="submit" name="submit">

	</form>

</body>
</html>