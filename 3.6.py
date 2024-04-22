import requests
import webbrowser
from bs4 import BeautifulSoup
import random

def shuffle():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    site = requests.get(url)
    soupRP = BeautifulSoup(site.text, "html.parser")
    title = soupRP.find("h1", {"id": "firstHeading"}).text
    print(title)

def main():
    notFound = True
    while(notFound):
        shuffle()
        choice = input("czy jesteś zainteresowany artykułem? (y/n)")
        if choice.lower() == 'y':
            notFound = False
            
if __name__ == "__main__":
    main()