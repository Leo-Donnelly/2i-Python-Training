def over_budget(budget, food_bill, electricty_bill, internet_bill, rent):
    total = food_bill + electricty_bill + internet_bill + rent

    if total > budget:
        return True
    else:
        return False
    
print(over_budget(80,20,30,10,30))