class Node:

    #Constructeur d'un noeud
    def __init__(self,lbl, father = None):
        self.label = lbl
        self.father = father
        self.children = []
        if father:
            father.add_child(self)

    def add_child(self, child):
        self.children.append(child)

    #Getter du nom du noeud
    def get_content(self):
        return self.label

    #Getter de la liste des enfants
    def get_children(self):
        return self.children

    def get_father(self):
        return self.father
