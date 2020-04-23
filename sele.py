from selenium import webdriver

url = 'https://www.ebay.com/itm/KitchenAid-Refurbished-5-Speed-Classic-Blender-RKSB1570/123896072608?_trkparms=pageci%3Abe19edf8-81dc-11ea-aba1-1633f81aff9a%7Cparentrq%3A900aeb991710a4b77ccd2ff8ffdc1b6d%7Ciid%3A1'
browser = webdriver.Chrome()
browser.get(url)
elem = browser.find_element_by_css_selector('#w1-24 > div.addon-row > a > span.addon-link-title')
elem.click()

#busca el search bar
searchElem = browser.find_element_by_css_selector('#gh-ac')
#le manda algo que quieras escribir
searchElem.send_keys('microphone')
#busca el boton de submit y clickea
searchElem.submit()

'''
browser.back()
browser.forward()
browser.refresh()
browser.quit()
'''
