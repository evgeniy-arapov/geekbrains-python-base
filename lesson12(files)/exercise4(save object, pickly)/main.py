import pickle

person = {'name': 'John', 'age': 20, 'girls': ['Trixy', 'Jaine', 'Lu']}

print(person)
with open('object.txt', 'wb') as file:
    pickle.dump(person, file)

with open('object.txt', 'rb') as file:
    person_from_file = pickle.load(file)

print(person_from_file)
