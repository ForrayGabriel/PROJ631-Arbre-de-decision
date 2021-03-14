class Node:

    #Constructeur d'un noeud
    def __init__(self):
        self.label = ""
        self.pred =   ""
        self.children = []
        self.isLeaf = False

    def addChildren(self, child):
        self.children.append(child)

    def setLabel(self, lbl):
        self.label = lbl

    def setNext(self, next):
        self.next=next

    def setChildren(self, child):
        self.children = child

    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def getChildren(self):
        return self.children