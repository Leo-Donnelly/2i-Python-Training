import random
import secrets

def generate_token():
    secureToken = secrets.token_bytes(64)
    return secureToken

def generate_URL():
    password_reset_link = "rockfield.com/users/user/reset="
    password_reset_link += secrets.token_urlsafe(16)
    return password_reset_link

def output(secureToken, password_reset_link):
    print("64 Byte token", secureToken)
    print("Password reset URL", password_reset_link)

def main():
    secureToken = generate_token()
    password_reset_link = generate_URL()
    output(secureToken, password_reset_link)

main()