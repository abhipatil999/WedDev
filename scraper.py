import requests
from bs4 import BeautifulSoup
  
# Web URL
Web_url = "https://www.geeksforgeeks.org/transparent-window-in-tkinter/"
  
# Get URL Content
r = requests.get(Web_url)
  
# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())