import Sapp_reader as Sr
import Tree_making.Node as nd
import Tree_making.Link as link
import ID3

class Decision_tree:

    def __init__(self, file):

        node_list = []
        link_list = []

        Sapp_rd = Sr.Sapp_reader("golf.csv")
        self.Sapp = Sapp_rd.get_Sapp()
        self.IG_calc = ID3.IG_calculator(self.Sapp)

        print(self.get_best(self.IG_calc.get_IG()))
        print(self.Sapp)

        index =  self.get_best(self.IG_calc.get_IG())
        root = nd.Node(self.Sapp[0][self.get_best(self.IG_calc.get_IG())])
        print(root.get_content())
        print(self.IG_calc.Sub_setter(self.Sapp, index ))
        for i in self.check_pure_class(index) :
            if i[0]:
                nd.Node(i[1], root)


    def get_best(self, S):

        best = 0
        max = 0
        for i in S:
            if i[1] > max :
                best = i[0]
                max = i[1]

        return  best

    def check_pure_class(self, index):
        sets = self.IG_calc.Sub_setter(self.Sapp, index )

        res = []
        for i in sets :
            first = i[0][len(i[0])-1]
            pure = True
            for j in i :
                if j[len(i[0])-1] != first:
                    pure = False
            res.append([pure, first])
        return res



a = Decision_tree("golf.csv")

n1 = nd.Node("Noeud 1 ")

