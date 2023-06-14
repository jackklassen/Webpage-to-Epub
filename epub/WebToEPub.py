
from epuber import *
import sys

import argparse




 
def get_epub(url,location):
    
    # get url from pasted text clean it up and ship it off to make book
    makebook(url,location)


parser = argparse.ArgumentParser(description="cmd verison of the program.")

parser.add_argument("-d", "--download",dest="download" , action="store", type = str )
parser.add_argument("-o", "--output", dest="location" ,action="store",default='', type=str)
args = parser.parse_args()

if args.download:
    get_epub(args.download,args.location);
    