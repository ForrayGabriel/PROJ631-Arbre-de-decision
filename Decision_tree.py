import Sapp_reader as Sr
import Tree_making.Node as nd
import Tree_making.Link as link
import ID3

class Decision_tree:

    def __init__(self, file):

        Sapp_rd = Sr.Sapp_reader("golf.csv")
        self.Sapp = Sapp_rd.get_Sapp()
        IG_calc = ID3.IG_calculator(self.Sapp)

        print(self.get_best(IG_calc.get_IG()))

    def get_best(self, S):

        best = 0
        max = 0
        for i in S:
            if i[1] > max :
                best = i[0]
                max = i[1]

        return  best

a = Decision_tree("golf.csv")

n1 = nd.Node("Noeud 1 ")

