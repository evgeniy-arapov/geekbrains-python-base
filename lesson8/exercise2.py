def get_sep(sep, sep_len):
    return sep * sep_len


print(get_sep('_-', 50))
sep = get_sep('*', 2)
print('раз {} два {}'.format(sep, sep))
