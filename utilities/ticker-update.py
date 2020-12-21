import requests
from bs4 import BeautifulSoup 

URL = 'https://finance.yahoo.com/quote/'
CONF_FILE = r"G:\system\ticker-updates.conf"


def get_securities_list():
   with open(CONF_FILE, "r") as conf_file:
      securities = conf_file.readlines()
      securities = [s.strip() for s in securities]
 
   return securities


def update_information(security):
   symbol, sell_price = security.split(',')

   query = URL + symbol
   page = requests.get(query)
   soup = BeautifulSoup(page.content, 'html.parser')

   span = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
   table_row = soup.select('table td')
   
   sell_price = float(sell_price)
   price = float(span.get_text())
   open_price = float(table_row[3].text)
   
   print(f"{symbol:>6}:  {open_price:<6}  {price:<6}  "
         f"{sell_price:<6}  {sell_price - price:<6.3f}  "
         f"{(sell_price - price) / sell_price :<6.2f}"
         )


def print_header():
   print(f"SYMBOL   OPEN    PRICE   SELL    DIFF    PERCENT")
   print(f"========+=======================================")
   
   
############
### MAIN ###
############
securities = get_securities_list()
print_header()
for security in securities:
    update_information(security)
    
# EOF
