import pandas as pd
import pycountry
import matplotlib.pyplot as plt

description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017', '2018 ', '2019 '
    ])
dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ':']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ','86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ','94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ','93 ', '95 ']),
    ('EC', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ','89 ', '90 ']),   #EA change to EC. EA not recognized
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ','90 ', '90 ']),
    ('GR', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ','76 ', '79 ']),   #EL changed to GR
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ','86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ','94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ','89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ','82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ','83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ','89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ','84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ','78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ','93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ','82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ','74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ','84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ','98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ','96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ','84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ','79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ','81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ','80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ','93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ','87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ','81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
    ('GB', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ','95 ', '96 ']),   #UK Changed to GB
    ('ZW', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ','93 ']),         #XK Changed to ZW
    ]

def dataset_comprehension(head, body):
    header_text = [head[0]]
    for i in head[1]:
        header_text.append(i)

    body_text = []
    for x in body:
        full_name = pycountry.countries.get(alpha_2=x[0]).name
        body_text_temp = [full_name]
        for y in x[1]:
            body_text_temp.append(y)
        body_text.append(body_text_temp)

    dictionar = {i: [] for i in header_text}

    for j in range(0, len(header_text)):
        for i in range(0, len(body_text)):
            dictionar[header_text[int(j)]].append(body_text[i][j])
    df = pd.DataFrame(dictionar)
    df.columns = df.columns.str.replace(' ', '')               #Instructiuni care scot spatiile goale din celule, scot literele din celulele numerice, inlocuiesc : cu 0
    df = df.set_index('Country')
    for u in range(0, df.shape[0]):
        for j in range(0, df.shape[1]):
            df.iloc[u,j]=df.iloc[u,j].strip()
            s = df.iloc[u,j]
            if ' ' in s:
                new_s  = ''.join(ch for ch in s if ch.isdigit())
                df.iloc[u,j] = new_s
            try:
                df.iloc[u,j] = int(df.iloc[u,j])
            except Exception:
                df.iloc[u, j] = None
    return df

def get_year_data(data, year):
    # get_year_dict = dict()
    df = dataset_comprehension(description, data)
    list = []
    for i in df.index:
        tup = (i, df.loc[i, year])
        # tup = (df.iloc[i,0], df.loc[i, year])
        list.append(tup)
    get_year_dict = {year: list}
    return get_year_dict

def get_country_data(data, tara):
    df = dataset_comprehension(description, data)
    list = []
    for i in range(0, len(df.columns)):
        # tup = (df.columns[i], 0)
        tup = (df.columns[i], df.loc[tara, df.columns[i]])
        # tup = (df.columns[i], df.loc[tara, df.columns[i]])
        list.append(tup)
    get_country_dict = {tara: list}
    return get_country_dict

def get_average_country_data(tara):
    df = dataset_comprehension(description, dataset)
    df_to_avg = df.loc[tara]
    medie = df_to_avg.mean(axis = 0, skipna=True)
    return medie

df2=dataset_comprehension(description, dataset)
df3 = df2
mean_list = []
for i in df3.index:
    mean_list.append(get_average_country_data(i))
# print(mean_list)
df3['Mean']=mean_list
print(df3)

df_sorted = df3.sort_values('Mean')
best_2 = df_sorted.tail(2)
print(best_2.index)
print(df2.loc[best_2.index[0]])

# df2.plot(kind = 'scatter', x = df2.loc[best_2.index[0]], y = df2.loc[best_2.index[1]])  #Plotare graph

df5 = pd.concat([df2.loc[best_2.index[0]], df2.loc[best_2.index[1]]], axis = 1)
print(df5)
df6=df5.transpose()
df6.drop('Mean', axis=1, inplace = True)
df6.plot(kind = 'scatter', x = range(0, 110,10), y= df6.columns[0])  #Plotare graph
plt.show()
# df2.loc['Romania'].plot(kind='hist')                     #Plotare histograma
# plt.show()

# df['AT'].plot(kind='hist')                     #Plotare histograma