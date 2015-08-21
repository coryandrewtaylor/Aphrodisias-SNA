from bs4 import BeautifulSoup as bs
import requests
from time import sleep
import codecs

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

headwords = ""

for url in url_list:
    """
    Load content from URL.
    Set BeautifulSoup to use the content.
    Find all <dd> tags on the site, which contain the names and references.
    """
    url = requests.get(url).text
    soup = bs(url, "html5lib")
    result = soup.find_all("dt")

    str_result = str(result)

    for item in str_result.split(","):    
        """ 
        Use BeautifulSoup to search through each name individually.
        Get the headwords contained within the <dt> tags.
        Append the name to the "names" list.
        """
        soup = bs(item)
        text = soup.get_text()       
        headwords = headwords + "\r\n" + text
        
    sleep(10)

with codecs.open("c:/users/cory taylor/dropbox/aphrodisias/headwords.txt", "w", 
                encoding="utf-8") as txt_out:
    txt_out.seek(0)
    txt_out.write(headwords)