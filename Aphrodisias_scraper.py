from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from time import sleep

url_list = ["http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcA.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcB.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcG.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcD.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcE.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcZ.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcH.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcQ.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcI.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcK.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcL.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcM.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcN.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcC.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcO.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcP.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcR.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcS.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcT.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcU.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcF.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcW.html",
        "http://insaph.kcl.ac.uk/iaph2007/inscriptions/indices/aphrodisian/aphrodisian-grcX.html"]

names = []

for url in url_list:
    """
    Load content from URL.
    Set BeautifulSoup to use the content.
    Find all <dd> tags on the site, which contain the names and references.
    """
    url = requests.get(url).text
    soup = bs(url, "html5lib")
    result = soup.find_all("dd")

    str_result = str(result)

    for item in str_result.split(","):    
        """ 
        Use BeautifulSoup to search through each name individually.
        Get the text contained within the <dd> tags and its children.
        Split the name and reference at the space to make individual records.
        Append the name and reference to the "names" list.
        """
        soup = bs(item)
        text = soup.get_text()    
        name = text.rsplit(" ", 1)[0]    
        reference = text.rsplit(" ", 1)[1]    
        names.append([name, reference])
        
    sleep(10)

names = pd.DataFrame.from_records(names)

with open("c:/users/cory taylor/dropbox/aphrodisias/names.csv", "w") as csv_out:
    names.to_csv(csv_out, encoding="utf-8")