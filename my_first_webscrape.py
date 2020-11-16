import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

# website url for scraping
my_url = 'https://www.stillwhite.com/backless-wedding-dresses?size=4&size=6&price=0-1500&back=1&page=1&listing=199026'

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs heach product
containers = page_soup.findAll("li", {"data-page":"1"})

# initiate .csv file open and write
filename = "products.csv"
f = open(filename, "w")
headers = "brand, price, size, percent_savings, item_link\n"
f.write(headers)
 
for container in containers:
    #
    title_container = container.findAll("div",{"class":"item-title-heading"})
    brand_name = title_container[0].text
    #
    price_container = container.findAll("div",{"class":"item-title-price"})
    item_price = price_container[0].text
    #
    size_container = container.findAll("small",{"class":"text-muted"}) 
    item_size = size_container[0].text.strip()
    for i in range(6):
        size_value = item_size[i]
        i += 1
    #    
    percentage_savings = item_size[-3:]
    percent_comparison = "%"
    if percentage_savings[-1] != "%":
        percentage_savings = "N/A"
    #
    link_container = container.a.text
    link_container_test = container.a["href"]
    #
    f.write(brand_name + "," + item_price.replace(",","'") + "," + size_value + "," + percentage_savings + "," + "https://www.stillwhite.com/" + link_container_test + "\n")
    
f.close()
print("Check products.csv folder in direcotry for latest scrape!")

# pronto testing kit
"""
print("brand: " + brand_name)
print("price: " +item_price)
print("size: " + size_value)
print("percent. savings: " + percentage_savings)
print("https://www.stillwhite.com/" + link_container_test)
"""
