import requests
from bs4 import BeautifulSoup 

URL = 'https://finance.yahoo.com/quote/'
CONF_FILE = "ticker-updates.conf"
secutities = []

with open(CONF_FILE, "r") as conf_file:
    securities = conf_file.readlines()
    securities = [s.strip() for s in securities]
    
for security in securities:
   symbol, sell_price = security.split(',')
   sell_price = float(sell_price)
   query = URL + symbol

   page = requests.get(query)
   soup = BeautifulSoup(page.content, 'html.parser')

   span = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
   price = float(span.get_text())

   table_row = soup.select('table td')
   open = float(table_row[3].text)
   
   print(f"{symbol:>6}: {open:<6}  {price:<6}  {sell_price:<6}  {sell_price - price:<6.3f}")
