def divisible_by_ten(num):
    remaineder = num %10

    if remaineder == 0:
        return True
    else:
        return False
    
print(divisible_by_ten(20))