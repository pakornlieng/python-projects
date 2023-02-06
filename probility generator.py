from random import randint as r

#add a test again option for ease of access
#add a thing where you can input what you want to change from the previous test

class main():
    def __init__(self):
        
        
        start, stop, groups, tests, cond1, sorter, appearances, cond2 = B.conditions()
       
        while True:
            B.probGen(start, stop, groups, tests, cond1, sorter, appearances, cond2)
            # answer = input()
            result = B.YesNoQuestion("Would you like to test again?\n")
            if result == False:
                break

            B.displayData(start, stop, groups, tests, cond1, sorter, cond2, appearances)
            
            # print("Here was your previous data:\nLower Limit: {}\nUpper Limit: {}\nGroups Size: {}\nTests ran: {}\nValues you were looking for: {} {}\nChance Number of Occurences: {}{}\n".format(start, stop, groups, tests, cond1, sorter, cond2, appearances))
            change = input("What would you like to change?\n").split()
            start, stop, groups, tests, cond1, sorter, cond2, appearances = B.change(start, stop, groups, tests, cond1, sorter, cond2, appearances, change)

class B():
    def displayData(start, stop, groups, tests, cond1, sorter, cond2, appearances):
        print("Here was your previous data:\nRange: {}-{}\nGroups Size: {}\nTests: {}\nValues you were looking for: v {} {}\nChance Number of Occurences: o {}{}\n".format(start, stop, groups, tests, cond1, sorter, cond2, appearances))
    
    def checkQuit(answer):
        if answer == "quit":
            return True
        return False

    def change(start, stop, groups, tests, cond1, sorter, cond2, appearances, condition):
        conds = [">=", ">", "<=", "<", "=="]
        
        for i in condition:
            i.lower()
        # change = []
            match i:
                case "r":
                    start, stop = input("Enter range: (LowerLimit UpperLimit)\n" ).split()
                    start = int(start)
                    stop = int(stop)
                case "g":
                    groups = int(input("Enter group size: \n"))
                case "t":
                    tests = int(input("Enter desired number of tests: \n"))
                case "v":
                    # block of code doesn't work because the variables that are referenced do not exist in this function
                    #problem solved 
                    
                    while True: 
                        try: 
                            cond1, sorter= input("Enter values you are looking for: (conditional number)\n").split()
                        except ValueError:
                            print("\nWrite the conditional in python, space, then the value: \n")
                        except UnboundLocalError:
                            print("Caught UnboundLocalError")
                        if cond1 in conds:
                            break
                        else: 
                            print("Enter a valid conditoinal: \nTry again >:( \n  ")

                case "o": 
                        while True:
                            try:
                                cond2, appearances = input("Enter chance number of occurances you want to calculate: (conditional number) \n" ).split()
                                appearances = int(appearances)
                            except ValueError:
                                print("\nWrite the conditional in python, space, then the value: \n")
                            if cond2 in conds and appearances <= groups:
                                break 
                # case "range" or "r":
                case "range":
                    start, stop = input("Enter range: (LowerLimit UpperLimit)\n" ).split()
                    start = int(start)
                    stop = int(stop)
                case "groups": #or "group size" or "g":
                    groups = int(input("Enter group size: \n"))
                case "tests": # or "tests" or "t":
                    tests = int(input("Enter desired number of tests: \n"))
                case "value": # or "v":
                    # block of code doesn't work because the variables that are referenced do not exist in this function
                    #problem solved 
                    
                    while True: 
                        try: 
                            cond1, sorter= input("Enter values you are looking for: (conditional number)\n").split()
                        except ValueError:
                            print("\nWrite the conditional in python, space, then the value: \n")
                        except UnboundLocalError:
                            print("Caught UnboundLocalError")
                        if cond1 in conds:
                            break
                        else: 
                            print("Enter a valid conditoinal: \nTry again >:( \n  ")

                case "occurences": # or "o":
                        while True:
                            try:
                                cond2, appearances = input("Enter chance number of occurances you want to calculate: (conditional number) \n" ).split()
                                appearances = int(appearances)
                            except ValueError:
                                print("\nWrite the conditional in python, space, then the value: \n")
                            if cond2 in conds and appearances <= groups:
                                break 

        return start, stop, groups, tests, cond1, sorter, cond2, appearances
                        # this would have the saame problem as trying to change the value 
                        # maybe after consoslidating the logic of both into a separate function then i won't run into this problme 


                

    def YesNoQuestion(question):
        while True:
            answer = input(question)
            answer.lower()
            if answer == "yes" or answer == "y" or answer == "ye":
                return True
            elif answer == "no" or answer == "n":
                print("Thank you for stopping by!!!")
                return False
            else:
                print("Invalid Input >:( \n \n \n \n \n . . . try again -_-")
        
    def conditions():
        #start, stop, groups = input("Enter values in this order(lower limit, upper limit, group size): \n").split()
        conds = [">=", ">", "<=", "<", "=="]

        start, stop = input("Enter range: (LowerLimit UpperLimit)\n" ).split()
        start = int(start)
        stop = int(stop)
        groups = int(input("Enter group size: \n"))


        # print(start)
        # print(stop)
        
        #there should be a way to consolidate both of these while statements into one function and having to call that function again
        while True: 
            try: 
                cond1, sorter= input("Enter values you are looking for: (conditional number)\n").split()
            except ValueError:
                print("\nWrite the conditional in python, space, then the value: \n")
            except UnboundLocalError:
                print("Caught UnboundLocalError")
            if cond1 in conds:
                break
            else: 
                print("Enter a valid conditoinal: \nTry again >:( \n  ")

        while True:
            try:
                cond2, appearances = input("Enter chance number of occurances you want to calculate: (conditional number) \n" ).split()
                appearances = int(appearances)
            except ValueError:
                print("\nWrite the conditional in python, space, then the value: \n")
            if cond2 in conds and appearances <= groups:
                break 

        
        tests = int(input("Enter desired number of tests: \n"))
        sorter = int(sorter)
        
        return start, stop, groups, tests, cond1, sorter, appearances, cond2
        
    
    def probGen(start, stop, groups, tests, cond1, sorter, appearances, cond2):
    #variables 
    
        print("caculating . . .")
        basket = []
        count = 0
        numer = 0
        denom = tests  
        data = []
    #generates the number of outputs desired 
        for i in range(tests):
        #creates a new array from the conditions for each interation of the loop
            array = [r(start,stop)for j in range(groups)]
            data.append(array)
        #checks through the array to see what numbers are lower than sorter 
            count = B.sorter(cond1, array, sorter)
        #adds the count to a basket
            basket.append(count)
        #reset the values of count 
            count = 0
        #checks what conditional to compare the values 
        numer = B.sorter(cond2, basket, appearances)
        out = (numer/denom) * 100
        print("Your probability is {} %".format(out))

        # print("\nWould you like to see the data set?\n")

    def sorter(conditional, basket, cond):
        
        match conditional: 
            case ">":
                number = B.greater_than(basket, cond)
                return number
            case "<":
                number = B.less_than(basket, cond)
                return number
            case ">=":
                number = B.greater_than_or_equal_to(basket, cond)
                return number
            case "<=":
                number = B.less_than_or_equal_to(basket, cond)
                return number
            case "==":
                number = B.equal_to(basket, cond)
                return number

    def greater_than(array, cond):
    #checks what numbers are greater than a condition
            number = 0
            for i in array:
                if i > cond:
                    numer += 1
            return number
    

    def greater_than_or_equal_to(array, cond):
    #cheks what numbers are greather than or equal to the condition
        numer = 0
        for i in array:
            if i >= cond:
                numer += 1
        return numer

    def less_than(array, cond):
    #checks what numbers are less than the condition
        numer = 0
        for i in array:
            if i < cond:
                numer += 1
        return numer

    def less_than_or_equal_to(array, cond):
    #checks what numbers are less than or equal to the condition
        numer = 0
        for i in array:
            if i <= cond:
                numer += 1
        return numer

    def equal_to(array, cond):
    #checks what numbers equal to the condition
        numer = 0
        for i in array:
            if i == cond:
                numer += 1
        return numer


main()

