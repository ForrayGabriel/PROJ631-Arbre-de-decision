import csv

def csv-reader(fichier):
	
	with open(fichier, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ' ', quotechar='|')
		data = []
		for row in reader:
			data.append(row[0].split(","))
		return data

for row in read_csv('golf.csv'):
	print(row)

