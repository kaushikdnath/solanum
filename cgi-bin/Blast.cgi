#!/usr/bin/perl
use CGI qw(:standard);
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

print qq~<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="EN" lang="EN" dir="ltr">
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
  <div id="container" style="font-size:17px;height:100px;padding-bottom:10px;">
	
		<table>
		<tr class="dark"><td >Up Stream</td><td>Locus</td><td>Down Stream</td></tr>
		<tr class="light">
			<td><input type="text" title="Up Stream" name="up" style="width:200px;" value=$inputs{"up"} /></td>
			<td><input type="text" title="The Locus" name="locus" style="width:400px;" value=$inputs{"locus"} /></td>
			<td><input type="text" title="DownStream" name="down" style="width:200px;" value=$inputs{"down"} /></td>
		</tr>
		<tr class="light"><td colspan="3"><a href="http://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome" target="_blank"><img src="../images/blast.png" width="70px" height="25px"></a></td></tr>
		</table>
  </div>
  <div id="container" style="font-size:15px;border:1px solid red;padding-bottom:10px;">
  			<p style="color:white;font-size:20px;" align="center"><b>STEPS FOR BLAST METHORD</b></p>
  			<p>1)	Copy the any of the text above click on BLAST </p>
			<p>2)	Click on BLAST</p>
			<p>3)	A new tab will be open to the NCBI Website where Actual Blast is performed</p>
			<p>4)	Paste the copied text to space provided with title "Enter accession number(s), gi(s), or FASTA sequence(s)"</p>
			<p align="center"><img src="../images/queryseqtxtarea.png" width="400px" height="100px"/></p>
			<p>5)	Select the options "others" and "Nucleotide Collection (nr/nt)" from "Choose Search Set" as shown below</p>
			<p align="center"><img src="../images/searchSet.png" width="400px" height="100px"/></p>
			<p>6)	Now scroll down and click on the button labelled BLAST</p>
			<p align="center"> <img src="../images/blastNCBI.png" width="500px" height="70px"/></p>
  		</div>
</div>



<div class="wrapper" style="padding-top:10px;">
  <div id="copyright" class="clear">
	<p>Copyright &copy; 2013 - All Rights Reserved - <a href="http://www.anthonys.ac.in">Bio-technology Department, St.Anthonys College | www.anthonys.ac.in</a> </p>
	<p>Developed by Kaushik Deb Nath(kdebnath56@gmail.com)</p>
  </div>
</div>
 





</body> </html> ~ ;

