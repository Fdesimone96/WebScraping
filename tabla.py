# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver

import pandas as pd
import time



options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')



site = 'https://www.ligaprofesional.ar/torneo-primera-lpf/' 

wd = webdriver.Chrome('chromedriver',options=options)
wd.get(site)
time.sleep(3)

html = wd.page_source

df = pd.read_html(html)

##print(df[25])

Row_list =[]
Row_list = df[32]
print(Row_list)
Row_list.to_csv('tablaPos.csv')

## Esta parte modifica el archivo para pasarlo a HTML
df = pd.read_csv("tablaPos.csv", index_col=False)
df =  df.drop("Unnamed: 0",axis=1)
df =  df.to_html(escape=False,index=False)


df=df.replace('<th>','<th class = "th-sm" style="text-align: left">').replace('class="dataframe"','class="display"')
msgxx ='''
<link rel="stylesheet" type="text/css" href="estiloTabla.css"/>
'''
df = msgxx + df
df=df.replace('<th>','<th class = "th-sm"') 
##print(df)
filename = 'abc.html'
f= open(filename, 'w+')
f.write(df)
f.close()

