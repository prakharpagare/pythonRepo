import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
subtexts = soup.select('.subtext')

for idx, link in enumerate(links):
	title = link.getText()
	href = link.get('href',None)
	vote = subtexts[idx].select('.score')
	if len(vote):
		points = int(vote[0].getText().replace(' points', ''))
		if points > 99:
			print(f"{title} {href} {points}")
