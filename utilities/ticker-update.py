import requests
from bs4 import BeautifulSoup 

URL = 'https://finance.yahoo.com/quote/'
securities = ['bgcp', 'cvx', 'f', 'ge', 'intc', 'lumn', 'src', 't']

for security in securities:
   query = URL + security

   page = requests.get(query)
   soup = BeautifulSoup(page.content, 'html.parser')
   span = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
   price = span.get_text()
   table_row = soup.select('table td')
   open = table_row[3].text
   
   print(f"{security:>6}: {open:<6}  {price:<6}")
