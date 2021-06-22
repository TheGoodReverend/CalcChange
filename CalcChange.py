#! /usr/bin/env python3
# CalcChange - KBowen

#Get Coin Method (We prefer the term function)
def getCoin(cointype):
    c = -1
    while c < 0:
        try:
            c = int(input("How many " + cointype + " do you have?: "))
            if c<0:
                print("Coins must be positive")
        except ValueError:
            print("Illegal input: must be a non negative integer")
            c = -1
            
    return c

print("Welcome to Change Calculator.")
print()



choice = input("Do you have change? (y/n) ")
#add option to accept anything that starts with Y

runningtotal = 0

while choice[0].lower() == "y":
    print("Your answer was " + choice)

    h = getCoin("Half Dollars")
    print("Half Dollars = " + str(h))
    q = getCoin("Quarters")
    print("Quarters = " + str(q))
    d = getCoin("Dimes")
    print("Dimes = " + str(d))
    n = getCoin("Nickles")
    print("Nickles = " + str(n))
    p = getCoin("Pennies")
    print("Pennies = " + str(p))

    totcents = (h*50) + (q*25) + (d*10) + (n*5) + p
    print("You have " + str(totcents) + " cent(s).")
    
    dollars = totcents //100
    cents = totcents % 100
    
    
    runningtotal += totcents
    runningdollars = runningtotal //100
    runningcents = runningtotal % 100
    

    print("Which is " + str(dollars) + " dollars and " + str(cents) + " cent(s).")
    choice = input("Do you have more change? (y/n) ")
    print()

print("Thanks for using the change calculator.")
print("You have a total of " + str(runningtotal) + " cent(s).")
print("Which is " + str(runningdollars) + " dollars and " + str(runningcents) + " cents.")
