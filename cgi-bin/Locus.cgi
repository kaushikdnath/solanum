#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);use CGI qw(:standard);
use CGI qw/:standard/;
use CGI::Cookie;
print "Content-type: text/html; charset=iso-8859-1\n\n";

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

$motif=$inputs{'motif'};;
open ID,"<","../Data/".$file."/Cleaned/Ids.txt";
open RECORD,"<","../Data/".$file."/Cleaned/Records.txt";
@Ids=<ID>;     
@recods=<RECORD>;
close(ID);
close(RECORD);
$i=0;
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
  <div id="container" style="font-size:17px;height:460px;overflow-x:hidden;">
	
		<table style="overflow-y:hidden;">
			<tr class="dark" style="font-size:15pt">
				<td>Record ID</td>
				<td style="font-size:16px;">No. of Repeats</td>
				<td width="120px">Locus</td>
				<td>Upstream(G+C)</td>
				<td>DownStream(G+C)</td><td></td>
			</tr>~;
foreach(@recods)
    {   
        $sequence=$_;
        $backup=$sequence;
           
        while ($sequence =~ m/(($motif){3,})/g )
        { 
        	$locus=$1;
          $seq_len=length($sequence);
          $len=length($1);
          $p= pos($sequence)- $len;
          
          $up=substr $sequence ,$p-20,20;
          $repeats=()=$1=~/$motif/g;
    	  $Ids[$i]=~ m/([a-zA-Z]+)#S([0-9]+)/;
	$id=$2;  
	$idName=$1;
    	  
          $down=substr $sequence,$p+$len,20;
          $no_up=()=$up=~/([GC])/g;
          $no_down=()=$down=~/([GC])/g;
          if($p>20&&$p+$len+20<length($sequence))
{		  
		  $locus=$up.$locus.$down;
          print qq~<form type="post" action="Blast.cgi" target="_blank">
          <tr class="light">
		  <td ><a href="http://www.ncbi.nlm.nih.gov/UniGene/seq.cgi?ORG=$idName&SID=$id" target="_blank">$Ids[$i]</a></td>
		  <td >$repeats</td>
		  <td width="120px"><input type="hidden" name="locus" value="$locus"/>$up<font color="red">($motif)</font>$down</td>
		  <td ><input type="hidden" name="up" value="$up"/>$no_up</td>
		  <td ><input type="hidden" name="down" value="$down"/>$no_down</td>
		  <td > <input type="image" src="../images/blast.png " alt="Submit"></td>
		  </tr></form>~;
}
        }
         $i++;
     }
print qq~</table>
  
	</div>
<p align="center" style="font-size:14px;"> Note:</p>
  <p align="center" style="font-size:14px;">1) If no record is shown then it means locus for the selected motif is not found.</p>
  <p align="center" style="font-size:14px;">2) Value inside brackets "(XX)" indicate that motif "XX" is repeated atleast 3 times. 



<div class="wrapper">
  <div id="copyright" class="clear">
	<p>Copyright &copy; 2013 - All Rights Reserved - <a href="http://www.anthonys.ac.in">Bio-technology Department, St.Anthonys College | www.anthonys.ac.in</a> </p>
	<p>Developed by Kaushik Deb Nath(kdebnath56@gmail.com)</p>
  </div>
</div>
 





</body> </html> ~ ;

