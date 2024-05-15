x_input = [0.1, 0.5, 0.2]

weights = [0.4, 0.3, 0.6]

threshold = 0.5

def step(weightedSum):
    if weightedSum>threshold:
        return 1
    else:
        return 0

def perceptron():
    weightedSum = 0
    for x,w in zip(x_input,weights):
        weightedSum += x*w
        print (weightedSum)
    return step(weightedSum)

output = perceptron()

print("Output: "+str(output))