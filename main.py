import pandas as pd
import math
import numpy as np
import Apprentissage.id3_internet as appr
import Prediction.pred as pred

data = pd.read_csv("3-dataset.csv")
features = [feat for feat in data]
features.remove("answer")

Root = appr.ID3(data, features)

Predicteur  = pred.Predicteur(Root, features)

print(Predicteur.getRes())


