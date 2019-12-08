import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.bathandbodyworks.com/p/kaleidoscope-ultra-shea-body-cream-024477198.html?cgid=body-cream#sz=48&start=90'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", class_= "product-name").get_text()
    price = soup.find("span", class_="price-sales").get_text()
    converted_price = float(price[1:5])


    if converted_price < 13.5:
        send_mail()
    print(converted_price)
    print(title.strip())

    if converted_price < 1.35:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('balasathya169@gmail.com', 'nzhjwnwbogxmoaps')

    subject = 'Price is down for Kaleidoscope!!!!!'
    body = 'Check bath and body works page : https://www.bathandbodyworks.com/p/kaleidoscope-ultra-shea-body-cream-024477198.html?cgid=body-cream#sz=48&start=90'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'xxxxxxxxxxx@gmail.com',
        'xxxxxxxxxxx@gmail.com',
        msg
    )

    print('Email has been sent!')

    server.quit()

check_price()



