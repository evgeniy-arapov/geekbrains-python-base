import json
import pickle

with open('group.pickle', 'rb') as file:
    my_favourite_group_pickle = pickle.load(file)

with open('group.json', 'r') as file:
    my_favourite_group_json = json.load(file)

print(my_favourite_group_pickle)
print(my_favourite_group_json)
