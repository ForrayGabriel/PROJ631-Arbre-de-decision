class Predicteur:

    def __init__(self, Node, features):
        self.root = Node
        self.features = features
        self.info = self.getInfo()
        self.res = self.predict(self.root)

    def getInfo(self):
        res = {}
        for i in self.features:
            a = input("What is the " + i + " :\n")
            res[i] = a
        return res

    def predict(self, node):
        print(node.value)
        res = self.info[node.value]
        bool = False
        for i in node.children:
            print("Child values :", i.value)
            if i.value == res :
                print("oui")
                if i.isLeaf :
                    return i.pred
                bool = True
                ress = self.predict(i.children[0])
        if bool == False:
            print("Il y a une erreur sur la saisie")
        return ress

    def getRes(self):
        return self.res
