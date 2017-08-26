'''
The mp3 archive on iuma has files sorted according to details (descriptions) 
    and download directories. 
    
    e.g. https://archive.org/details/anarchopunk-1986
         https://archive.org/download/anarchopunk-1986
    
    It can be a pain to expand and click manually f you want to download from
    a bunch of directories. Once you know which directories are of interest, 
    add them to the group_page_list below and this script will get the files. 

    e.g. group_page_list = ["japanoise_japanoise_20130831", "anarchopunk-1986"]
    
 Copyright 2017 Dave Cuthbert, MIT license
'''



import requests as r
import time
import re
import os
from bs4 import BeautifulSoup


def get_listings_page(BASE_URL):
    page = r.get(listings_page)
    soup = BeautifulSoup(page.text, "html.parser")

    return soup
    

def search_mp3s(href, group):
    tmp = re.search("\A.*\.mp3\Z", str(href), re.I)
    if tmp:
        mp3 = r.get(BASE_URL + group + "/" + tmp.group(0), stream=True)
        with open(tmp.group(0),'wb') as output:
            for block in mp3.iter_content(1024):
                output.write(block)

        
def search_jpgs(href, group):
    tmp = re.search("\A.*\.jpg\Z", str(href), re.I)
    if tmp:
        jpg = r.get(BASE_URL + group + "/" + tmp.group(0), stream=True)
        with open(tmp.group(0),'wb') as output:
            for block in jpg.iter_content(1024):
                output.write(block)


if "__main__" == __name__:
    BASE_URL = "https://archive.org/download/"
    
    group_page_list = [ **ADD DIRECTORIES HERE** ]
    
    
    for group_page in group_page_list:
        time.sleep(1)
        current_dir = os.getcwd()
        os.mkdir(group_page)
        os.chdir(group_page)
        
        listings_page = BASE_URL + group_page
        soup = get_listings_page(listings_page)
        for link in soup.find_all('a'):
            href = link.get('href')
            search_mp3s(href, group_page)
            search_jpgs(href, group_page)
        
        os.chdir(current_dir)
