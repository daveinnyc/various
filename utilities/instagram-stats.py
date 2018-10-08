'''
Parse Instagram Datafiles to genereate some usage stats

HOW TO RUN:
Download the instagram data file using the link on the IG web site
Extract and copy the json files to a subdirectory called json-input
Run this script from directly above the subdirectory
'''
import json


def process_followers():
    try:
        with open("json-input/connections.json", "r") \
             as connections_file:
             connections = json.load(connections_file)
    except IOError as ioerr:
        print("File error: {}".format(ioerr))
    except Exception as e:
        print("Other file error: {}".format(e))
    
    '''
    Connection types 2018-10-07
        blocked_users
        follow_requests_sent
        followers   # accounts that follow you
        following   # accounts that you follow
        following_hashtags
    '''
    print(len(connections['followers']))
    for k,v in connections['followers'].items():
        print("{} {}".format(k, v))


def main():
    process_followers()
    
    
if __name__ == "__main__":
    main()
    
# EOF