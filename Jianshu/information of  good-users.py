import requests,os
from bs4 import BeatifulSoup

os.chdir(os.getcwd())
def write():
    with open('Information.txt','a') as f:
        f.write(information+'\r\n')
