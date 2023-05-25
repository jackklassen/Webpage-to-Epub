from bs4 import BeautifulSoup
import requests

#split into get author, get title, etc, for 1 page send just body text to epub so main file is now epub
def m_body(url): #maybe inseted of get the data and return it just send this info to the epub packeger directlly.

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    body = soup.find('body')
    
    return body


def m_gettitle(urL):
    page = requests.get(urL)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('title')
    title_text = title.get_text()
    return title_text

def m_getauthorname(url):
    split_url = url.split('/')
    
    #test for possible failures of this method
    author_url = (split_url[0] + '/' + split_url[1] +'/' + split_url[2] + '/' + split_url[3] + '/' + split_url[4] + '/')
    apage = requests.get(author_url)
    asoup = BeautifulSoup(apage.content, "html.parser")

    
    header_list = []
    
    for header in asoup.find_all(["h1","h2","h3"]):
        header_list.append(header)
    
    raw_name = header_list[0].get_text()
    name = raw_name.replace('Archive','') #accomidate all variantions of archive
    return name
    
    
    
def m_getchapterlist(url):
    
    url_split = url.split('/')
    site = url_split[5] #check if the site is an author page.
    body = m_body(url)
    chapter_list = []
    if site == '':
          for a in body.find_all('a', href=True):
              if a['href'] != '../index' and a['href'] != '../../admin/volunteers/steering.htm' and a['href'] != '../../index.htm' and a['href'] != '../index.htm':
                chapter_list.append(url + '/' + a['href'])
          return chapter_list
          #use requsests and soup to grab link urls
    chapter_list.append(url)
    return chapter_list
        

#also include get author collection