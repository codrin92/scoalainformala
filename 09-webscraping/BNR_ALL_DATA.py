# from bs4 import BeautifulSoup
# import requests
#
# r = requests.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
#
# print(r.text)   #Ne va da doar codul neincarcat.

#Vom importa selenium. Nu putem utiliza BS direct

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# caps = options.to_capabilities()

browser = webdriver.Chrome(ChromeDriverManager().install(), service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")

# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")

#Ne vom folosi de id-ul data table din pagina

table = browser.find_element(by =By.XPATH, value = '//*[@id="Data_table"]')     #xpath reprezinta trimiterea pentru table. Se da click dreapta pe ID in html, copy, copy xpath
table_text = table.text
lista = table_text.split('\n')
# print(table_text)

# print(lista)

header_len = browser.find_element(by=By.XPATH, value = '//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}   #List comprehension la dictionare!!!


for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
        # print(lista[i])
        # print(header[int(j)])

# print(dictionar)

df = pd.DataFrame(dictionar)
# df.to_csv('BNR_ALL_DATA.xls')
df.to_csv('BNR_ALL_DATA.csv')

# print(header)
browser.close()


