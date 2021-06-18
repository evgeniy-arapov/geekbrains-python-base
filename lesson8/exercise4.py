def my_f():
    global global_var
    local_var = 1

    print(local_var)
    print(global_var)
    global_var = 4


# my_f()

global_var = 2

my_f()

print(global_var)