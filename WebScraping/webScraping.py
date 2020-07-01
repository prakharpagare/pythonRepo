import requests
from bs4 import BeautifulSoup

res = requests.get("https://timesofindia.indiatimes.com/home/headlines")

soup = BeautifulSoup(res.text, 'html.parser')
headlines = soup.select('.sechead-link')
print(headlines[0].get('href'))