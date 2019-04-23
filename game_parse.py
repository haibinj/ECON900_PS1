import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import re

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("output/gamepage*"):
	print("parsing"+ one_file_name)
	f = open(one_file_name,"r")
	soup = BeautifulSoup(f.read(),'html.parser')
	f.close
	# find table
	game_table = soup.find("table", {"id": "collectionitems"})
	# find rows
	game_rows = game_table.find_all("tr",{"id":"row_"})
	for r in game_rows:
		game_rank  = r.find("td",{"class":"collection_rank"}).text
		#print(game_rank)
		game_name = r.find("td", {"class":"collection_objectname"}).find('a').text
		#print(game_name)
		game_geek_rating = r.find("td",{"class":"collection_bggrating"}).text
		#print(game_geek_rating)
		game_avg_rating = r.findNext("td",{"class":"collection_bggrating"}).findNext("td",{"class":"collection_bggrating"}).text
		#print(game_avg_rating)
		game_voting = r.findNext("td",{"class":"collection_bggrating"}).findNext("td",{"class":"collection_bggrating"}).findNext("td",{"class":"collection_bggrating"}).text
		#print(game_avg_rating)
		game_year = r.find("span",{"class":"smallerfont dull"})		
		#print(game_year)
		game_price_find = r.find("div",text = re.compile('List:'))
		
		
		#amazon_price_low = r.find("a",text = re.compile('Lowest Amazon:'))
		#.find_parent("a",text = re.compile('New Amazon:'))
		#print(amazon_price_new)
		#print(amazon_price_low)
		#ios_price = r.find("td",{"class":"collection_shop"}.findNext("div",{"class":"aad"}) text = re.compile('iOS App:'))
		#print(ios_price)

		# game_price_sibling = r.find_all("div")
		# game_price = game_price_sibling[2].text
		#print(game_price_find)
		df = df.append({
			'rank':game_rank,
			'name':game_name,
			'geek_rating':game_geek_rating,
			'avg_rating':game_avg_rating,
			'voting': game_voting,
			'price': game_price_find,
			'year':game_year,
			} ,ignore_index=True)

print(df)
df.to_csv("parsed_files/games.csv")