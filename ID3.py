import Sapp_reader as Sr
import math

def ID3(fichier):

	Sapp = Sr.get_Sapp(fichier)
	p("yes", Sapp)
	entropy(Sapp)

#Function that calculate the entropy
def entropy(S):

	entropy = 0

	for i in range(0,len(S[1][len(S[1])-1])):
		prob = p(S[1][len(S[1])-1][i],S)
		entropy -= prob*math.log2(prob)

	print(entropy)
	return(entropy)


#function that return the proportion of "result" in the last column of S
def p(result, S):

	cpt_occurence = 0
	cpt_total = 0

	for i in S[2]:
		cpt_total += 1
		if result == i[len(i)-1]:
			cpt_occurence +=1
	return cpt_occurence/cpt_total


ID3("golf.csv")