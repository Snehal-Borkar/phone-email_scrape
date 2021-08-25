# from requests_html import HTMLSession
# import requests
import bs4
import re
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage





def get_phone(soup):
    soup=str(soup)   
    phone = re.findall(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$', soup)
    phone1= re.findall(r'\d{2}-\d{8}', soup)   
    phone.extend(phone1)
    phone2= re.findall(r'\d{3}-\d{4}-\d{3}', soup)
    phone.extend(phone2)
    phone3 = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', soup)
    phone.extend(phone3)
    if phone:
        return phone
    else:
        print ('Phone not found')
        phone = ''
        return phone
    

        
def get_email(soup):

    email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',soup.text)
    if email:
        return email
    else:
        print ('Email not found')
        email = ''
        return email
        
class Client(QWebEnginePage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)

        self.html=""
        self.loadFinished.connect(self.on_page_load)

        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.html=self.toHtml(self.Callable)
        # print("In on_page_load \n \t HTML: ",self.html)

    def Callable(self,html_str):
        # print("In Callable \n \t HTML_STR: ",len(html_str))
        self.html=html_str
        # print("In Callable \n \t HTML_STR: ",len(self.html))
        self.app.quit()

print("Enter URL")
url = str(input())

#"https://randommer.io/Phone""https://ccctechcenter.org/about/accessibility"
response= Client(url)
# response=requests.get(url)
soup = bs4.BeautifulSoup(response.html, 'html.parser')
# print(soup.prettify() )

# session= HTMLSession()     #parsing html fter running javascript can be done using requests_html
# r=session.get(url) 
# r.html.render() 
# soup=r.html.html 
# print(soup)
# print(type(soup))
email = get_email(soup)
phone = get_phone(soup)
 

print("Phone: ",phone)
print("Email: ",email)