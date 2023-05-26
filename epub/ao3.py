from bs4 import BeautifulSoup
import requests

def a_body(url): 

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    body = soup.find('body')
    
    return body


def a_gettitle(urL):
    page = requests.get(urL)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('title')
    title_text_raw = title.get_text()
    title_text_split = title_text_raw.split('-')
    print(title_text_split[0])
    return title_text_split[0].strip()


def a_getauthorname(urL):
    page = requests.get(urL)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('title')
    title_text_raw = title.get_text()
    title_text_split = title_text_raw.split('-')
    return title_text_split[2].strip()


def a_getchapterlist(url):
    
    url_split = url.split('/')
    site  = (url_split[0] + '/' + url_split[1] +'/' + url_split[2] + '/' + url_split[3] + '/' + url_split[4] + '/' + 'navigate' + '/')
    print(site)
    body = a_body(site) 
    chapter_list = []
    for a in body.find_all('a', href=True):
        if 'chapters' in a['href']:
            chapter_list.append('https://archiveofourown.org' + a['href'])
            

    return chapter_list
               
