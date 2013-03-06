<?php
include "db_connect.php";


$query = mysql_query("SELECT count(word) FROM words;");
$max = mysql_fetch_array($query);

$rand = rand(1, $max)

mysql_query("SELECT word FROM words WHERE id = $rand;");
$word = mysql_fetch_array($query);
	
$response = Array("$word");
echo json_encode($response);
mysql_close($con);
?>