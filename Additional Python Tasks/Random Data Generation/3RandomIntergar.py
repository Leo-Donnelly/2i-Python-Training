import random

def generate_random_numbers():
    for x in range(3):
        print(random.randrange(100,999,5))

def main():
    generate_random_numbers()

main()