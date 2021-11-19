import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSSoup
import ssl

ctx = ssl.create_defualt_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CER_NONE

url = input("Enter - ")
html = urllib.request.openurl(url, context = ctx).read()
soup = BeautifulSoup(html, html.parser)

tegs = soup('a')
for tag in tags:
    print(tag.get('href', None))
