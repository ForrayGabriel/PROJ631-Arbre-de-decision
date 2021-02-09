import csv_reader as cr

def get_Sapp(fichier):

	data = cr.read_csv(fichier)

	attributs_name = []

	for name in data[0]:
		attributs_name.append(name)

	attributs_val = []

	for i in range(0,len(attributs_name)):
		val = []
		for j in range(1,len(data)):
			if data[j][i] not in val:
				val.append(data[j][i])
		attributs_val.append(val)

	print(attributs_name)
	print(attributs_val)

	return attributs_name, attributs_val, data
