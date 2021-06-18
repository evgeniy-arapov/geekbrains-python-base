import os


def dir_creator():
    for i in range(1, 20, 2):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(new_path)


if __name__ == '__main__':
    dir_creator()
