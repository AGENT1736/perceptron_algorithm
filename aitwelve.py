import random as rand

features = int(input("Enter number of features: "))

# labels = int(input("Enter number of labels: "))

itrs = int(input("Enter number of iterations"))

numOfPoints = int(input("Enter number of points"))

points = [[] for i in range(numOfPoints)]

labels = [0,1]

results = [[] for i in range(features)]