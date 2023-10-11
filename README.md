
# Automated Amazon Price Tracker
### Step 1 - Use BeautifulSoup to Scrape the Product Price
 1. Find a product on Amazon that you want to track and get the product URL or just use the one I'm tracking.

https://www.amazon.com/Apple-MacBook-Pro-Early-2023/dp/B0C531YZH8/ref=sr_1_5?crid=1XIOIRK1VDB0C&keywords=macbook&qid=1696972734&sprefix=amazon+macbook%2Caps%2C221&sr=8-5

In addition to the URL, when your browser tries to load up a page in Amazon, it also passes a bunch of other information. e.g. Which browser you're using, which computer you have etc.

These additional pieces of information are passed along in the request Headers.

You can see your browser headers by going to this website:

http://myhttpheader.com/

2. Use the requests library to request the HTML page of the Amazon product using the URL you got from 1.

HINT 1: You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.


HINT 2: Remember this is how you pass headers with the requests library:

https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method

HINT 3: Print the output of the get request and make sure the actual HTML of the web page is printed, if not try adding more items from your header from hint1. Sometimes, Amazon might just return the Captcha page.


3. Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml" parser instead of the "html.parser" for this to work.



HINT: If you get an error that says "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser." Then it means you're not using the right parser, you'll need to import lxml at the top and install the module then use "lxml" instead of "html.parser" when you make soup.



4. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.

HINT: You might need to use the split() method: https://www.w3schools.com/python/ref_string_split.asp

### Step 2 - Email Alert When Price Below Preset Value
We want to get an email when the price of our product is below a certain value. e.g in the case of the Instant Pot, we'll set the target price as $100.

1. So when the price is below 100 then use the smtp module to send an email to yourself. In the email, include the title of the product, the current price and a link to buy the product.

e.g.


HINT: You can test the email by changing the target price to above the current live price of the product, e.g. $200.





NOTE: If you have issues and keep getting this error:


1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"





Below are steps specific to users sending email from Gmail and Yahoo addresses as outlined in the Birthday Wisher on Day 32.


2. Turn on 2-Step Verification for your email under the Security settings for your account. For example, Manage Your Google Account -> Security.


3. Add an App Password under your email settings. Select "Other" from the drop-down settings and choose a password. Use this app password in your Python code.


4. Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587)
