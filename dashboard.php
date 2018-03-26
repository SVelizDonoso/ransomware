<?php
$server = "localhost";
$username = "newuser";
$password = "password";
$dbname = "ransomware_db";
$conn = new mysqli($server, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "select * from victimas;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // listamos las filas y columnas
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["ID"]. " - Name: " . $row["IDD"]. " " . $row["PASS"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
