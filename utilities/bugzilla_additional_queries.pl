#!/usr/bin/perl

# How many open bugs were there in a given year for several years

use warnings;
use strict;
use DBI;
use constant TRUE => 1;
use constant FALSE => 0;
use Getopt::Long;


my $start_date = "2010-10-01";        #Default, -s <value>   command line override
my $end_date = "2010-12-31";          #Default, -e <value>   command line override
my $target_milestone = "5.3.0";       #Default, -t <value>   command line override
my %result_counts;                    #Counts for each quesry, by date
my %sums_by_year;                     #Sums by year of query counts
my $human_output = FALSE;             #Default, -h command line overrride
my $num_queries = 5;                  #Used to work with:  $result_counts{ $key }[ $num_queries ] 

GetOptions( 'start_date=s' => \$start_date,
            'end_date=s' => \$end_date,
            'target_milestone=s' => \$target_milestone,
            'human_output' => \$human_output
          );



#Connect to DB
my $dbHandle = DBI->connect( "DBI:mysql:database=bugs;host=bugzilla.sf.coverity.com", 
                               "bugs", "bug1zilla", { 'RaiseError' => 1 } );

#DATE FAKE FOR KEN's YEAR BASED QUERIES
my $YEAR = '';
my $count_opened = 0;
my $count_resolved_fixed = 0;
my $count_reopened = 0;
my $count_verified = 0;
my $count_resolved_any = 0;


