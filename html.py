import urllib2
from bs4 import BeautifulSoup


page = urllib2.urlopen('http://www.google.de/')

soup = BeautifulSoup(page)
#print(soup)

print(soup.title)
for link in soup.find_all('a'):
    print(link.get('href'))