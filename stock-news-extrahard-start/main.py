import requests
import html
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_email = 'Insert your email'
password = 'Insert your password'

##### --------------------------- FUNCTIONS --------------------------- #####
def daily_list(days):
    daily_closed_list = []
    for day in days:
        daily_closed_value = stock_data["Time Series (Daily)"][f"{day}"]['4. close']
        daily_closed_list.append(float(daily_closed_value))
    return daily_closed_list
def percentual_change(vcera, zavcera):
    procent = round(((vcera-zavcera)/zavcera)*100,2)
    if procent >= 5 or procent <=-5:
        predmet = f"Tesla {procent}%"
    return predmet
def send_email(subject,letter):
    global my_email,password
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='butevski_@hotmail.com',
                            msg=f'Subject: {subject}!\n\n {letter} !' )



STOCK_API_KEY = 'Insert your stock api key'
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
response = requests.get(url='https://www.alphavantage.co/query', params = parameters)
response.raise_for_status()
stock_data = response.json()

### Making a list of closed day values
days = stock_data['Time Series (Daily)']
daily_prices = daily_list(days)
vcera = daily_prices[0]
zavcera = daily_prices[1]

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
predmet = percentual_change(vcera,zavcera)


NEWS_API_KEY = 'Insert your news api key'
parameters1 = {
    'q':'tesla',
    'from': '2021-12-24',
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}

response1 = requests.get(url='https://newsapi.org/v2/everything', params =parameters1)
response1.raise_for_status()
news_data = response1.json()['articles'][0:3]

letter_1 = f"Headline: {news_data[0]['title']}\n\nBrief: {news_data[0]['description']}"
letter_2 = f"Headline: {news_data[1]['title']}\n\nBrief: {news_data[1]['description']}"
letter_3 = f"Headline: {news_data[2]['title']}\n\nBrief: {news_data[2]['description']}"

LETTER = f"LETTER 1: \n{letter_1}\n\n LETTER 2: \n{letter_2}\n\nLETTER 3: \n{letter_3}"



# Send a seperate message with the percentage change and each article's title and description to your phone number. 
send_email(subject=predmet, letter=letter_1)




