import random
import string

def generate_string():
    randomString = ''.join(random.choice(string.ascii_letters) for x in range(5))
    print (randomString)

def main():
    generate_string()

main()