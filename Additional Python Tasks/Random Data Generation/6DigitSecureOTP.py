import secrets

def generate_secret_num():
    secretsGenerator = secrets.SystemRandom()

    random_pass = secretsGenerator.randrange(100000, 999999)

    return random_pass

def display_OTP(random_pass):
    print("Your OTP is:", random_pass)

def main():
    random_pass = generate_secret_num()
    display_OTP(random_pass)

main()