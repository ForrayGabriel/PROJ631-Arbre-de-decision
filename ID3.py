import Sapp_reader as Sr
import math

def ID3(fichier):

	Sapp = Sr.get_Sapp(fichier)
	entropy_set(Sapp, 4)
	print(Sapp[0], "\n", Sapp[1], "\n", Sapp[2])

def Information_Gain(S, A):
	E = entropy_set(S)


#Function that calculate the entropy
def entropy_set(S, index):

	entropy = 0

	for i in range(0,len(S[1][index])):
		prob = p(S[1][index][i],S, index)
		entropy -= prob*math.log2(prob)

	print(entropy)
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


ID3("golf.csv")