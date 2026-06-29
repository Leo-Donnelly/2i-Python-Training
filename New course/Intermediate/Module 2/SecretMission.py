import requests

response = requests.get("https://api.github.com")

print("Secret misson has completed succesfully")
print("Status Code:", response.status_code)