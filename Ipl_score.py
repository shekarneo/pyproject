from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

url = 'https://www.news18.com/cricketnext/series/ipl-2019/points-table.html'
page = requests.get(url)
pagetext = page.text
soup = BeautifulSoup(pagetext, 'html.parser')


header = ['Team', 'Matches', 'Won', 'Lost', 'Tied', 'NR', 'Points', 'NRR']

data1= []

for row in soup.find_all('table',{'class':'full-pnttbl vsp10'}):
    for col in row.find_all('td'):
        data1.append(col.text)

data = [data1[i * n:(i+1) * n] for i in range(0,n)]
rank = 1,2,3,4,5,6,7,8
df = pd.DataFrame(data, columns= header, index= rank)
