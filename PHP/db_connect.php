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
//$coni = new MySQLI("$db_host", "$db_username", "$db_password", "$db_name");
$con = mysql_connect("$db_host", "$db_username", "$db_password");
if (!$con)
  {
	die("cannot select DB");
  }
$db = mysql_select_db("$db_name");
?>