#!/usr/bin/perl

use warnings;
use strict;
use DBI;
use constant TRUE => 1;
use constant FALSE => 0;
use Getopt::Long;


my $start_date = "2010-11-15";        #Default, -s <value>   command line override
my $end_date = "2011-02-27";          #Default, -e <value>   command line override
my $target_milestone = "5.4.0";       #Default, -t <value>   command line override
my %result_counts;
my $human_output = FALSE;             #Default, -h command line overrride

GetOptions( 'start_date=s' => \$start_date,
            'end_date=s' => \$end_date,
            'target_milestone=s' => \$target_milestone,
            'human_output' => \$human_output
          );



#Connect to DB
my $dbHandle = DBI->connect( "DBI:mysql:database=bugs;host=bugzilla.sf.coverity.com", 
                               "bugs", "bug1zilla", { 'RaiseError' => 1 } );


my $query_bugs_created = "SELECT bugs.bug_id AS bug_id,
                                 DATE_FORMAT( bugs.creation_ts, \'%Y-%m-%d\' ) AS openDate
                            FROM bugs 
                            INNER JOIN products AS map_products 
                                 ON (bugs.product_id = map_products.id) 
                            LEFT JOIN bug_group_map 
                                 ON bug_group_map.bug_id = bugs.bug_id 
                                 AND bug_group_map.group_id 
                                     NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                            WHERE ((bugs.creation_ts >= \'${start_date} 00:00:00\'))
                                 AND ((bugs.creation_ts <= \'${end_date} 00:00:00\'))
                                 AND (( bugs.target_milestone IN (\'${target_milestone}\') )) 
                                 AND bugs.creation_ts IS NOT NULL
                                 AND (bug_group_map.group_id IS NULL) 
                             ;" ;     

my $query_bugs_resolved_fixed = "SELECT bugs.bug_id AS bug_id,
                                        actcheck.added AS added,
                                        DATE_FORMAT( bugs.creation_ts, \'%Y-%m-%d\' ) AS openDate,
                                        DATE_FORMAT( actcheck.bug_when, \'%Y-%m-%d\' ) AS activityDate,
                                        DATE_FORMAT( bugs.delta_ts, \'%Y-%m-%d\' ) AS changeddate
                                   FROM bugs
                             INNER JOIN products AS map_products
                                        ON (bugs.product_id = map_products.id)
                              LEFT JOIN bugs_activity AS actcheck
                                        ON (actcheck.bug_id = bugs.bug_id
                                            AND actcheck.bug_when >= \'$start_date 00:00:00\' 
                                            AND actcheck.bug_when <= \'$end_date 00:00:00\'
                                            AND actcheck.added = 'FIXED'
                                            AND actcheck.fieldid IN (11) )
                              LEFT JOIN bug_group_map
                                        ON bug_group_map.bug_id = bugs.bug_id
                                        AND bug_group_map.group_id
                                            NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13)
                                  WHERE ((actcheck.bug_when IS NOT NULL))
                                        AND (( bugs.target_milestone IN (\'$target_milestone\') )) 
                                        AND bugs.creation_ts IS NOT NULL
                                        AND (bug_group_map.group_id IS NULL)
                               ORDER BY changeddate,bug_id
                                     ;" ;


my $query_bugs_verified = "SELECT bugs.bug_id AS bug_id,
                                  actcheck.added AS added,
                                  DATE_FORMAT( bugs.creation_ts, \'%Y-%m-%d\' ) AS openDate,
                                  DATE_FORMAT( actcheck.bug_when, \'%Y-%m-%d\' ) AS activityDate,
                                  DATE_FORMAT( bugs.delta_ts, \'%Y-%m-%d\' ) AS changeddate
                             FROM bugs
                       INNER JOIN products AS map_products
                                  ON (bugs.product_id = map_products.id)
                        LEFT JOIN bugs_activity AS actcheck
                                  ON (actcheck.bug_id = bugs.bug_id
                                      AND actcheck.bug_when >= \'$start_date 00:00:00\'
                                      AND actcheck.bug_when <= \'$end_date 00:00:00\'
                                      AND actcheck.added = 'VERIFIED'
                                      AND actcheck.fieldid IN (8) )
                         LEFT JOIN bug_group_map
                                   ON bug_group_map.bug_id = bugs.bug_id
                                       AND bug_group_map.group_id
                                           NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13)
                              WHERE ((actcheck.bug_when IS NOT NULL))
                                    AND bugs.target_milestone IN (\'$target_milestone\') 
                                    AND bugs.creation_ts IS NOT NULL
                                    AND bug_group_map.group_id IS NULL
                                ;" ;


my $query_bugs_reopened = "SELECT bugs.bug_id AS bug_id,
                                  actcheck.added AS added,
                                  DATE_FORMAT( bugs.creation_ts, \'%Y-%m-%d\' ) AS openDate,
                                  DATE_FORMAT( actcheck.bug_when, \'%Y-%m-%d\' ) AS activityDate,
                                  DATE_FORMAT( bugs.delta_ts, \'%Y-%m-%d\' ) AS changeddate
                             FROM bugs 
                       INNER JOIN products AS map_products 
                                  ON (bugs.product_id = map_products.id) 
                        LEFT JOIN bugs_activity AS actcheck 
                                  ON (actcheck.bug_id = bugs.bug_id 
                                  AND actcheck.bug_when >= \'$start_date 00:00:00\' 
                                  AND actcheck.bug_when <= \'$end_date 00:00:00\'
                                  AND actcheck.added = \'reopened\' 
                                  AND actcheck.fieldid IN (8) ) 
                        LEFT JOIN bug_group_map 
                                  ON bug_group_map.bug_id = bugs.bug_id 
                                     AND bug_group_map.group_id 
                                         NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                            WHERE ((actcheck.bug_when IS NOT NULL)) 
                                  AND bugs.target_milestone IN (\'$target_milestone\')  
                                  AND bugs.creation_ts IS NOT NULL 
                                  AND bug_group_map.group_id IS NULL 
                               ;" ;


my $select = "";

#Execute query - opened
$select = $dbHandle->prepare( $query_bugs_created ); 
$select->execute();

#Parse results - opened
my $count_opened = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_opened++;
    $result_counts{ $results->{ 'openDate' } }[ 0 ]++;
}#End while

#Execute query - resolved fixed
$select = $dbHandle->prepare( $query_bugs_resolved_fixed ); 
$select->execute();

#Parse results - resolved fixed
my $count_resolved_fixed = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_resolved_fixed++;
    $result_counts{ $results->{ 'activityDate' } }[ 1 ]++;
}#End while

#Execute query - reopened
$select = $dbHandle->prepare( $query_bugs_reopened ); 
$select->execute();

#Parse results - reopened
my $count_reopened = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_reopened++;
    $result_counts{ $results->{ 'activityDate' } }[ 2 ]++;
}#End while

#Execute query - verified
$select = $dbHandle->prepare( $query_bugs_verified ); 
$select->execute();

#Parse results - verified
my $count_verified = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_verified++;
    $result_counts{ $results->{ 'activityDate' } }[ 3 ]++;
}#End while



#Print out results 
my $separator = ','; #Default to csv format

if ( $human_output ){
    $separator = '           '; 

    print "Opened since $start_date: $count_opened\n";
    print "Resolved since $start_date: $count_resolved_fixed\n";
    print "Reopened since $start_date: $count_reopened\n";
    print "Verified since $start_date: $count_verified\n";
    print "\n";
}#End $human_output

print "Date${separator}Opened${separator}Fixed${separator}Reopen${separator}Verified\n";
foreach my $key ( sort ( keys( %result_counts ) ) ){
    print $key;
    for ( my $i = 0 ; $i < 4 ; $i++ ){
        if ( $result_counts{ $key }[ $i ] ){
             print "${separator}$result_counts{ $key }[ $i ]";
        } else {
             #Just print 0 if $result_counts{ $key }[ $i ] is undefined
             print "${separator}0";
        }#End if - else     
    }#End for $i
    print "\n";
}#End foreach $key


#Clean up connections
$dbHandle->disconnect();

#EOF
