import pandas as pd
import Learning.id3_internet as appr
import Predicting.pred as pred

file = input("Chemin du fichier :\n")

data = pd.read_csv(file)

features = [feat for feat in data]
features.remove("answer")

TreeMaker = appr.TreeMaker()

Root = TreeMaker.ID3(data, features)

choice = "0"
while choice != "4":
    choice = input("1- Display data\n"
                   "2- Display tree\n"
                   "3- Make a prediction\n"
                   "4- Quit\n")
    if choice == "1":
        print("The data are :\n", data)
    elif choice == "2":
        TreeMaker.printTree(Root)
    elif choice == "3":
        Predicteur = pred.Predicteur(Root, features)
        if Predicteur.getRes():
            print("The prediction is :", Predicteur.getRes()[0])
