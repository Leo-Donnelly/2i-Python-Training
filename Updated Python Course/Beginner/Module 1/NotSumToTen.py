def not_sum_to_ten(num1, num2):
    total = num1 + num2

    if total == 10:
        return True
    else:
        return False
    
print(not_sum_to_ten(9, -1))