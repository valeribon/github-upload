#! /usr/bin/env python3

import webbrowser, requests, bs4

def getEbayprice(productUrl):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    print ('The price is: ' + elems[0].text.strip())

url = 'https://www.ebay.com/itm/KitchenAid-Refurbished-5-Speed-Classic-Blender-RKSB1570/123896072608?_trkparms=pageci%3Abe19edf8-81dc-11ea-aba1-1633f81aff9a%7Cparentrq%3A900aeb991710a4b77ccd2ff8ffdc1b6d%7Ciid%3A1'

getEbayprice(url)
