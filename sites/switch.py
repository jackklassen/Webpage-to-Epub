#this stores the functions that apply the apropiate function based on website that is being scrapped.
from marxists import  *

def getchapterlist(url):
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_getchapterlist(url)


def gettitle(url): #extend for all websites we account for
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_gettitle(url)
    
    
def getbody(url):
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_body(url)

def getauthor(url):
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_getauthorname(url)

