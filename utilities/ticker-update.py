import requests
from bs4 import BeautifulSoup 

URL = 'https://finance.yahoo.com/quote/'
secutities = []

with open("ticker-updates,cong", r) as conf_file:
    securities = conf_file.readlines()
    securities = [s.strip() for s in securities]
    
for security in securities:
   query = URL + security

   page = requests.get(query)
   soup = BeautifulSoup(page.content, 'html.parser')
   span = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
   price = span.get_text()
   table_row = soup.select('table td')
   open = table_row[3].text
   
   print(f"{security:>6}: {open:<6}  {price:<6}")
