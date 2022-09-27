from email import message
from itertools import count
from sys import flags
from tokenize import Double
import urllib.request
import bs4
import smtplib
import time

pricelsit=[]

def checkprice():
    url="https://www.flipkart.com/apple-2022-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly33hn-a/p/itm48f8f11263927?pid=COMGFB2GMCRXZG85&lid=LSTCOMGFB2GMCRXZG859PGKWX&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_2&otracker=browse&iid=25d4324c-6792-46af-8c60-15565e112060.COMGFB2GMCRXZG85.SEARCH&ssid=9stt9gnnls0000001663351076184"

    sauce=urllib.request.urlopen(url).read()
    soup=bs4.BeautifulSoup(sauce,"html.parser")
    price=soup.find(class_="_30jeq3 _16Jk6d").get_text()
    price= float(price.replace(",","").replace("₹",""))
    pricelsit.append(price)
    return price



def send_email(message):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("amitkunaratk3@gmail.com", "owqtsbfbgjeqybph")
    s.sendmail("amitkunaratk3@gmail.com","amitatk03@gmail.com", message)
    s.quit()

def pricedec(pricel_list):
    if pricelsit[-1]<pricelsit[-2]:
        return True
    else:
        return False
c=1
while True:
    curntprice=checkprice()
    if c>1:  
        flag =pricedec(pricelsit)
        if flag:
         decrease=pricelsit[-1] - pricelsit[-2]
         message="The Price is decreased by {decrease}."
         send_email(message) 
    time.sleep(3000)
    c+=1
