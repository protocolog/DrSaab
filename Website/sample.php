<?php
$name=$_POST['name'];
$email=$_POST['email'];
$password=$_POST['password'];
$age=$_POST['age'];
$confirm=$_POST['password_repeat'];
if($password != $confirm){
    echo "Confirmation Password is not correct.";
}
else{
if(count($_POST)>0) {
	$conn = mysqli_connect("localhost","id13304525_users","@3UWXln2[pUr5(+|","id13304525_user_login");
	$result = mysqli_query($conn,"INSERT into users (Name,Email,Password,Age) Values('$name',$email','$password','$age')");
    if($result){
            echo "<h1 style='margin:15% 25%;box-sizing: border-box;
            padding: 12px 20px 12px 40px;
            width: 50%;
            
            background-color: #5763eb;color:white;text-decoration:none;'><center>You have login Successfully Registered<br><a href='index.html' style='color:white;text-decoration:none;'>Click Here</a></center></h1>";
        }
    else{
          echo "<h1 style='margin:15% 25%;box-sizing: border-box;
            padding: 12px 20px 12px 40px;
            width: 50%;
            
            background-color: #5763eb;color:white;text-decoration:none;'><center>Failed to add you<br><a href='signup.html' style='color:white;text-decoration:none;'>Click Here</a></center></h1>";
            }   
}
}



?>