import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.binance.com/en/support/sections/115000106672'

response2 = requests.get(url)
soup2 = BeautifulSoup(response2.text, 'html.parser')
news2 = soup2.text
    
while True:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.text

    time.sleep(15)
    
    if news == news2:
        print("....")
    else:
        print("updated")
    break

