#!/usr/bin/perl
use CGI qw(:standard);
use File::Path qw(make_path);
print "Content-type: text/html; charset=iso-8859-1\n\n";
use CGI::Carp qw(fatalsToBrowser);

						# delete all previous data uploaded that are 2 days old
use File::Path;
opendir $f, "../Data/";
@file=readdir $f;
close $f;
foreach(@file)
{	
	if(!($_=~/\./))
	{
		$fld="../Data/".$_;
		$file="../upload/".$_.".txt";
		# print "\n$fld"."\t\t".(-M $fld);
		if(-M $fld>2){	
			rmtree($fld);unlink $file;
		}
	}
}

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

	# concatenating lines of dna and keeping only id

	
$source="../upload/".$file.".txt";
open $src, '<', $source;
$targetR="../Data/".$file."/Cleaned/Records.txt";
$targetID="../Data/".$file."/Cleaned/Ids.txt";

make_path("../Data/".$file."/Cleaned","../Data/".$file."/Cluster","../Data/".$file."/Motifs","../Data/".$file."/TotalCount");

open $tarR, '>', $targetR;
open $tarID, '>', $targetID;
$f=1;
while($line=<$src>)
{
	if($line !~ />/){
		chomp($line);
		print $tarR $line;
	}
	else{
		$line=~ /([a-zA-Z]{2,}#S[0-9]*)/;
		if($f==1){$f=0;}else{print $tarR "\n";}
		print $tarID ($1)."\n";
	}
}
close $tar;
close $src;

	#Counting & finding Motifs

open MOT,'>',"../Data/".$file."/Motifs/motifs.txt";
open $tarR,'<',$targetR;
@arr=<$tarR>;
close($tarR);
for($size=2;$size<=6;$size++)
{
	foreach(@arr)
	{
			
		$sequence=$_;
		while ($sequence =~ m/(\w{$size})/)
		{
			$lineshash{"$1"}+=1;
			$sequence =~ s/\w//;
			
		}	
	}
	open REPORT, ">", "../Data/".$file."/TotalCount/TotalCount[$size].txt" or die $!;
	@k = sort by_score keys %lineshash;
	foreach(@k)    {
		if($lineshash{$_}<100){}
		else{
			print REPORT "$_\t$lineshash{$_}\n";
			print MOT "$_\n";
		}
		
	}
	close(REPORT);
	%lineshash=();
}
close(MOT);
sub by_score { $lineshash{$b} <=> $lineshash{$a} };



	#Extracting key-value from post methord

if ( $ENV{'REQUEST_METHOD'} eq "POST" ) {
	read(STDIN,$form, $ENV{'CONTENT_LENGTH'}); 
	
}else
{print 'no i/p';}
foreach $pair (split('&', $form)) {
        if ($pair =~ /(.*)=(.*)/) 
	{  # found key=value;
		($key,$value) = ($1,$2);     # get key, value.
		$inputs{$key} = $value;   
         }
}

	#Redirecting 
	
$met="<meta http-equiv=\"refresh\" content=\"0.5;url=./PrimaryResult.cgi?id=$file\" />
	</head>
	If you are not automatically redirected,then <a href=\"./PrimaryResult.cgi?id=$file\">click here</a>";

print $met;