# -*- coding: utf-8 -*-
"""COVID-Scrapping-project-3pm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V2GAk7FOtvLes_j9cu1xIo1ij9SB2RKP
"""

# !pip install beautifulsoup4
# !pip install requests
from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
print(soup)
print(soup.text)

code = BeautifulSoup(soup.text, "lxml")
code

table_code = code.table
table_code

tags = table_code.find_all('tr')
tags

raw_data = []
for tag in tags:
  x = tag.text
  y = x.split('\n')[1:-1]
  if y[0] != '':
    raw_data.append(y)

print(raw_data)

import csv
with open('covid.csv','w') as file:
  x = csv.writer(file)
  for i in raw_data:
    x.writerow(i)

import pandas as pd
df = pd.read_csv('/content/covid.csv',encoding = 'ISO-8859-1')
df

country = list(df['Country,Other'][0:5])
TotalCases = list(df['TotalCases'][0:5])
new_Total_cases = []
for TotalCase in TotalCases:
  x = TotalCase.replace(',','')
  new_Total_cases.append(int(x))

new_Total_cases

import plotly.graph_objects as go
fig = go.Figure(data=[go.Pie(labels=country, values=new_Total_cases)])
fig.show()

import plotly.graph_objects as go

fig = go.Figure([go.Bar(x=country, y=new_Total_cases)])
fig.show()

