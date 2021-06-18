import os
import datetime
import shutil


def create_file(name, text=None):
    with open(name, 'w') as f:
        f.write(text)


def create_dir(name):
    try:
        os.mkdir(name)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def delete(name):
    try:
        if os.path.isdir(name):
            shutil.rmtree(name)
        else:
            os.remove(name)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def rename(name, new_name):
    try:
        os.rename(rf'{name}', rf'{new_name}')
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def copy(name, new_name):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copyfile(name, new_name)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def get_list():
    print(os.listdir())


def save_log(command, name, advanced_arg):
    with open('log.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {command}')
        if name:
            f.write(f': {name}')
        if advanced_arg:
            f.write(f' - {advanced_arg}')
        f.write('\n')


def change_dir(arg):
    print('Current dir {}'.format(os.getcwd()))
    try:
        os.chdir(arg)
        print('Dir changed to {}'.format(os.getcwd()))
    except Exception as e:
        print(f'Error: {e}')
