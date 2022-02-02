import requests
from bs4 import BeautifulSoup
URL =  "https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQMW44C/ref=sr_1_2?crid=2YH7O9TY27V8&keywords=macbook&qid=1643715923&sprefix=macbook+%2Caps%2C204&sr=8-2"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"


headers = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(url=URL, headers=headers)
website = response.text

soup = BeautifulSoup(website, 'html.parser')
# Scraping the Price
price_string = soup.find_all(name='span', class_='a-offscreen')[0].get_text()
price_float = float(price_string[1:].replace(',',''))
# Scraping the Name and link
title = soup.find_all(name='span', id='productTitle', class_='a-size-large product-title-word-break')[0].get_text().strip()

if price_float < 2500:
    print(f"Product: {title}\nCurrent price: ${price_float} \nLink: {URL}")
    # email could be sent to the user through smtplib library instead of printing



