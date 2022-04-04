from bs4 import BeautifulSoup

import requests
import pandas as pd

r=requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")

# print(r)        #Se printeaza statusul paginii. Lista de statusuri https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# print(r.text)   #Se printeaza toata sursa html a paginii

link = BeautifulSoup(r.text, "html.parser")

# print(link)

title=link.find_all('div', attrs={'class':"contentDiv"})  #title accesseaza intregul div. Class content div se ia din codul paginii inspectate in google chrome
# print(title)
dataset = []
for i in title:
    # print(i)  #Afisam randul pentru fiecare element din lista
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            # print(td_index)
            td_list = []  #Lista temporara pt intrarea pe fiecare rnad
            if td_index.find_all('th'):
                header = [th_index.get_text() for th_index in td_index.find_all('th')]  #Get text este o metoda prin care preluam textul
            for index, td_value in enumerate(td_index.find_all('td')):
                print(index, td_value)
                if index == 0:
                    td_list.append(td_value.get_text())
                else:
                    td_list.append(float(td_value.get_text().replace(',','.')))
            dataset.append(td_list)
# print(header)
print(dataset)

df = pd.DataFrame(dataset, columns = header)
df.to_csv("CursBNR.csv", header = header)