my $query_bugs_created = "SELECT bugs.bug_id  AS bug_id, 
                            map_products.name AS product, 
                            DATE_FORMAT( bugs.creation_ts, \'%Y-%m\' ) AS opendate, 
                            DATE_FORMAT( bugs.delta_ts, \'%Y-%m\' )  AS changeddate 
                    FROM bugs 
                INNER JOIN profiles AS map_reporter 
                            ON (bugs.reporter = map_reporter.userid) 
                INNER JOIN products AS map_products 
                            ON (bugs.product_id = map_products.id)
                LEFT JOIN priority 
                            ON (priority.value = bugs.priority) 
                LEFT JOIN bug_group_map 
                            ON bug_group_map.bug_id = bugs.bug_id 
                            AND bug_group_map.group_id 
                            NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                LEFT JOIN cc 
                            ON cc.bug_id = bugs.bug_id AND cc.who = 164 
                    WHERE ((bugs.creation_ts >= \'${start_date} 00:00:00\'))
                            AND ((bugs.creation_ts <= \'${end_date} 00:00:00\'))
                            AND ( bugs.product_id IN (19) ) 
                            AND bugs.creation_ts IS NOT NULL
                            AND ((bug_group_map.group_id IS NULL) 
                                OR (bugs.reporter_accessible = 1 AND bugs.reporter = 164) 
                                OR (bugs.cclist_accessible = 1 AND cc.who IS NOT NULL) 
                                OR (bugs.assigned_to = 164) 
                                OR (bugs.qa_contact = 164) ) 
                    GROUP BY bugs.bug_id 
                    ORDER BY changeddate;"; 

my $query_bugs_resolved_fixed = "SELECT bugs.bug_id AS bug_id, 
                            map_products.name AS product, 
                            DATE_FORMAT( bugs.creation_ts, \'%Y-%m\' ) AS opendate, 
                            DATE_FORMAT( bugs.delta_ts, \'%Y-%m\' )  AS changeddate 
                    FROM bugs 
                INNER JOIN profiles AS map_reporter 
                            ON (bugs.reporter = map_reporter.userid) 
                INNER JOIN products AS map_products 
                            ON (bugs.product_id = map_products.id) 
                LEFT JOIN bugs_activity AS actcheck 
                            ON (actcheck.bug_id = bugs.bug_id 
                            AND actcheck.bug_when >= \'${start_date} 00:00:00\' 
                            AND actcheck.bug_when <= \'${end_date} 00:00:00\' 
                            AND actcheck.added = \'FIXED\' 
                            AND actcheck.fieldid IN (11) ) 
                LEFT JOIN bug_group_map 
                            ON bug_group_map.bug_id = bugs.bug_id 
                            AND bug_group_map.group_id 
                            NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                LEFT JOIN cc 
                            ON cc.bug_id = bugs.bug_id 
                            AND cc.who = 164 
                    WHERE ((actcheck.bug_when IS NOT NULL)) 
                        AND (( bugs.product_id IN (19) )) 
                GROUP BY bugs.bug_id 
                ORDER BY opendate,changeddate;" ;


my $query_bugs_verified = "SELECT bugs.bug_id AS bug_id, 
                            map_products.name AS product, 
                            DATE_FORMAT( bugs.creation_ts, \'%Y-%m\' ) AS opendate, 
                            DATE_FORMAT( bugs.delta_ts, \'%Y-%m\' )  AS changeddate 
                    FROM bugs 
                INNER JOIN profiles AS map_reporter 
                            ON (bugs.reporter = map_reporter.userid) 
                INNER JOIN products AS map_products 
                            ON (bugs.product_id = map_products.id) 
                LEFT JOIN bugs_activity AS actcheck 
                            ON (actcheck.bug_id = bugs.bug_id 
                                AND actcheck.bug_when >= \'${start_date} 00:00:00\' 
                                AND actcheck.bug_when <= \'${end_date} 00:00:00\' 
                                AND actcheck.added = 'VERIFIED' 
                                AND actcheck.fieldid IN (8) )
                LEFT JOIN priority ON (priority.value = bugs.priority) 
                LEFT JOIN bug_group_map 
                            ON bug_group_map.bug_id = bugs.bug_id 
                            AND bug_group_map.group_id 
                            NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                LEFT JOIN cc 
                            ON cc.bug_id = bugs.bug_id 
                            AND cc.who = 164 
                    WHERE ((actcheck.bug_when IS NOT NULL)) 
                            AND (( bugs.product_id IN (19) )) 
                            AND bugs.creation_ts IS NOT NULL 
                            AND ((bug_group_map.group_id IS NULL) 
                                OR (bugs.reporter_accessible = 1 AND bugs.reporter = 164) 
                                OR (bugs.cclist_accessible = 1 AND cc.who IS NOT NULL) 
                                OR (bugs.assigned_to = 164) 
                                OR (bugs.qa_contact = 164) ) 
                GROUP BY bugs.bug_id 
                ORDER BY opendate;" ; 

my $query_bugs_reopened = "SELECT bugs.bug_id AS bug_id, 
                            map_products.name AS product, 
                            DATE_FORMAT( bugs.creation_ts, \'%Y-%m\' ) AS opendate, 
                            DATE_FORMAT( bugs.delta_ts, \'%Y-%m\' )  AS changeddate 
                    FROM bugs 
                INNER JOIN profiles AS map_reporter 
                            ON (bugs.reporter = map_reporter.userid) 
                INNER JOIN products AS map_products 
                            ON (bugs.product_id = map_products.id) 
                LEFT JOIN bugs_activity AS actcheck 
                            ON (actcheck.bug_id = bugs.bug_id 
                            AND actcheck.bug_when >= \'${start_date} 00:00:00\' 
                            AND actcheck.bug_when <= \'${end_date} 00:00:00\' 
                            AND actcheck.added = 'REOPENED' 
                            AND actcheck.fieldid IN (8) ) 
                LEFT JOIN priority 
                            ON (priority.value = bugs.priority) 
                LEFT JOIN bug_group_map 
                            ON bug_group_map.bug_id = bugs.bug_id 
                            AND bug_group_map.group_id 
                            NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                LEFT JOIN cc 
                            ON cc.bug_id = bugs.bug_id 
                            AND cc.who = 164 
                    WHERE ((actcheck.bug_when IS NOT NULL)) 
                            AND (( bugs.product_id IN (19) )) 
                            AND bugs.creation_ts IS NOT NULL 
                            AND ((bug_group_map.group_id IS NULL) 
                                OR (bugs.reporter_accessible = 1 AND bugs.reporter = 164) 
                                OR (bugs.cclist_accessible = 1 AND cc.who IS NOT NULL) 
                                OR (bugs.assigned_to = 164) 
                                OR (bugs.qa_contact = 164) ) 
                GROUP BY bugs.bug_id 
                ORDER BY opendate; ";


my $query_bugs_resolved_any = "SELECT bugs.bug_id  AS bug_id, 
                            map_products.name AS product, 
                            DATE_FORMAT( bugs.creation_ts, \'%Y-%m\' ) AS opendate, 
                            DATE_FORMAT( bugs.delta_ts, \'%Y-%m\' )  AS changeddate, 
                            map_reporter.login_name AS reporter 
                    FROM bugs 
                INNER JOIN profiles AS map_reporter 
                            ON (bugs.reporter = map_reporter.userid) 
                INNER JOIN products AS map_products 
                            ON (bugs.product_id = map_products.id) 
                LEFT JOIN bugs_activity AS actcheck 
                            ON (actcheck.bug_id = bugs.bug_id 
                                AND actcheck.bug_when >= \'${start_date} 00:00:00\' 
                                AND actcheck.bug_when <= \'${end_date} 00:00:00\' 
                                AND actcheck.added = \'Resolved\' 
                                AND actcheck.fieldid IN (8) ) 
                LEFT JOIN priority 
                            ON (priority.value = bugs.priority) 
                LEFT JOIN bug_group_map ON bug_group_map.bug_id = bugs.bug_id 
                            AND bug_group_map.group_id 
                            NOT IN (8,3,7,9,4,5,2,39,20,44,30,21,41,36,37,22,32,23,13) 
                LEFT JOIN cc 
                            ON cc.bug_id = bugs.bug_id 
                            AND cc.who = 164 
                    WHERE ((actcheck.bug_when IS NOT NULL)) 
                            AND (( bugs.product_id IN (19) )) 
                            AND bugs.creation_ts IS NOT NULL 
                            AND ((bug_group_map.group_id IS NULL) 
                                OR (bugs.reporter_accessible = 1 AND bugs.reporter = 164) 
                                OR (bugs.cclist_accessible = 1 AND cc.who IS NOT NULL) 
                                OR (bugs.assigned_to = 164) OR (bugs.qa_contact = 164) ) 
                GROUP BY bugs.bug_id 
                ORDER BY opendate; " ;


my $select = "";


$start_date = "$YEAR-01-01";
$end_date = "$YEAR-12-31";

#Execute query - opened
$select = $dbHandle->prepare( $query_bugs_created ); 
$select->execute();

#Parse results - opened
$count_opened = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_opened++;
    $result_counts{ $results->{ 'opendate' } }[ 0 ]++;
}#End while

#Execute query - resolved fixed
$select = $dbHandle->prepare( $query_bugs_resolved_fixed ); 
$select->execute();

#Parse results - resolved fixed
$count_resolved_fixed = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_resolved_fixed++;
    $result_counts{ $results->{ 'changeddate' } }[ 1 ]++;
}#End while

#Execute query - reopened
$select = $dbHandle->prepare( $query_bugs_reopened ); 
$select->execute();

#Parse results - reopened
$count_reopened = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_reopened++;
    $result_counts{ $results->{ 'changeddate' } }[ 2 ]++;
}#End while

#Execute query - verified
$select = $dbHandle->prepare( $query_bugs_verified ); 
$select->execute();

#Parse results - verified
$count_verified = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_verified++;
    $result_counts{ $results->{ 'changeddate' } }[ 3 ]++;
}#End while

#Execute query - resolved any resolution
$select = $dbHandle->prepare( $query_bugs_resolved_any ); 
$select->execute();

#Parse results - resolved any resolution
$count_resolved_any = 0;
while( my $results = $select->fetchrow_hashref() ) {
    $count_resolved_any++;
    $result_counts{ $results->{ 'changeddate' } }[ 4 ]++;
}#End while


#Print out some headers 
my $separator = ','; #Default to csv format

if ( $human_output ){
    $separator = '           '; 

    print "Opened since $start_date: $count_opened\n";
    print "Fixed since $start_date: $count_resolved_fixed\n";
    print "Any Res since $start_date: $count_resolved_any\n";
    print "Reopened since $start_date: $count_reopened\n";
    print "Verified since $start_date: $count_verified\n";
    print "\n";
}#End $human_output

#Print results, also process totals
#  Should be refactored one day

my $year = '';
print "Date${separator}Opened${separator}Fixed${separator}Reopen${separator}Verified${separator}Any Res\n";
foreach my $key ( sort ( keys( %result_counts ) ) ){
   #The $key will be the date passed into the hash
    print $key;
    for ( my $i = 0 ; $i < $num_queries ; $i++ ){
        if ( $result_counts{ $key }[ $i ] ){
             print "${separator}$result_counts{ $key }[ $i ]";
             #Get the year from YYYY-MM-DD
             ( $year ) = split( '-', $key, 2 ); 
             if ( $i == 0 ){ 
                 $sums_by_year{ $year }[ 0 ] += $result_counts{ $key }[ $i ]; 
             }#End if open
             if ( $i == 4 ){ 
                 $sums_by_year{ $year }[ 1 ] += $result_counts{ $key }[ $i ];
             }#End if any_res
        } else {
             #Just print 0 if $result_counts{ $key }[ $i ] is undefined
             print "${separator}0";
        }#End if - else     
    }#End for $i
    print "\n";
}#End foreach $key

my $delta = 0;
my $running_total = 0;
print "\n\n\n";
print "Year${separator}Open${separator}Resolv${separator}Delta${separator}Total\n" ;
foreach my $y ( sort ( keys( %sums_by_year ) ) ){
    print $y; 
    for ( my $i = 0 ; $i < 2 ; $i++ ) {
        if ( $sums_by_year{ $y }[ $i ] ){ 
            print "${separator}$sums_by_year{ $y }[ $i ]"; 
        } else {
            $sums_by_year{ $y }[ $i ] = 0; 
            print "${separator}0"; 
        }#End if $sums-by_year          
    }#End for $i    
    $delta =  $sums_by_year{ $y }[ 0 ] - $sums_by_year{ $y }[ 1 ] ; 
    $running_total += $delta;
    print "${separator}$delta${separator}$running_total\n"; 
}#End foreach $key



#Clean up connections
$dbHandle->disconnect();


#EOF
