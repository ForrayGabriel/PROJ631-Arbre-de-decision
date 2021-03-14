import math


class IG_calculator:

	def __init__(self, Sapp):
        pass

	def get_IG(self, data):

		Info_Gain = []
		for i in range(len(data[0])-1):
			Info_Gain.append([i,self.Information_Gain(data,i)])

		print("je sais pas smamam",Info_Gain)
		return(Info_Gain)

	# Function that return the information gain for a given index
	def Information_Gain(self,S, index):

		entropy_global = self.entropy_set(S, len(S[0])-1)

		I = 0
		j = 0

		for i in S[1][index]:
			I += self.p(i,S,index) * self.entropy_set(self.set_divider(self.Sub_setter(S,index)[j]),len(S[0])-1)
			j+=1
		return(entropy_global-I)

	# Function that return a list in which each list only contain one result at the given posistion
	def Sub_setter(self,S, index):

		sub_sets = []

		for j in range(len(S[1][index])):

			searched = S[1][index][j]
			sub_set = []
			for i in S[2] :
				if i[index] == searched:
					sub_set.append(i)

			sub_sets.append(sub_set)

		return(sub_sets)


	#Function that calculate the entropy
	def entropy_set(self, S, index):

		entropy = 0

		for i in range(0,len(S[1][index])):
			prob = self.p(S[1][index][i],S, index)
			entropy -= prob*math.log2(prob)

		return(entropy)


	#function that return the proportion of "result" in the last column of S
	def p(self, result, S, index):

		cpt_occurence = 0
		cpt_total = 0

		for i in S[2]:
			cpt_total += 1
			if result == i[index]:
				cpt_occurence +=1
		return cpt_occurence/cpt_total

	# Function that
	def set_divider(self, S):

		attributs_val = []

		#Get the differents value for every attributs
		for i in range(0,len(S[0])):
			val = []
			for j in range(1,len(S)):
				if S[j][i] not in val:
					val.append(S[j][i])
			attributs_val.append(val)

		return None,attributs_val, S

	def attributRemover(self, data, index):
		list1 = []
		list2 = []
		list3 = []
		for i in range(len(data[0])):
			if i != index:
				list1.append(data[0][i])
		for i in range(len(data[1])):
			if i != index:
				list2.append(data[1][i])
		for j in data[2]:
			list4 = []
			for i in range(len(j)):
				if i != index:
					list4.append(j[i])
			list3.append(list4)

		res = [list1, list2, list3]
		return res

	def keep(self, data, label, index):
		res = []
		for i in data:
			if i[index] == label:
				res.append(i)
		return res
