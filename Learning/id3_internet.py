import math
import numpy as np

# Code founded on https://www.vtupulse.com/machine-learning/decision-tree-id3-algorithm-in-python/

class Node:
    def __init__(self):
        self.children = []
        self.value = ""
        self.isLeaf = False
        self.pred = ""


class TreeMaker :
    def __init__(self):
        pass

    def entropy(self, examples):
        pos = 0.0
        neg = 0.0
        for _, row in examples.iterrows():
            if row["answer"] == "yes":
                pos += 1
            else:
                neg += 1
        if pos == 0.0 or neg == 0.0:
            return 0.0
        else:
            p = pos / (pos + neg)
            n = neg / (pos + neg)
            return -(p * math.log(p, 2) + n * math.log(n, 2))

    def info_gain(self, examples, attr):
        uniq = np.unique(examples[attr])
        gain = self.entropy(examples)
        for u in uniq:
            subdata = examples[examples[attr] == u]
            sub_e = self.entropy(subdata)
            gain -= (float(len(subdata)) / float(len(examples))) * sub_e
        return gain

    def ID3(self, examples, attrs):
        root = Node()
        max_gain = 0
        max_feat = ""
        for feature in attrs:
            gain = self.info_gain(examples, feature)
            if gain > max_gain:
                max_gain = gain
                max_feat = feature
        root.value = max_feat
        uniq = np.unique(examples[max_feat])
        for u in uniq:
            subdata = examples[examples[max_feat] == u]
            if self.entropy(subdata) == 0.0:
                newNode = Node()
                newNode.isLeaf = True
                newNode.value = u
                newNode.pred = np.unique(subdata["answer"])
                root.children.append(newNode)
            else:
                dummyNode = Node()
                dummyNode.value = u
                new_attrs = attrs.copy()
                new_attrs.remove(max_feat)
                child = self.ID3(subdata, new_attrs)
                dummyNode.children.append(child)
                root.children.append(dummyNode)
        return root

    def printTree(self, root: Node, depth=0):
        for i in range(depth):
            print("\t", end="")
        print(root.value, end="")
        if root.isLeaf:
            print(" -> ", root.pred)
        print()
        for child in root.children:
            self.printTree(child, depth + 1)

