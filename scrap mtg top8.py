import requests
from bs4 import BeautifulSoup



def deck():
    commander="The Gitrog Monster"

    url="https://mtgtop8.com/format?f=EDH"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())


    for link in soup.find_all("a"):
    #    inner_text="{}".format(link.text)


        if "{}".format(link.text)==commander:
            print("{}".format(link.text))
            print("{}".format(link.get("href")))
            url="{}".format(link.get("href"))


    url="https://mtgtop8.com/"+url

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    compteur=0

    for link in soup.find_all("a"):

        if "{}".format(link.text)==commander:
                
            if compteur==1:
                
                print("https://mtgtop8.com/{}".format(link.get("href")))

            compteur=1



def tournoi():
    url="https://mtgtop8.com/format?f=EDH"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())


    for link in soup.find_all("a"):
    #    inner_text="{}".format(link.text)

        if "event" in "{}".format(link.get("href")):
            
            return("Le dernier gros tournoi :\nhttps://mtgtop8.com/{}".format(link.get("href")))
