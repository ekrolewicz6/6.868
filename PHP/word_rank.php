<?php
include "db_connect.php";

$word = $_POST['word'];
$rank = $_POST['rank'];

$query = mysql_query("SELECT user_password FROM `users` WHERE user_name='$kerberos';");
$oldrank = mysql_fetch_array($query);

$rank = $rank + $oldrank

mysql_query("UPDATE words SET rank=$rank WHERE word='$word';");
	
$response = Array("TRUE");
echo json_encode($response);
mysql_close($con);
?>