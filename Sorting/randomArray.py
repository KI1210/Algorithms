import random

def getRandomArray(length):
    arr = []
    choiceArray = list(range(length))
    
    for i in range(length):
        arr.append(random.choice(choiceArray))
    
    return arr