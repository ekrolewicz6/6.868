<?php
// include "db_connect.php";


$query = "select * from words";
// $result = $con->query($query);
// $row = $result->fetch_array(MYSQLI_NUM);
// $max = mysqli_fetch_array($query);
echo json_encode($query);

// $rand = rand(1, $max)

// mysql_query("SELECT word FROM words WHERE id = $rand;");
// $word = mysql_fetch_array($query);
	
// $response = Array("$word");
// echo json_encode($response);
// mysql_close($con);
?>