<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Administrator Page</title>
  <style>
    td{
      border: 1px solid;
      text-align: center;
      padding: 0.5rem;
    }
    </style>
</head>

<body>
  <h1>Administrator Page</h1>

  <!-- PHP to display admin information -->

  <?php
  session_start();
  //Check if the sesion variables are correct
  if(isset($_SESSION["loggedinusr"]) && $_SESSION["usertype"] === 'admin'){
    //check if the button has been pressed
    if(isset($_POST["button"])){
      header("Location: logout_page.php");
    }
    //if the button isn't pressed, create, populate the table
    else{
      $_SESSION['adminloggedin'] = 'TRUE';
      $_SESSION['userloggedin'] = 'FALSE';
      require_once 'login.php';
      $connection = new mysqli($hn, $un, $pw, $db);
      $user = $_SESSION["loggedinusr"];
      if ($connection->connect_error)
        die($connection->connect_error);
      echo"<p>Welcome back, $user!</p>";
      echo"<p>Here is the list of all orders...</p>";

      $result = $connection->query("SELECT * FROM lab4_orders");
      if(!$result)
        die($connection->erorr);

      echo "<table>";
      echo "<tr>";
      echo "<th>Order ID</th>";
      echo "<th>Order Total</th>";
      echo "<th>Quantity</th>";
      echo "<th>Shipping</th>";
      echo "<th>Username</th>";
      echo "</tr>";

      while($row = mysqli_fetch_array($result)){
        $shipping = $row["shipping"];
        $quantity = $row["quantity"];
        $orderTotal = $row["orderTotal"];
        $orderID = $row["orderID"];
        $db_user = $row["username"];
        echo "<tr>";
        echo "<td>$orderID</td>";
        echo "<td>$orderTotal</td>";
        echo "<td>$quantity</td>";
        echo "<td>$shipping</td>";
        echo "<td>$db_user</td>";
        echo "</tr>";
        }

      echo"</table>";

        echo"<form action='admin_page.php' method='post'>
        <button type='submit' name='button'>Logout</button>
        </form>";
    }

  }
  //If someone tries to access admin_page without being logged in
  else{
    $_SESSION['adminloggedin'] = 'FALSE';
    echo"<h1>You aren't an Admin... no data for you.</h1>";
    echo"<form action='admin_page.php' method='post'>";
    echo"<button type='submit' name='button2'>Return to Login</button>";
    echo"</form>";
    if(isset($_POST['button2'])){
      header("Location: login_page.php");
    }
  }

  ?>

</body>

</html>
