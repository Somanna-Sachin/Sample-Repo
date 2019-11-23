import requests

name = input("Your name? ")
print("Hello,", name)
r = requests.get("http://realpython.com")
print(r.status_code)
print(r.ok)


print("somanna")
