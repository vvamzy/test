import bs4
import requests
from bs4 import *

x = input("Enter month: ")
y = input("Enter date: ")

res = requests.get(f"https://en.wikipedia.org/wiki/{x}_{y}")
soup = bs4.BeautifulSoup(res.text,"lxml")
soup_title = soup.select('title')
print(soup_title)
