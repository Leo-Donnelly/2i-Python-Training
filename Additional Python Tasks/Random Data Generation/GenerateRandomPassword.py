import random
import string

def generate_random_password():
    RandPassword = random.choice(string.ascii_uppercase)
    RandPassword += random.choice(string.ascii_uppercase)
    RandPassword += random.choice(string.digits)
    RandPassword += random.choice(string.punctuation)

    for x in range(6):
        RandPassword += random.choice(string.ascii_lowercase)

    print(RandPassword)

def main():
    generate_random_password()

main()