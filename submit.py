import requests
from bs4 import BeautifulSoup

def Get_Text(URL):
    req=requests.get(URL)
    src=req.content
    soup=BeautifulSoup(src,'html.parser')
    text=soup.get_text(strip=True,separator='\n')
    return text

Lovecraft_text=Get_Text('https://www.hplovecraft.com/writings/texts/fiction/bws.aspx')
Lovecraft_text=Lovecraft_text[:Lovecraft_text.find('Return to “Beyond the Wall of Sleep”')]
Austin_text=Get_Text('https://www.gutenberg.org/files/1342/1342-h/1342-h.htm')
Austin_text=Austin_text[Austin_text.find("Chapter 61"):]
# Text Cleaning
# Beyond the Wall of Sleep, By H. P. Lovecraft
Lovecraft_text_cleaning=Lovecraft_text
# Remove punctuation marks
punctuations="!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
Lovecraft_text_cleaning="".join([i.lower() for i in Lovecraft_text_cleaning if i not in punctuations])
#convert the string into list
Lovecraft_text_cleaning=Lovecraft_text_cleaning.split()
stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
#Remove stop words
Lovecraft_text_cleaning=[i for i in Lovecraft_text_cleaning if i not in stop_words ]
#Remove numbers
Lovecraft_text_cleaning=[i for i in Lovecraft_text_cleaning if not  i.isdigit()]
#Pride and Prejudice, by Jane Austen
Austin_text_cleaning=Austin_text
#Remove punctuation marks
Austin_text_cleaning="".join([i.lower() for i in Austin_text_cleaning if i not in punctuations])
#convert the string into list
Austin_text_cleaning=Austin_text_cleaning.split()
#Remove stop words
Austin_text_cleaning=[i for i in Austin_text_cleaning if i not in stop_words]
#Remove numbers
Austin_text_cleaning=[i for i in Austin_text_cleaning if not  i.isdigit()]
print("The common words between those two books are: \n \n ",set(Austin_text_cleaning) & set(Lovecraft_text_cleaning),"\n")
print("The number of common words between those two books is: \n",len(set(Austin_text_cleaning) & set(Lovecraft_text_cleaning)))




