import random #generate a random integer

def rollDice():
    '''This function returns a random integer 1,2,3,4,5 or 6'''
    return random.randrange(1,7)

def firstRoll(numDice):
    '''rolls numDice and return a list of the length numDice of random integers each obtained by calling rollDice'''
    lengthlist=[]
    # roll the dice 'numDice' times and append the results to lengthlist
    
    for _ in range(numDice):
        lengthlist.append(rollDice())
    return lengthlist

def newRoll(diceList, choice):
    '''Performs a new roll for the dice that did not match the choice in the previous roll  '''
    newlist = []
    # Roll each die; if it matches 'choice', keep it, otherwise roll again
    
    for dice in diceList:
        if dice != choice:
            newlist.append(rollDice()) #Reroll and add to the newlist
        else:
            newlist.append(dice)
    return newlist

def createDiceDict(diceList):
    '''create a dictionary which keys are possible roll values which values are the number of times that roll value appear in the list'''
    # Create a dictionary to count the occurences of each die value 

    diceDict = {i:0 for i in range(1,7)} # Increment the count for each die value 
    for dice in diceList:
        diceDict[dice] += 1
    return diceDict

def mostFrequent(diceDict):
    '''Return the highest dice value that have the largest number of matching dice'''

    maxFrequency = 0
    maxDiceValue = None

    for diceValue, count in diceDict.items():
        if count > maxFrequency:
            maxFrequency = count
            maxDiceValue = diceValue
        elif count == maxFrequency and maxDiceValue is not None:
            maxDiceValue = max(maxDiceValue, diceValue)
    return maxDiceValue 

def probabilityYahtzee(numTrials,numDice):
    '''Calculates the probability of getting a Yahtzee in a given number of trials'''
    yahtzeeCount = 0 #Initializing 
    for _ in range(numTrials): # Repeat the simulation 'numTrails' times 
        dice = firstRoll(numDice)
        for _ in range(2):#Roll two more times 
            if len(set(dice)) == 1: #To check whether the dice are all the same
                yahtzeeCount += 1
                break
            
    return yahtzeeCount / numTrials #The probability of Yahtzee to appear 

def rollsToGetTenzi(numTrials,numDice):
    '''A simulation to check how many rolls it needs to be to let all the dice to be the same'''

    rollcount = {i:0 for i in range(1,11)} #A dictionary whose keys are the numbers of rolls that it takes 
    rollcount['more than 10'] = 0 #After 10 rolls the dice do not all match

    for _ in range(numTrials):
        dice = firstRoll(numDice)
        roll = 1
        while True:
            if len(set(dice)) == 1: #To check whether the dice are all the same
                break
            if roll >= 10:
                rollcount['more than 10'] += 1
                break
            else:
                diceDict = createDiceDict(dice)
                dice = newRoll(dice,mostFrequent(diceDict))
                roll += 1

        if roll <= 10: #more logic not sure
            rollcount[roll] += 1
    return rollcount

# main program 

def main():
    while True: 
        character = input("Enter Y to Yahtzee, T to Tenzi:")
        if character == 'Y':
            numTrials = int(input("Enter number of trials for Yahtzee:"))
            numDice = int(input("Enter number of dice for Yahtzee:"))
            prob = probabilityYahtzee(numTrials, numDice)
            print(f"Probability of Yahtzee with {numDice} dice: {prob:.4f}")
        elif character == 'T':
            numTrials = int(input("Enter number of trials for Tenzi:"))
            numDice = int(input("Enter number of dice for Tenzi:"))
            rollcount = rollsToGetTenzi(numTrials, numDice)
            print(f"Rolls to get a Tenzi with {numDice} dice: ")
            for rolls, count in rollcount.items():
                print(f"{rolls}: {count}")
        else:
            break

if __name__ == "__main__": #Check whether the file is being run by the main program or not 
    main()
