import requests
from bs4 import BeautifulSoup

url = "https://pythonjobs.github.io/"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
#print (soup)

results = soup.find(class_="job_list")

#print (results)

jobs = results.find_all('h1')

links = results.find_all('a')
for links in links:
	print (links['href'])

towns = results.find_all('span',class_="info")
for town in towns:
	print(town.text)