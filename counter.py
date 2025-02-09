#functions to calculate dollar totals of coins
def quarters():
    """function calculates dollar total of quarters"""
    qTotal = (quarter * 25) / 100
    return float(qTotal)
def dimes():
    """function calculates dollar total of dimes"""
    dTotal = (dime * 10) / 100
    return float(dTotal)
def nickles():
    """function calculates dollar total of nickles"""
    nTotal = (nickle * 5) / 100
    return float(nTotal)
def pennies():
    """function calculates dollar total of pennies"""
    pTotal = penny / 100
    return float(pTotal)

#variable definitions
quarter = int(input("How many quarters do you have? "))
dime = int(input("How many dimes do you have? "))
nickle = int(input("How many nickles do you have? "))
penny = int(input("How many pennies do you have? "))

print("You have " + str(quarters()) + " in quarters.")
