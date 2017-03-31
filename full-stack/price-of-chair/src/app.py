import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/herman-miller-aeron-office-chair/p230630306")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("strong", {"class":"simpleNowPrice"})
string_price = element.text.strip() #"£899.00"

price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 1000:
    print("You should buy the chair!")
    print("The current price is {}".format(string_price))
else:
    print("Don't buy !!! It's too expensive !!! ")

# <strong class="simpleNowPrice">£899.00</strong>