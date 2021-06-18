import os

print(os.name)

print(os.getcwd())

new_path = os.path.join(os.getcwd(), 'new_f')

os.mkdir(new_path)