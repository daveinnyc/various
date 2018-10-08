'''
Parse Instagram Datafiles to genereate some usage stats

HOW TO RUN:
Download the instagram data file using the link on the IG web site
Extract and copy the json files to a subdirectory called json-input
Run this script from directly above the subdirectory
'''
import json
import csv
import sys
import datetime as dt
from collections import defaultdict


def get_followers():
    try:
        with open("json-input/connections.json", "r") \
             as connections_file:
             connections = json.load(connections_file)
    except IOError as ioerr:
        print("File error: {}".format(ioerr))
    except Exception as e:
        print("Other file error: {}".format(e))
    
    '''
    Connection types as of 2018-10-07
        blocked_users
        follow_requests_sent
        followers   # accounts that follow you
        following   # accounts that you follow
        following_hashtags
    '''
    followers = {}
    followers_by_date = defaultdict(list)
    for follower,join_date in connections['followers'].items():
        followers[follower] = join_date[:10]
        jd_date = dt.datetime.date(dt.datetime.strptime(
                              join_date, '%Y-%m-%dT%H:%M:%S'))
        followers_by_date[jd_date].append(follower)
        
    try:
        with open("followers.csv", "w") as output:
            # For dev / debugging
            # w = csv.writer(sys.stderr)
            w = csv.writer(output)
            w.writerows(followers.items())
    except IOError as ioe:
            print("IOError: {}".format(ioe))
    except Exception as e:
            print("SOme other error: {}".format(e))
            
    return followers_by_date

def main():
    followers = get_followers()
    
    
if __name__ == "__main__":
    main()
    
# EOF