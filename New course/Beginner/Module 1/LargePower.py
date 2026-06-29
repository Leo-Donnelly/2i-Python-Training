def large_power(base, exponent):
    total = base**exponent 

    if total > 5000:
        return True
    else:
        return False
    
print(large_power(2, 13))