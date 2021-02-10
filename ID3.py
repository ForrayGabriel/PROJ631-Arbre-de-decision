import Sapp_reader as Sr
import math

def ID3(fichier):

	Sapp = Sr.get_Sapp(fichier)
	#print(Sapp)
	entropy_global = entropy_set(Sapp, len(Sapp[0])-1)
	print("The global entropy is ", entropy_global)
	#print(Sapp[0], "\n", Sapp[1], "\n", Sapp[2])
	#Sub_setter(Sapp,0)
	#print("Hein ?" ,set_divider(Sub_setter(Sapp,0)[0]))
	print("Entropy de ",Sub_setter(Sapp,0)[1][0][0], " :", entropy_set(set_divider(Sub_setter(Sapp,0)[1]),4))

	print(Information_Gain(Sapp,0))


	Info_Gain = []
	for i in range(len(Sapp[0])-1):
		Info_Gain.append([i,Information_Gain(Sapp,i)])

	print(Info_Gain)

def Information_Gain(S, index):

	entropy_global = entropy_set(S, len(S[0])-1)

	I = 0
	j = 0

	for i in S[1][index]:
		print(i)
		print(p(i,S,index))
		I += p(i,S,index) * entropy_set(set_divider(Sub_setter(S,index)[j]),len(S[0])-1)
		j+=1
	print(I)
	return(entropy_global-I)


def Sub_setter(S, index):

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
def entropy_set(S, index):

	entropy = 0

	for i in range(0,len(S[1][index])):
		prob = p(S[1][index][i],S, index)
		entropy -= prob*math.log2(prob)

	return(entropy)


#function that return the proportion of "result" in the last column of S
def p(result, S, index):

	cpt_occurence = 0
	cpt_total = 0

	for i in S[2]:
		cpt_total += 1
		if result == i[index]:
			cpt_occurence +=1
	return cpt_occurence/cpt_total

def set_divider(S):

	attributs_val = []

	#Get the differents value for every attributs
	for i in range(0,len(S[0])):
		val = []
		for j in range(1,len(S)):
			if S[j][i] not in val:
				val.append(S[j][i])
		attributs_val.append(val)

	return None,attributs_val, S


ID3("golf.csv")