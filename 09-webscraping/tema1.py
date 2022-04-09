from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

iter = 0
dfmaster = pd.DataFrame()
for jj in range(20, 27, 1):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{jj}-ianuarie-ora-13-00/")
    try:
        table = browser.find_element(by=By.CLASS_NAME, value="entry-content")
        table_text = table.text
        lista = table_text.split('\n')
        lista_index_start = [i for i, w in enumerate(lista) if 'Nr. crt.' in w]
        lista_index_final = [i for i, w in enumerate(lista) if '43.' in w]
        lista = lista[lista_index_start[0]:lista_index_final[0]:1]
        header_text_str = lista[0]
        header_text = re.findall('[A-Z][^A-Z]*', header_text_str)
        lista = lista[1::1]
        lista1 = []

        for k in lista:
            j = k.split(' ')
            for x in j:
                lista1.append(x)
        lista1.remove("Mare")
        lista1.remove("Mun.")


        dictionar = {i : [] for i in header_text}
        for j in range(0, len(header_text)):
            for i in range(int(j), len(lista1), len(header_text)):
                # print(lista[i])
                dictionar[header_text[int(j)]].append(lista1[i])
        df = pd.DataFrame(dictionar)
        # print(df.iloc[:, [0, 1, 2]])
        if iter ==0:
            df_to_copy = df.iloc[:, [0, 1, 3]]
            df_to_copy.columns.values[2] = f"{jj} ianuarie"
        else:
            df_to_copy = df.iloc[:, [3]]
            df_to_copy.columns.values[0] = f"{jj} ianuarie"
        dfmaster = pd.concat([dfmaster, df_to_copy], axis = 1)
    except Exception:
        pass
    iter +=1
    browser.close()

dfmaster.to_csv('Raportare7zile.csv')

print(dfmaster)



