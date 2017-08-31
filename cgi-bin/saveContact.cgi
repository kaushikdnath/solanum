#!/usr/bin/perl
use CGI qw(:standard);
use File::Basename;
print "Content-type: text/html; charset=iso-8859-1\n\n";

open CONTACT,'>>', "./Contact/Contact.txt";
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
if($inputs{"value"})
{
	$inputs{"value"}=~ s/[+]/ /g;
	$inputs{"value"}=~ s/%0D%0A/\n\t\t/g;
	print CONTACT "\n\nNAME::\t".$inputs{"nam"}."\nEMAIL::\t".$inputs{"email"}."\nMESSAGE::\n\t\t".$inputs{"value"}."\n______________________________________________________________";
}
print qq~
	<meta http-equiv="refresh" content="0.5;url=../Contact.html" />
~;