import json

person = {'name': 'John', 'age': 20, 'girls': ['Trixy', 'Jaine', 'Lu']}

with open('person.json', 'w') as f:
    json.dump(person, f)

with open('person.json', 'r') as f:
    person_from_json = json.load(f)

print(person)
print(type(person))
print(person_from_json)
print(type(person_from_json))
