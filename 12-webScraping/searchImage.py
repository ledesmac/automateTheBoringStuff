#! python3
# searchImage.py - Python program to open Imgur and gather top x search results at once

import bs4, os, requests, sys, webbrowser

os.makedirs('imgur_results', exist_ok=True) 
searchString =' '.join(sys.argv[1:])
print("Searching...")       # display text while downloading the search result page
res = requests.get(f'https://imgur.com/search?q={searchString}')

res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
imgElems = soup.select('.post img')
print(imgElems)

numOpen = min(3, len(imgElems))
for i in range(numOpen):
    imgUrl = 'https:' + imgElems[i].get('src')
    print('Downloading image %s...' % (imgUrl))
    temp_res = requests.get(imgUrl)
    temp_res.raise_for_status()

    imageFile = open(os.path.join('imgur_results', os.path.basename(imgUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()