#functions to calculate dollar totals of each coin
def quarters():
    """function to calculate dollar totals of quarters"""
    qTotal = (quarter * 25) / 100
    return float(qTotal)

quarter = int(input("How many quarters? "))
print(quarters())    
