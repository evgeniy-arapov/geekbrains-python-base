import pickle, json

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
    ]
}

my_favourite_group_pickle = pickle.dumps(my_favourite_group)
my_favourite_group_json = json.dumps(my_favourite_group)

print(my_favourite_group_pickle)
print(my_favourite_group_json)

with open('group.pickle', 'wb') as file:
    pickle.dump(my_favourite_group, file)

with open('group.json', 'w', encoding='utf-8') as file:
    json.dump(my_favourite_group, file)
