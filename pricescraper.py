# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.nasdaq.com/symbol/aapl'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# get the index name
'''name_box = soup.find('div', attrs={'id':'qwidget-pageheader'})
name = name_box.text
print name'''

# get the index price
price_box = soup.find('div', attrs={'class':'qwidget-dollar'})
price = price_box.text
print price