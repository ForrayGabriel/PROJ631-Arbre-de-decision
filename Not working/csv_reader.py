import csv

# Open en read a csv file


def read_csv(fichier):

    with open(fichier, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data = []
        for row in reader:
            data.append(row[0].split(","))
        return data
