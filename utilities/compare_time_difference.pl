#!/usr/bin/perl

#Get time differences from a bunch of input lines
#Input line starts like this:
# [2011-03-08 12:39:14.777] [INFO] Migrating source run 260 into stream prevent-dev

use warnings;
use strict;
use constant { TRUE => 1, 
               FALSE => 0
             };

use Time::Local;

sub get_num_seconds{

    my $line = shift;

    if( $line =  /\[(\d\d\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d):(\d\d)\.\d\d\d\]/ ){
        my $year = $1;
        my $month = $2;
        my $mday = $3;
        my $hour = $4;
        my $min = $5;
        my $sec = $6;

        #time in seconds = timegm( $sec, $min, $hour,  $mday, $month, $year);

        return( timegm( $sec, $min, $hour,  $mday, $month, $year) );
     } else {
       die "MISSING TIME STAMP\n";
     }   
}#End get_num_seconds


#Setup variable for the while loop 
my $firstRun = TRUE;
my $timeLastRunFinished = 0;
my $timeThisRunFinished = 0;
my $timeForThisRun = 0;
my $timeForLastRun = 0;
my $totalTime = 1;
my $totalRuns = 0;
my $changeThisRun = 0;
my $changeLastRun = 0;
while ( <STDIN> ){
    chomp( my $inputLine = $_ );

    if( $inputLine =~ /Migrating source run/ ){

        #How long did this run take?
        $timeThisRunFinished = get_num_seconds( $inputLine );
        $timeForThisRun = $timeThisRunFinished - $timeLastRunFinished;

        #Are we getting better or worse?
        $changeThisRun = $timeForThisRun - $timeForLastRun;
        my $runDifference = $changeThisRun - $changeLastRun;

        #Work out the current average runtime
        $totalTime += $changeThisRun unless( $firstRun == TRUE );
        $totalRuns += 1;
        my $averageRunTime = $totalTime / $totalRuns;

        #Tell me about it 
        if ( $runDifference < 0 ){
            printf( "FASTER: This run: %5d     Diff: %5d     Ave: %5d\n", $changeThisRun, $runDifference, $averageRunTime );
        } elsif ( $runDifference > 0 ){
            printf( "SLOWER: This run: %5d     Diff: %5d     Ave: %5d\n", $changeThisRun, $runDifference, $averageRunTime );
        } else {
            printf( "EQUAL:  This run: %5d     Diff: %5d     Ave: %5d\n", $changeThisRun, $runDifference, $averageRunTime );
        }#End if $changeThisRun

        #Set up for next time through loop 
        $firstRun = FALSE;
        $timeForLastRun = $timeForThisRun;
        $changeLastRun = $changeThisRun;
    }#End if ~= $input line
}#End while STDIN

#EOF
