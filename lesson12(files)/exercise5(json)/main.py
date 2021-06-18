import json

person = {'name': 'John', 'age': 20, 'girls': ['Trixy', 'Jaine', 'Lu']}

person_json_str = json.dumps(person)

person_from_json = json.loads(person_json_str)

print(person)
print(type(person))
print(person_json_str)
print(type(person_json_str))
print(person_from_json)
print(type(person_from_json))
