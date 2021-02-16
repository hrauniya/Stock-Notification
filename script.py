
import time
import requests
from bs4 import BeautifulSoup
import smtplib


def checkpriceofstock():

    webaccess=requests.get("https://finance.yahoo.com/quote/TSLA/")
    websource= webaccess.content
    soup= BeautifulSoup(websource,"lxml")
    priceofstockstring= soup.find(attrs={"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text()
    convertedprice= float(priceofstockstring.replace(",",""))
    if(convertedprice<1500):
        sendemail()




def sendemail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('senderemailaddress',"password")
    subject="ACTION needed with your stock:TSLA Stock Price has exceeded $1500"
    body="Check Yahoo Finance TSLA link for more information:https://finance.yahoo.com/quote/TSLA?p=TSLA"
    emailmessage= f"Subject:{subject}\n\n{body}"
    server.sendmail('senderemailaddress','recieveremailaddress',emailmessage)
    print("Your email has been sent")
    server.quit()

while (True):
    checkpriceofstock()
    time.sleep(86400)
