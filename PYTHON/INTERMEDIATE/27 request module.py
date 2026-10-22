import requests
from  bs4 import BeautifulSoup
url="https://www.youtube.com"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
#display all code in fomatted way
for h2 in soup.find_all("h2"):
    print(h2.text)
#print all tags data with <h2>