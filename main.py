import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Apple-MacBook-Pro-Early-2023/dp/B0C531YZH8/ref=sr_1_5?crid=1XIOIRK1VDB0C&keywords=macbook&qid=1696972734&sprefix=amazon+macbook%2Caps%2C221&sr=8-5"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
print(price)
price_without_currency = price.split("$")[1]
price_without_currency = price_without_currency.split(".00")
price_without_currency = price_without_currency[0].replace(",", ".")
price_without_currency = float(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 5000.00
YOUR_SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = "muhammedcubukcu0@gmail.com"
PASSWORD = ""
if price_without_currency < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )