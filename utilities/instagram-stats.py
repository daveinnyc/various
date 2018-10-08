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
    
    followers = {}
    followers_by_date = defaultdict(list)
    # 'connections' json structure has a 'followers' section
    for follower,join_date in connections['followers'].items():
        followers[follower] = join_date[:10]
        jd_date = dt.datetime.date(dt.datetime.strptime(
                              join_date, '%Y-%m-%dT%H:%M:%S'))
        followers_by_date[jd_date].append(follower)


    write_csv("followers.csv", followers)    

    return followers_by_date
          
    
def num_followers_to_date(followers_dict):
    num_by_date = defaultdict(list)
    account_list = []
    count = 0
    for k, v in sorted(followers_dict.items()):
        count = count + len(v)
        account_list.extend(v)
        num_by_date[k] = [count]
        num_by_date[k].extend(account_list)       
        
    write_csv("num_followers.csv", num_by_date)
    
    return num_by_date    


def write_csv(filename, dictionary):        
    try:
        filename = str(dt.date.today()) + "." + filename
        with open(filename, "w") as output:
            # For dev / debugging
            # w = csv.writer(sys.stderr)
            w = csv.writer(output)
            w.writerows(dictionary.items())
    except IOError as ioe:
            print("IOError: {}".format(ioe))
    except Exception as e:
            print("Some other error: {}".format(e))

            
def main():
    followers = get_followers()
    follow_count_by_date = num_followers_to_date(followers)
    #for a,b in sorted(follow_count_by_date.items()):
    #    print("{}: {}".format(a, b))
    
    
if __name__ == "__main__":
    main()
    
# EOF