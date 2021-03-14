import Tree_making.Node as nd

class Link:

    def __init__(self, name):
        self.name = name
        self.start = None
        self.end = None

    def get_name(self):
        return self.name

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def setStart(self, node):
        self.start = node

    def setEnd(self, node):
        self.end = node