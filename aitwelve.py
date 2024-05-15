import random as rand

weights = []
#this is the random numbers that the weights are going to be
w1 = rand.randint(0,5)

w2 = rand.randint(0,5)

w3 = rand.randint(0,5)

weights.append(w1)
weights.append(w2)
weights.append(w3)

print ("The initail weights are: ",weights)

maxNoOfIterations = 6

noOfFeatures = 2

for i in range(maxNoOfIterations):
    print("Data added!")

print("The final weights are:",weights)