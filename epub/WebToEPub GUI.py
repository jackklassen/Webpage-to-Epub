import eel
from epuber import *
import sys


eel.init("web") 
eel.start('index.html', block = False) 
  
# Exposing the random_python function to javascript
@eel.expose    
def get_epub(url):
    
    # get url from pasted text clean it up and ship it off to make book
    makebook(url)
    
    
  
# Start the index.html file
eel.start("index.html")

#top level does nothing but gets url info/ handles gui and CMD and sends it on its way to the sites and from there to the epub packeger
    


#BeautifulSoup grab Webpage


#Check website against options (if alt-hist point grab webpage at all threadmarks etc)

#make it apply formatting to grabed text

#Turn to EPub and export.