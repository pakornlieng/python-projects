
from random import randint as r

def __int__(self, answer):
    self.answer = input("Would you like to use the probability calculator(y/n)?")
    answer.lower()
    if answer == "yes" or answer == "y":
        conditions()
    elif answer == "no" or answer == "n":
        return False 
    print("that's is not a valid response >:(")

def conditions(self, start, stop, outputs, groups, conditional, cond):
        self.start = input("Enter your lower limit: ")
        self.stop = input ("Enter your upper limit: ")
        self.outputs = input("Enter how many outputs you want:")
        self.groups = input("Enter size of groups: ")
        self.conditional = input("Enter what conditional you want to find:")
        self.cond = input("Enter limit you want to find: ")
    
def probGen(start, stop, outputs, groups, conditional, cond):
    #variables 
    out = []
    count = 0
    numer = 0
    denom = outputs 
    #generates the number of outputs desired 
    for i in range(outputs):
        #creates a new array from the conditions for each interation of the loop
        array = [r(start,stop)for i in range(groups)]
        #checks through the array to see what numbers are lower than 10 
        if conditional == "greater than" or ">":
            count = greater_than(array, cond)
        elif conditional == "greater than or equal to " or ">=":
            count = greater_than_or_equal_to(array, cond)
        elif conditional == "less than" or "<":
            count = less_than(array, cond)
        elif conditional == "less than or equal to"  or "<=":
            count = less_than_or_equal_to(array, cond)
        elif conditional == "equal to" or "==":
            count = equal_to(array, cond)
        #adds the count to a basket
        out.append(count)
        #reset the values of count 
        count = 0
        #checks what conditional to compare the balues 
    if conditional == "greater than" or conditional == ">":
        numer = greater_than(out, cond)
    elif conditional == "greater than or equal to " or ">=":
        numer = greater_than_or_equal_to(out, cond)
    elif conditional == "less than" or "<":
        numer = less_than(out, cond)
    elif conditional == "less than or equal to"  or "<=":
        numer = less_than_or_equal_to(out, cond)
    elif conditional == "equal to" or "==":
        numer = equal_to(out, cond)

    return numer/denom

def greater_than(out, cond):
    #checks what numbers are greater than a condition
    number = 0
    for i in out:
        if i > cond:
            numer += 1
    return number
    

def greater_than_or_equal_to(out, cond):
    #cheks what numbers are greather than or equal to the condition
    numer = 0
    for i in out:
        if i >= cond:
            numer += 1
    return numer

def less_than(out, cond):
    #checks what numbers are less than the condition
    numer = 0
    for i in out:
        if i < cond:
            numer += 1
    return numer

def less_than_or_equal_to(out, cond):
    #checks what numbers are less than or equal to the condition
    numer = 0
    for i in out:
        if i <= cond:
            numer += 1
    return numer

def equal_to(out, cond):
    #checks what numbers equal to the condition
    numer = 0
    for i in out:
        if i == cond:
            numer += 1
    return numer

