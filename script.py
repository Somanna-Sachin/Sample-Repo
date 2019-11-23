import requests

name = input("Your name? ")
print("Hello,", name)
r = requests.get("http://realpython.com")
print(requests.codes(r))

print("somanna")
