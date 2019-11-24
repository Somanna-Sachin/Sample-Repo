import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Somanna"))
name = input("Your name? ")
print("Hello,", name)
r = requests.get("http://realpython.com")
print(r.status_code)
print("somanna")
