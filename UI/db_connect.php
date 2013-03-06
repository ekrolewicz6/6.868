<?php
/* This code will make a connection with database */
$db_host = "sql.mit.edu";
// Host name
$db_username = "tchwella";
// Mysql username
$db_password = "12345678";
// Mysql password
$db_name = "tchwella+6868";
// Database name
$con = new mysqli("$db_host", "$db_username", "$db_password", "$db_name");
// $con = mysqli_connect("$db_host", "$db_username", "$db_password", "$db_name");
// $con = mysql_connect("$db_host", "$db_username", "$db_password");
// if ($con->connect_errno)
//   {
// 	die($con->connect_errno);
//   }
$db = $con->select_db("$db_name");
?>