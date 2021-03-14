import csv_reader as cr

#Function that take a data set form a csv file and return a list of the names
#of the attributs, a list of the differents value possible and a trimed dataset without the first line

class Sapp_reader:

	def __init__(self, file):
		self.file = file

	def get_Sapp(self):

		#Get the data from a csv file
		data = cr.read_csv(self.file)

		attributs_name = []

		#Get the differents attributs names
		for name in data[0]:
			attributs_name.append(name)

		attributs_val = []

		#Get the differents value for every attributs
		for i in range(0,len(attributs_name)):
			val = []
			for j in range(1,len(data)):
				if data[j][i] not in val:
					val.append(data[j][i])
			attributs_val.append(val)

		return attributs_name, attributs_val, data[1:]
