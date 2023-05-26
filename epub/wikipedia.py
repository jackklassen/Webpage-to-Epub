from bs4 import BeautifulSoup
import requests


def w_body(url): #maybe inseted of get the data and return it just send this info to the epub packeger directlly.

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    body = soup.find('div',{'id':'bodyContent'})
    return body

def w_gettitle(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('title')
    title_text = title.get_text()
    return title_text

def w_getchaptertitle(url):
    return w_gettitle(url)

def w_getauthorname(url):
    return 'wikipedia'


def w_getchapterlist(url):
    chapter_list = [url]
    
    return chapter_list