import os
import sys

print(sys.path)

name = sys.platform

for i in range(1, 6):
    print(os.getcwd())
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    print(new_path)
    # os.mkdir(new_path)
