import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import re
import time
import os
import logging

logging.basicConfig(
    format="{asctime} - {levelname}: {message}",
    style = "{",
    level=logging.DEBUG,
    datefmt="%d/%m/%Y %H:%M"
)

HEADERS = {       
    # "Header Name": program_name/Version number extra comment. Need this to prevent some rate limiting                             
    "User-Agent": "BlockImage/1.0 (block project)" # 
}

session = requests.Session()
session.headers.update(HEADERS)

BASE_URL = "https://crystalrealms.wiki.gg/" # Base website url
BLOCKS_URL = "https://crystalrealms.wiki.gg/wiki/Blocks" # Page with all blocks listed


blocks_main_response = session.get(BLOCKS_URL) # The downloaded page

if blocks_main_response.status_code != 200:
    print(f"Failed to download page: {blocks_main_response.status_code}")
    exit()

time.sleep(2)
print("Waiting 2 seconds to prevent rate limiting or IP ban.")
blocks_page_html = blocks_main_response.text # Turned into ONLY HTML text now
blocks_soup = BS(blocks_page_html, "html.parser")



SIZE_FOLDERS = {
    "1x1": "1x1",
    "2x2": "2x2",
    "1x3": "1x3",
    "2x1": "2x1",
    "1x2": "1x2",
    "2x4": "2x4",
    "3x2": "3x2",
    "3x3": "3x3",
    "2x3": "2x3",
    "4x4": "4x4",
    "4x3": "4x3",
    "5x4": "5x4"
}

   # print(blocks_page_html.status_code)
    #print(blocks_page_html.url)
    #print(blocks_page_html.text[:500])


item_count = 0

for img in blocks_soup("img", class_="pixel-image"):        # Check all a tags for the right one that has (class="image")
                                                            # in the <img>. There are many other images so thats why we check
                                                            # from what i saw, only the main image of the page has (class="image").
    item_count += 1

    image_href = img.parent.get("href")                     # Relative link to page of block. <img> tag is contained within a <a> tag so we need to get parent of <img> tag
    image_src = img.get("src")                              # src is the relative link. We then join the base url with this relative link
    image_alt = img.get("alt")                              # alt is the filename so we can properly label our images
    
    image_url = urljoin(BASE_URL, image_src)                # URL containing only the image
    block_page_url = urljoin(BASE_URL, image_href)          # URL containing info of the block



    block_response = session.get(block_page_url)            # The downloaded block page
    print("Sleeping for 2 seconds")
    time.sleep(2)                                           # Sleep for 2 seconds to prevent rate limiting 
    block_page_html = block_response.text                   # Turned into ONLY HTML text now
    single_block_soup = BS(block_page_html, "html.parser")  # Converted into BeautifulSoup Object

    print(block_page_url)                                  
    print(block_page_html[:160])                        
    size = single_block_soup.find(                          # Div containing "druid-data-Size" which contains the size of the image
        "div",
        class_="druid-data-Size"
    )

    if size is None:
        print("No size:", image_alt)
        continue

    size = size.get_text(strip=True)

    folder = SIZE_FOLDERS.get(size)

    if folder is None:
        print("Unknown size:", size)
        continue




    image_response = session.get(image_url)
    time.sleep(2)
    print("Waiting 0.2 seconds to prevent rate limiting or IP ban. image_response")

    filepath = f"../assets/blocks/{folder}/{image_alt}.png"
    
    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )

    if os.path.exists(filepath):
        print(f"{image_alt} already exists.")

    else:    
        with open(filepath, "wb") as f:
            f.write(image_response.content)

        print(f"Saved {image_alt}")
    
    print(image_alt, image_src, image_url)
    print(item_count)

print(item_count)