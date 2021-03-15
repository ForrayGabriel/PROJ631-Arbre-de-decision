# PROJ631 : _Arbre de decision_
First mini project for the PROJ631 about creating a decision tree

During this project I learned a lot about how decision tree are made.
I tried making one myself, but I didn't succed and finally took an already existing algorythm that I found online.

I was able to read a .csv file, calculate the entropy and information gain of a feature, but the way I made my function made it impossible for me to build the recursive tree.

I took [this algorythm](https://www.vtupulse.com/machine-learning/decision-tree-id3-algorithm-in-python/) and analysed how it worked.

I then made the part that use the tree given by the algorythm to predict the answer.

# How to use :
Just launch main.py using a python interpreter.

The program will ask you the path to the file containing the training data (you can use the given data.csv).

Then a menu will show. By typing the right number and pressing enter you can :
* Display the data
* Display the decision tree
* Make a prediction

When choosing to make a prediction, you will be asked various informations. If one of your answers is necessary and doesn't correspond to any know data, an error message will be displayed.

# Structure :
_Not working folder :_
All of the useless files that I initially made but are useless

* csv_reader : open a .csv file and return the data
* sapp_reader : use the .csv reader to retreive the 
* ID3 : contains the function to calculate and split sets
* Decision_tree : Tries to make a tree but doesn't work

_Learning folder :_ 
* id3_internet : The file that make a decision tree out of data

_Predicting folder :_ 
* pred : The file that give a prediction
