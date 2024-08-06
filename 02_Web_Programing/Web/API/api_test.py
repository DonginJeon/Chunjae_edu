import requests

response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2")
print(response.json())

