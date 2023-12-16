import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B06Y1MP2PY&pd_rd_w=zLoN1&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=T6XM1MA510W3YAR71YZ2&pd_rd_wg=T8pvu&pd_rd_r=fe1f4ce7-1ba6-4c35-a734-75e622a5ea66&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)