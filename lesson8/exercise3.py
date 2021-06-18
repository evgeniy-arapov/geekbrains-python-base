def greeting(*args, say='Hello'):
    print(say, args)


greeting('Leo', 'Kate', 'Max', say='Hi')
greeting('Leo', 'Kate', 'Max')


def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age='22')
