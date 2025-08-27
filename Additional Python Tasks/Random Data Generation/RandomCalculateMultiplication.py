import random

def find_random_number():
    random1 = random.uniform(0.1, 1)
    random2= random.uniform(9.5, 99.5)
    
    return random1, random2

def multiply(random1, random2):
    total = random1*random2
    print(total)

def main():
    random1, random2 = find_random_number()
    multiply(random1, random2)

main()