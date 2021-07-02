import requests
from bs4 import BeautifulSoup 
from collections import defaultdict

URL = 'https://finance.yahoo.com/quote/'
CONF_FILE = r"G:\system\ticker-updates.conf"


def get_securities_list():
   with open(CONF_FILE, "r") as conf_file:
      securities = conf_file.readlines()
      securities = [s.strip() for s in securities]
 
   return securities


def update_information(security):
   symbol, sell_price = security.split(',')
  
   user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' + \ 
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 ' + \ 
                       'Safari/537.36'
   headers = { 'User-Agent': user_agent_desktop}
 
   if (price_cache[symbol][0] == "0"):
      query = URL + symbol
      page = requests.get(query, headers=headers)
      soup = BeautifulSoup(page.content, 'html.parser')

      span = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
      table_row = soup.select('table td')
      
      price_cache[symbol][0] = float(span.get_text())    # last price
      price_cache[symbol][1] = float(table_row[3].text)  # open price
 
   price = price_cache[symbol][0]
   open_price = price_cache[symbol][1]
   sell_price = float(sell_price)
   diff = sell_price - price
   percent = round(diff / sell_price * 100, 3)
   change = (price - open_price) 
   price_up = change > 0
   
   return (symbol, price, open_price, sell_price, diff, percent, change, price_up)


def print_row(stock):
   symbol, price, open_price, sell_price, diff, percent, change, up = stock
   direction = '+' if up else '-'
   
   print(f"{symbol: >7}:  "
         f"{direction}{direction}  "
         f"{percent: >8.3f}"
         f"{diff: >8.2f}"
         f"{change: >8.2f}"
         f"{price: >8.2f}"
         f"{open_price: >8.2f}"
         f"{sell_price: >8.2f}"
        )


def print_header():
   print(f" SYMBOL   D     %TO GO    DIFF   CHNG    PRICE    OPEN    SELL  ")
   print(f"================================================================")
   

def print_table(update_list):
   update_list.sort(key=lambda sort_value: sort_value[0])
   print_header()
   for stock in update_list:
      print_row(stock)
   
   
############
### MAIN ###
############
price_cache = defaultdict(lambda: ["0",0])
securities = get_securities_list()
security_updates = []
for security in securities:
    security_updates.append(update_information(security))
print_table(security_updates)
    
# EOF
