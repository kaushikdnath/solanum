#!/usr/bin/perl
 use CGI qw/:standard/;
    use CGI::Cookie;
print "Content-type: text/html; charset=iso-8859-1\n\n";
use CGI::Carp qw(fatalsToBrowser);

# %cookies = CGI::Cookie->fetch;

# $file=$cookies{'microsatelites_KDN'}->value;
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
print qq~
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="EN" lang="EN" dir="ltr">
<head profile="http://gmpg.org/xfn/11"><title>Primary Results</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" href="../styles/layout.css" type="text/css" />
<script type="text/javascript">
    function valid()
    {
        var fup = document.getElementById('search');
        var Text = fup.value;
		var re = /^[ATCGN]+/g;
		if(!re.exec(Text))
		{
			alert("Enter only 'A','T','C','G','N' in search field!");
			return false;
		}
    }
</script>
</head><body id="top" style="background:url(../images/backgrnd_full.png) top">
<div id="strfld" class="wrapper col1" style="position:absolute;background:url(../images/topbar.png) top left repeat-x;padding-top:0px;">
</div>
  <div id="header" class="clear" style="background:url(../images/header.png) top left;height:100px"></div>
  <div id="topbar" class="clear">
    <ul id="topnav">
      <li><a href="../index.html">Home</a></li>
      <li class="active"><a href="../QueryInput_1.html">Query</a></li>
      
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
  <div id="container" class="clear" style="font-size:17px;padding-bottom:20px;">

		<div class="wrapper" >
			<hr/>
			<div align="center">
			<form align="center" method="get" action="./Locus.cgi?" onsubmit="return valid(this)">
			<input type="text" id="search" name="motif" style="width:310px;" /><input type="hidden" name="id" value="$file"/>
			<input type="submit" value="search"/><a href="./Clustering.cgi?id=$file"><img align="right" src="../images/Cluster.png" width="200px" height="40px" /></a>
			</form></div></br>
			<hr/>
		  <div class="wrapper">
			<div id="tab" class="fl_right" >
			
				<table>
					<tr style="background-color:#007A0E;color:#ffffff;">
						<td>Motif</td><td>Count</td>
					</tr>
~;
open FILE,'<',"../Data/".$file."/TotalCount/TotalCount[2].txt";
while($i=<FILE>)
{
	$i=~ m/([ATGCN]*)\t([0-9]*)/;
		print qq~	<tr style="background-color:lavender;color:black;">
						<td><a href="./Locus.cgi?motif=$1&id=$file">$1</a></td><td>$2</td>
					</tr>~;
}
print qq~
				</table>
			</div>
			<div id="tab" class="fl_right" >
			
				<table>
					<tr style="background-color:#007A0E;color:#ffffff;">
						<td>Motifs</td><td>Count</td>
					</tr>
~;
open FILE,'<',"../Data/".$file."/TotalCount/TotalCount[3].txt";
while($i=<FILE>)
{
	$i=~ m/([ATGCN]*)\t([0-9]*)/;
		print qq~	<tr style="background-color:lavender;color:black;">
						<td><a href="./Locus.cgi?motif=$1&id=$file">$1</a></td><td>$2</td>
					</tr>~;
}
print qq~
				</table>
			</div>
			<div id="tab" class="fl_right" >
			
				<table>
					<tr style="background-color:#007A0E;color:#ffffff;">
						<td>Motifs</td><td>Count</td>
					</tr>
~;
open FILE,'<',"../Data/".$file."/TotalCount/TotalCount[4].txt";
while($i=<FILE>)
{
	$i=~ m/([ATGCN]*)\t([0-9]*)/;
		print qq~	<tr style="background-color:lavender;color:black;">
						<td><a href="./Locus.cgi?motif=$1&id=$file">$1</a></td><td>$2</td>
					</tr>~;
}
print qq~
				</table>
			</div>
			<div id="tab" class="fl_right" >
			
				<table>
					<tr style="background-color:#007A0E;color:#ffffff;">
						<td>Motifs</td><td>Count</td>
					</tr>
~;
open FILE,'<',"../Data/".$file."/TotalCount/TotalCount[5].txt";
while($i=<FILE>)
{
	$i=~ m/([ATGCN]*)\t([0-9]*)/;
		print qq~	<tr style="background-color:lavender;color:black;">
						<td><a href="./Locus.cgi?motif=$1&id=$file">$1</a></td><td>$2</td>
					</tr>~;
}
print qq~
				</table>
			</div>
			<div id="tab" class="fl_right" style="padding-left:0px;">
			
				<table>
					<tr style="background-color:#007A0E;color:#ffffff;">
						<td>Motifs</td><td>Count</td>
					</tr>
~;
open FILE,'<',"../Data/".$file."/TotalCount/TotalCount[6].txt";
while($i=<FILE>)
{
	$i=~ m/([ATGCN]*)\t([0-9]*)/;
		print qq~	<tr style="background-color:lavender;color:black;">
						<td><a href="./Locus.cgi?motif=$1&id=$file">$1</a></td><td>$2</td>
					</tr>~;
}
print qq~
				</table>
			</div>
		  </div>
		  	<div>

			<p style="color:blue;">Click on motif to go to its Locus table </p>
			</div>
			<!--</br></br>
			<p style="font-size:17pt;">Implement the Association Rule Algorithm</p>
			<hr/>
			Enter the Minumum Support(in % )
			<div id="tab">
			<form method="post" action="#">
				<table><tr><td><input style="width:200px;" type="text" name="support"></td><td><input type="submit" value="Execute Algorithm"></td></tr></table>
			</form>
			</div>-->
			
		</div>
</div>  </div>
</div>

<!-- ####################################################################################################### -->
<div class="wrapper">
  <div id="copyright" class="clear">
	<p>Copyright &copy; 2013 - All Rights Reserved - <a href="http://www.anthonys.ac.in">Bio-technology Department, St.Anthonys College | www.anthonys.ac.in</a> </p>
	<p>Developed by Kaushik Deb Nath(kdebnath56@gmail.com)</p>
  </div>
</div>
</body>
</html>~;
