#!/usr/bin/perl
print "Content-type: text/html; charset=iso-8859-1\n\n";

if ( $ENV{'REQUEST_METHOD'} eq "GET"){	
	$form=$ENV{'QUERY_STRING'};
}
foreach $pair (split('&', $form)) {
        if ($pair =~ /(.*)=(.*)/) 
	{  # found key=value;
		($key,$value) = ($1,$2);     # get key, value.
		$inputs{$key} = $value;   
    }
}
$file=$inputs{'id'};

open $src,'<',"../Data/".$file."/Cleaned/Records.txt";
open $tar1,'>',"../Data/".$file."/Cluster/c1.txt";
open $tar2,'>',"../Data/".$file."/Cluster/c2.txt";
#open $tar3,'>',"./Cluster/c3.txt";
@arr=<$src>;
close($src);
foreach(@arr) {
	$a=()=$_=~ m/A/g;
	$t=()=$_=~ m/T/g;
	$c=()=$_=~ m/C/g;
	$g=()=$_=~ m/G/g;
	$n=()=$_=~ m/N/g;
	(!$n)?$d=5:$d=4;
	$sum=($a+$t+$c+$g+$n)/$d;
	push @records,$sum;
#	print $tar3 @records;
}
$err=0;$m=80;$n=140;
#do
for($i=0;$i<15;$i++)
{	$prevErr=$err;
	$prevavg=$avg;
	$err=0;
	foreach(@records)
	{
		$r=($m+$n)/2;
		if($_ < $r)
		{
			push @c1,$_;
		}
		else{
			push @c2,$_;	
		}
		$sum1=0;$sum2=0;$id1=1;$id2=1;
		foreach(@c1){$sum1+=$_;$id1++;$err+=($_ - $m)**2;}
		foreach(@c2){$sum2+=$_;$id2++;$err+=($_ - $n)**2;}
		$m=$sum1/$id1;
		$n=$sum2/$id2;
	}
	$avg=$prevavg-($err-$prevErr);
}#while(($err-$prevErr));
open IDS,'<',"../Data/".$file."/Cleaned/Ids.txt";
@id=<IDS>;
close(IDS);
foreach(@c1)
{	
	$i=0;
	$val=$_;
	foreach(@records)
	{
		if($_=~m/$val/)
		{
			$_=~s/$val//;
			print $tar1 ">$id[$i]$arr[$i]";
		}
		$i++;
	}

}
foreach(@c2)
{	
	$i=0;
	$val=$_;
	foreach(@records)
	{
		if($_=~m/$val/)
		{
			$_=~s/$val//;
			print $tar2 ">$id[$i]$arr[$i]";
		}
		$i++;
	}

}
close($tar1);
close($tar2);

print qq~
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="EN" lang="EN" dir="ltr">
<head profile="http://gmpg.org/xfn/11">
<title>Mining for DNA motifs in Tomato | Query</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" href="../styles/layout.css" type="text/css" />
</head>
<body id="top" style="background:url(../images/backgrnd_full.png) top">
<div id="strfld" class="wrapper col1" style="position:absolute;background:url(../images/topbar.png) top left repeat-x;padding-top:0px;">
</div> 
  <div id="header" class="clear" style="background:url(../images/header.png) top left;height:100px"></div>
  <div id="topbar" class="clear">
    <ul id="topnav">
      <li ><a href="../index.html">Home</a></li>
      <li><a href="../QueryInput_1.html">Query</a></li>
      <li><a href="../Contact.html">Contact Us</a></li>
    </ul>
  </div>
</div>
<script src="../scripts/starfield.js"></script>
	<script>
		var container = document.getElementById('strfld');
		var starfield = new Starfield();
		starfield.initialise(container);
		starfield.start();		
	</script>
<!-- ####################################################################################################### -->
<div class="wrapper ">
 	<div id="container" style="font-size:17px;padding-bottom:10px;">
		<p>Right click & click "Save link As" on the below links to download the Clusters</p>
		</br>
		<p align="center"><a href="../Data/$file/Cluster/c1.txt">Cluster 1</a></p>
		<p align="center"><a href="../Data/$file/Cluster/c2.txt">Cluster 2</a></p>
	</div>
</div>


<div class="wrapper" >
  <div id="copyright">
	<p>Copyright &copy; 2013 - All Rights Reserved - <a href="http://www.anthonys.ac.in">Bio-technology Department, St.Anthonys College | www.anthonys.ac.in</a> </p>
	<p>Developed by Kaushik Deb Nath(kdebnath56@gmail.com)</p>
  </div>
</div>
 





</body> </html> 
~;