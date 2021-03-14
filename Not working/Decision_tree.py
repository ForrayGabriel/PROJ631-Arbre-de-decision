import Sapp_reader as Sr
import Tree_making.Node as nd
import Tree_making.Link as link
import ID3
import math

class Decision_tree:

    def __init__(self, file):

        Sapp_rd = Sr.Sapp_reader("golf.csv")

        self.Sapp = Sapp_rd.get_Sapp()

        self.IG_calc = ID3.IG_calculator(self.Sapp)

        root = self.treeBuilding(self.Sapp, self.Sapp[0])

        print("ooooo", root.getChildren())

        self.afficheTree(root)


    #https://www.vtupulse.com/machine-learning/decision-tree-id3-algorithm-in-python/

    def treeBuilding(self, data, attributs):

        root = nd.Node()
        print(data)
        print("atributs", attributs)

        label = data[0][self.get_best(self.IG_calc.get_IG(data))]
        print(label)

        root.label = label
        index = self.searchGlobalIndex(label)
        print(index)

        uniq = data[1][index]
        print("youou", uniq)

        for u in uniq:
            subset = self.IG_calc.keep(data[2],u, index)
            print("uuu", subset)

            if self.entropy(subset) == 0.0 :
                newNode = nd.Node()
                newNode.isLeaf = True
                newNode.setLabel(u)
                newNode.pred = subset[0][len(subset[0])-1]
                root.addChildren(newNode)
            else :
                node = nd.Node()
                node.setLabel(u)
                newData = self.IG_calc.attributRemover(data, index)

                child = self.treeBuilding(newData, attributs[:index]+ attributs[index+1:])
                node.addChildren(child)
                root.addChildren(node)


        return root

    def searchGlobalIndex(self, keyword):
        for i in range(len(self.Sapp[0])):
            if self.Sapp[0][i] == keyword:
                return i
        return None

    def dataset_split(self, data, index, val):
        new = []

        for i in data:
            if i[index] == val:
                reducedSet = list(i[:index])
                reducedSet.extend(i[index+1:])
                new.append(reducedSet)
        return new


    def get_best(self, S):
        best = 0
        max = 0
        for i in S:
            if i[1] > max :
                best = i[0]
                max = i[1]

        return  best

    # Function that check if one of the attribute only return the same result
    def check_pure_class(self, sets):

        res = []
        for i in sets :
            first = i[0][len(i[0])-1]
            pure = True
            for j in i :
                if j[len(i[0])-1] != first:
                    pure = False
            res.append([pure, first, i[0][3]])
        return res

    def entropy(self,data):
        pos = 0.0
        neg = 0.0
        for i in data:
            if i[len(i)-1] == "yes":
                pos += 1
            else:
                neg += 1
        if pos == 0.0 or neg == 0.0:
            return 0.0
        else:
            p = pos / (pos + neg)
            n = neg / (pos + neg)
            return -(p * math.log(p, 2) + n * math.log(n, 2))

    def afficheTree(self, node, prof = 1):

        for i in range(prof):
            print("\t", end="")
        print(node.label)
        if node.isLeaf:
            for i in range(prof):
                print("\t", end="")
            print("           ", node.pred)
        for i in node.getChildren():
            self.afficheTree(i, prof+1)





a = Decision_tree("golf.csv")


