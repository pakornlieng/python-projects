
from random import randint as r

class main():
    def __init__(self):
        answer = input("Would you like to use the probability calculator?(y/n)\n")
        answer.lower()
        if answer == "yes" or answer == "y":
            start, stop, groups, tests, condtional, sorter = B.conditions()
            B.probGen(start, stop, groups, tests, condtional, sorter)
        elif answer == "no" or answer == "n":
            print("Thank you for stopping by!!!")
        else:
            print("Invalid Input >:( \n \n \n \n \n . . . try again -_-")

    
class B():
    
    def conditions():
        #start, stop, groups = input("Enter values in this order(lower limit, upper limit, group size): \n").split()
        start = int(input("Enter lower limit: \n"))
        stop = int(input("Enter upper limit: \n"))
        groups = int(input("Enter group size: \n"))
        tests = int(input("Enter desired number of tests: \n"))
        conditional, sorter= input("How would u like to sort?(conditional, number)\n").split()
        sorter = int(sorter)
        return start, stop, groups, tests, conditional, sorter
        
    
    def probGen(start, stop, tests, groups, conditional, sorter):
    #variables 
        print("caculating . . .")
        basket = []
        count = 0
        numer = 0
        denom = tests  
    #generates the number of outputs desired 
        for i in range(tests):
        #creates a new array from the conditions for each interation of the loop
            array = [r(start,stop)for j in range(groups)]
        #checks through the array to see what numbers are lower than 10 
            count = sort(conditional, array, sorter)
        #adds the count to a basket
            basket.append(count)
        #reset the values of count 
            count = 0
        #checks what conditional to compare the values 
        
        out = (numer/denom) * 100
        print("Your probability is {}%".format(out))

    def  sort(conditional, basket, cond):
        
        match conditional: 
            case ">":
                number = C.greater_than(basket, )
                return number
            case "<":
                number = C.less_than(basket, cond)
                return number
            case ">=":
                number = C.greater_than_or_equal_to(basket, cond)
                return number
            case "<=":
                number = C.less_than_or_equal_to(basket, cond)
                return number
            case "==":
                number = C.equal_to(basket, cond)
                return number
                
            case _:
                return "Invalid Input >:("


class C():
    
   
    """   
    def  sort(conditional):
        
        match conditional: 
            case ">":
                number = greater_than(basket, cond)
            case "<":
                number = less_than(basket, cond)
            case ">=":
                number = greater_than_or_equal_to(basket, cond)
            case "<=":
                number = less_than_or_equal_to(basket, cond)
            case "==":
                number = equal_to(basket, cond)
                return number 
            case _:
                return "Invalid Input >:("
    """
   

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

