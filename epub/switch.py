#this stores the functions that apply the apropiate function based on website that is being scrapped.
from marxists import  *
from wikipedia import *
from ao3 import *

def getchapterlist(url):
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_getchapterlist(url)
    if site == 'en.wikipedia.org':
        return w_getchapterlist(url)
    if site == 'archiveofourown.org':
        return a_getchapterlist(url)


def gettitle(url): #extend for all websites we account for
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_gettitle(url)
    if site == 'en.wikipedia.org':
        return w_gettitle(url)
    if site == 'archiveofourown.org':
        return a_gettitle(url)
    
def getchaptertitle(url): #extend for all websites we account for
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_getchaptertitle(url)
    if site == 'en.wikipedia.org':
        return w_getchaptertitle(url)
    if site == 'archiveofourown.org':
        return a_getchaptertitle(url)    
    
    
def getbody(url):
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_body(url)
    if site == 'en.wikipedia.org':
        return w_body(url)
    if site == 'archiveofourown.org':
        return a_body(url)

def getauthor(url):
    url_split = url.split('/')
    site = url_split[2]
    if site == 'www.marxists.org':
        return m_getauthorname(url)
    if site == 'en.wikipedia.org':
        return w_getauthorname(url)
    if site == 'archiveofourown.org':
        return a_getauthorname(url)

