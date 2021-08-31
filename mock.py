import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE)
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + "tony")
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + "jack")
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + "bruce")
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + "steve")
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + "unkown")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + "tony")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + "bruce")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + "jack")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + "steve")
print(response.json())

input("Press Enter for next")


response = requests.put(BASE + "tony")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + "unkown")
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + " ")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + " ")
print(response.json())

input("Press Enter for next")

response = requests.get(BASE + "")
print(response.json())

input("Press Enter for next")

response = requests.put(BASE + "")
print(response.json())