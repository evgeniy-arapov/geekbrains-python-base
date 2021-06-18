import inspect
import os
import random
import sys
from core import get_list, create_dir, create_file, rename, delete, save_log, copy, change_dir

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from lessons6_7 import python_guesses, user_guesses
sys.path.insert(0, current_dir)

command = None
name = None
text = None
new_name = None

for index in range(len(sys.argv)):
    if index == 1:
        command = sys.argv[index]
    if index == 2:
        name = sys.argv[index]
    if index == 3:
        new_name = None
        text = None
        if command == 'file':
            text = sys.argv[index]
        else:
            new_name = sys.argv[index]

# print(f'command: {command}')
# print(f'name: {name}')
# print(f'text: {text}')
# print(f'new_name: {new_name}')

if command == 'list':
    get_list()
elif command == 'play':
    playGame = random.choice([user_guesses.play, python_guesses.play])
    playGame()
elif not name:
    raise Exception('name required')
elif command == 'mkdir':
    create_dir(name)
elif command == 'file':
    create_file(name, text)
elif command == 'cd':
    change_dir(name)
elif command == 'delete':
    delete(name)
elif not name:
    raise Exception('second argument required')
elif command == 'rename':
    rename(name, new_name)
elif command == 'copy':
    copy(name, new_name)

save_log(command, name, new_name or text)
