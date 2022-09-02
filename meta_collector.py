import sys
import json
import requests
from bs4 import BeautifulSoup

URL = sys.argv[1]

def getMetaTags(URL):
    # data request info
    response = requests.request('GET', URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    metas = []
  
    for tag in soup.find_all("meta"):
        meta = {"name": tag.get('name'), "content": tag.get('content')}
        if meta['name'] is not None and meta['content'] is not None:
            metas.append(meta)
    
    toJson = json.dumps(metas)
    return toJson

# example
print(getMetaTags(URL))