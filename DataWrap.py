import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r=requests.get(url)
#print (r)

soup = BeautifulSoup(r.text,'lxml')
#print(soup)
table = soup.find("table", class_ ="ih-td-tab auction-tbl")

title = table.find_all("th")
print(title)
#print(table)

header = []
for i in title:
  name = i.text
  header.append(name)

df= pd.DataFrame(columns=header)
print(df)

row=table.find_all("tr")
#print(row)
for i in row[1:]:
  first_td = i.find_all("td")[0].find("div", class_ ="ih-pt-ic").text.strip()
  data = i.find_all("td")[1:]
  row = [tr.text for tr in data]
  #print(row)
  row.insert(0,first_td)
  l=len(df)
  df.loc[l]=row

print(df)

df.to_csv("ipl Auction Stats.csv")
