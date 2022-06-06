from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

url = "https://etherscan.io/txsPending"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})   # I got this line from another post since "uClient = uReq(URL)" and "page_html = uClient.read()" would not work (I beleive that etherscan is attemption to block webscraping or something?)
htmlCode = urlopen(req, timeout=20).read()
print(htmlCode)