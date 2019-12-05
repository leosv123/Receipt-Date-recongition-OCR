<?php

$img=$_GET["image"];
system("/usr/anaconda/bin/python ocr_core.py ".$img." 2>&1");

$base64 = base64_encode(file_get_contents($file));
$imagedata=base64_decode($base64);
$source = imagecreatefromstring($imagedata);
$angle = 0;
$rotate = imagerotate($source, $angle, 0); // if want to rotate the image
$imageName = "hello1.jpeg";
$imageSave = imagejpeg($source,$imageName,100);



?>


