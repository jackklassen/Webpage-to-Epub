from bs4 import BeautifulSoup
import requests

def m_getsinglepage(url): #maybe inseted of get the data and return it just send this info to the epub packeger directlly.

    page = requests.get(websiteurl)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('title')

    title_text = title.get_text()
    
    author_name = m_getauthorname(url)

    body = soup.find('body')
    
    print(title_text)
    print(author_name)
    #print(body.prettify())



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
    
    
#also include get author collection