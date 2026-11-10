import csv
data = list(csv.reader(open("Top US Tech Companies.csv")))
sector = ''
sector_dictionary = {} # total market cap per sector
sector_dictionary2 = {} # no. of companies per sector 
sector_dictionary3 = {} # average market cap per sector


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
	print (sector_dictionary, sector_dictionary2)
sort_companies_by_sector(data)