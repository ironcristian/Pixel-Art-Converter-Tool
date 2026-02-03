import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import re
import time
import os

headers = {                                        #
    "User-Agent": "BlockImage/1.0 (block project)"
}

session = requests.Session()
session.headers.update(headers)

website_url = "https://crystalrealms.wiki.gg/" # Base website url

# Page with links to all blocks information
Blocks_page_URL = "https://crystalrealms.wiki.gg/wiki/Blocks" # The url
blocks_page_html = session.get(Blocks_page_URL) # The downloaded page
img_tags_blocks_url_html = blocks_page_html.text # Turned into ONLY HTML text now
img_tags_blocks = BS(img_tags_blocks_url_html, "html.parser") 



header = {
    "User-Agent": "BlockImage/1.0 (block project)"
}


for img in img_tags_blocks("img", class_="pixel-image"):  # Check all a tags for the right one that has (class="image")
                                                          # in the <img>. There are many other images so thats why we check
                                                          # from what i saw, only the main image of the page has (class="image").

    image_src = img.get("src")                            # src is the relative link. We then join the base url with this relative link
    image_alt = img.get("alt")                            # alt is the filename so we can properly label our images
    
    fullurl = urljoin(website_url, image_src)             # joins base url and relative url (image_src)

    image = session.get(fullurl)
    filepath = f"../assets/blocks/{image_alt}.png"
    
    if os.path.exists(filepath):
        print(f"{image_alt} already exists.")
    else:    
        with open(f"../assets/blocks/{image_alt}.png", "wb") as f:
            f.write(image.content)
    
    print(image_alt, image_src, fullurl)