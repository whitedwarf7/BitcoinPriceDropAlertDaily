import urllib
import requests
from bs4 import BeautifulSoup
import smtplib

query = 'bitcoin price in inr'
query = query.replace(' ', '+')
urls = f"http://google.com/search?q={query}"
res = requests.get(urls)
soup = BeautifulSoup(res.text,"html.parser")
mydivs = soup.findAll("div", {"class": "BNeawe iBp4i AP7Wnd"})
price = ""
stri = mydivs[0].text[:9]
for character in stri:
    if character.isalnum():
        price += character
integer_price= int(price)

gmail_user = 'gmail address'
gmail_password = 'password'


#email properties
sent_from = gmail_user
to = ['email address']
subject = "Alert for reduced in price"
email_text = f"Alert for reduced in price {integer_price}"

if integer_price < 600000:
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except Exception as e:
        print(e)
        print ('Something went wrong...')
