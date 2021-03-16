class Predicteur:

    def __init__(self, Node, features):
        self.root = Node
        self.features = features
        self.info = self.getInfo()
        self.res = self.predict(self.root)

    def getInfo(self):
        """Ask the user about the necessary inforamtions"""

        res = {}
        for i in self.features:
            a = input("What is the " + i + " :\n")
            res[i] = a
        return res

    def predict(self, node):
        """Retrun a the next node corresponding to the data in the tree

        """
        res = self.info[node.value]
        bool = False
        for i in node.children:
            if i.value == res:
                if i.isLeaf:
                    return i.pred
                bool = True
                ress = self.predict(i.children[0])
        if not bool:
            print("Error : user entry doesn't correspond to any known data")
            return False
        return ress

    def getRes(self):
        """Return the value of the choosen leaf of the tree

        """
        return self.res
