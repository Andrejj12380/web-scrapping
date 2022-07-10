# coding=utf-8
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Экология']

main_url = 'https://habr.com'
url = main_url + '/ru/all/'
headers = Headers(browser="chrome",  os="win",   headers=True).generate()

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, features = 'html.parser')

articles = soup.find_all('article')

for article in articles:
	hubs = article.find_all(class_='tm-article-snippet__hubs-item')
	hubs = [hub.find('span').text for hub in hubs]
	for hub in hubs:
		if hub.lower() in [word.lower() for word in KEYWORDS]:
			time = article.find_all('time')[0].attrs['title']
			title = article.find_all(class_='tm-article-snippet__title tm-article-snippet__title_h2')
			title = [name.find('span').text  for name in title][0]
			href = main_url + article.find(class_="tm-article-snippet__title-link").attrs['href']
			print(f'<{time}> --- <{title}> --- <{href}>')