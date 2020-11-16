import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 


my_url = 'https://www.amazon.com/s?k=iphone+8+cases&ref=nb_sb_noss_2'

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

page_soup.h1