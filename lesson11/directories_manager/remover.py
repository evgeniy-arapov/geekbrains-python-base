import os


def dir_remover():
    paths_list = filter(lambda el: 'dir_' in el, os.listdir())

    for dir_name in paths_list:
        path_name = os.path.join(os.getcwd(), dir_name)
        print(path_name)
        os.rmdir(path_name)


if __name__ == '__main__':
    dir_remover()
