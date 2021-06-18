import os
import sys


def ping():
    print('pong')


def hello(name):
    print('Hello, {}'.format(name))


def get_dir_list():
    print(os.listdir())


command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_dir_list()
elif command == 'name':
    name = sys.argv[2]
    hello(name)
