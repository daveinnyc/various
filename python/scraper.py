'''
Script to gather contact data from <SITE NAME> 

Site details have been removed. This could be a guide for scraping another 
site once site specific detaisl are added back in. 

Note: an earlier version used beautiful soup, but the site html was broken 
      (extra </td> tags) and caused the soup parser to miss most cell contents

'''
import csv
import urllib2
import re
import time



def build_urls():
    urls = []
    
    us_states = {"AL": ["Burmingham", "Tuscaloosa"],
    "AZ": ["Scottsdale", "Tucson", "Tempe"],
    "CA": ["Oakland", "San+Francisco", "San+Diego"],
    "NY": ["New+York", "Buffalo"],
    "NC": ["Charlotte"],
    "WI": ["Green+Bay"]
    }
                 
    work_type = ["outside"]         #Commercial also types: "inside" -> residential, "energy" -> non-building
    
    major_work_suffix = ["%3AG2","%3AD2","%3AD3","%3AL1","%3ALV4","%3AG3","%3AS2","%3ALV6","%3AD1"]
                    
    url_base = SITE_NAME + "/" + REST_OF_PATH_IN_URL   #NOTE: This needs to be updated for the site to be scraped
    url_state = "state=" #e.g. "state=WA"
    url_work_type = "&work="   #e.g. "&work=energy"
    url_city = "&inclnm=No&directly=&CityName="    #e.g.  "&inclnm=No&directly=&CityName=Some+City
    url_city_finish = "&CntyName="                #value blank if not used in query
    url_major_work = "&majorwork="   #e.g.  "&majorwork=[PREFIX]%3ALV2"
    url_remainder = "&project_size=1000&project_size_type=total&bonded=+&designbuild=+"
    
    
    for wt in work_type:
        for st in us_states.keys():
            for city in us_states[st]:
                if "outdoor" == wt:
                    prefix = "BC"
                elif "indoor" == wt:
                    prefix = "LC"
                else:
                    prefix = "ES"
                for mw in major_work_suffix:
                    url_to_fetch = url_base \
                       + url_state + st \
                       + url_work_type + wt \
                       + url_city + city + url_city_finish\
                       + url_major_work + prefix + ":" + mw \
                       + url_remainder
                    urls.append(url_to_fetch)

    '''
    #Just use one url for testing
    urls = []
    urls = ["GENERATE A LIST THEN PICK ONE"]
    '''
    '''
    #Just print out list and die for testing
    for u in urls: print u
    import sys
    sys.exit()
    '''    
    
    return urls


def get_state(url):
    ret_value = ''
    regex_state = re.compile('state=(\w\w)')
    
    m = regex_state.search(url)
    if m:
        ret_value = m.group(1)
    else:
        ret_value ="ERROR: NO STATE"
        
    return ret_value
    
    
   
def get_city(url):
    ret_value = ''
    regex_city = re.compile('&CityName=(\w*\+?\w*)&')
    
    m = regex_city.search(url)
    if m:
        ret_value = m.group(1)
    else:
        ret_value ="ERROR: NO CITY"
        
    return ret_value
    
    
    
def get_work_type(url):
    ret_value = ''
    regex_work_type = re.compile('&work=(\w*)&')
    
    m = regex_work_type.search(url)
    if m:
        type_code = m.group(1)
        if "outside" == type_code:
            ret_value = "Commercial"
        elif "indoor" == type_code:
            ret_value = "Residentail"
        else:
            ret_value = "Non-building"
    else:
        ret_value ="ERROR: NO WORK TYPE"
        
    return ret_value    


    
def parse_page(url):
    row_list = []
    regex_city_state = re.compile('(\w.*\s?\w.*?), (\w\w)')
    regex_phone = re.compile('^\(?\d{3}\)?[- ]\d{3}[- ]\d{4}')
    regex_member_id = re.compile('"(.*memberid=\d*)">(.*)<')
    regex_row = re.compile('<tr>(.*?)</tr>')
    regex_cell = re.compile('<td .*?>(.*?)</td>')
    regex_href_contact = re.compile('<a(.*?)>(.*?)</a>')
    regex_empty_line = re.compile('^$')

    print "TRYING: " + url
    try:
        response = urllib2.urlopen(url)
    except:
        print "FAILED: URL " + url
        empty = []
        return empty
        
    html_original = response.read()
    html = html_original.replace('\n', '')
    html = re.sub('\s{2,}', ' ', html)
    
    rows = re.finditer(regex_row, html)
    for r in rows: 
        this_row = []
               
        cells = re.findall(regex_cell, r.group(1))
        for c in cells: 
            #Process cells in column three
            if regex_phone.match(c):
                this_row.append(regex_phone.match(c).group(0))  #Phone Number
                hrefs = re.findall(regex_href_contact,c)
                for h in hrefs: 
                    this_row.append(h[1]) #Email address, web site

            #Process cells in column two
            elif regex_city_state.search(c):
                city = regex_city_state.search(c).groups()[0]
                state = regex_city_state.search(c).groups()[1]
                this_row.append(city)    #Contractor location
                this_row.append(state)   #(may be willing to travel to search location)
                
            #Process cells in column one    
            elif regex_member_id.search(c):
                company = regex_member_id.search(c).groups()[1]
                member_id = regex_member_id.search(c).groups()[0]
                this_row.append(company)
                this_row.append(member_id)
              
            else:
                #print "IGNORE: " + c
                pass
                
               
        if 0 < len(this_row):
            this_row.insert(0, get_city(url))
            this_row.insert(1, get_state(url))
            this_row.insert(2, get_work_type(url))
            row_list.append(this_row)
        
    print "ENDING: " + url
    
    return row_list

    
def print_records(record_list):
    csv_output = open('OUTPUT_FILE_NAME.csv', 'a+')
    writer = csv.writer(csv_output)
    for r in record_list:
        writer.writerow(r)
            
    
######################
######## MAIN ########
######################    
url_list = build_urls()
for url in url_list:
    print_records(parse_page(url))
    time.sleep(3) #Try not to crush their server
        

#EOF
