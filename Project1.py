#Question: Which Tech Sector in the US has the highest average market cap?
#Project 1 CSE 8A - Eason Wei
#Data Set: Top US Tech Companies.csv 
#Help from Copilot
import csv
data = list(csv.reader(open("Top US Tech Companies.csv")))
sector = ''
sector_dictionary = {} # total market cap per sector
sector_dictionary2 = {} # no. of companies per sector 
sector_dictionary3 = {} # average market cap per sector

def print_long_names(names):
	# Your code here
	for name in names:
		if len(name) > 4:
			print(name)

def sort_companies_by_sector(data):
	#sorts company by sector using a for loop and dictionary. I put range(1,lendata) to skip the header row. Also sum the market cap of each sector in the same time. Killing 2 Birds w One Stone
	for i in range(1,len(data)):
		sector = (data[i][2])
		if sector not in sector_dictionary:
			sector_dictionary[sector] = 0.0
			sector_dictionary2[sector] = 0
			sector_dictionary[sector] += float(data[i][6])
			sector_dictionary2[sector] += 1
		#sector_dictionary[sector].append(data[i][0])
		else:
			sector_dictionary[sector] += float(data[i][6])
			sector_dictionary2[sector] += 1
	#print (sector_dictionary, sector_dictionary2)


def find_average_market_caps(sector_dictionary, sector_dictionary2):
#finds the average market cap of each sector by dividing the total market cap by the number of companies in that sector. 
	for sector in sector_dictionary:
		sector_dictionary3[sector] = 0.0
		sector_dictionary3[sector] = sector_dictionary[sector] / sector_dictionary2[sector]

def print_sector_ranking(sector_dictionary3):
	for position, sector in enumerate(sorted(sector_dictionary3, key=sector_dictionary3.get, reverse=True), start=1):
		print(f"{position}. {sector}: {sector_dictionary3[sector]:.3g} trillion")

sort_companies_by_sector(data)
find_average_market_caps(sector_dictionary, sector_dictionary2)
print_sector_ranking(sector_dictionary3)