<?php
$fldr=rand().rand();
if( $_FILES['file']['name'] != "" )
{	
		$folder="upload/".$_FILES['file']['name'];
		copy($_FILES['file']['tmp_name'],$folder) or 
		die( "Could not upload file!");
		rename($folder,"upload/".$fldr.".txt");
		$title='<title>Specify Motif</title>';
		$body='
	<html>
	<head>
		<meta http-equiv="refresh" content="1;url=cgi-bin/Clean.cgi?id='.$fldr.'" />
	</head>
	</html>';
	
}
echo $body;
?>