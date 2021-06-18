s = 'Hello world, да?'

bs = b'Hello world'

us = s.encode('utf-8')

# asc = s.encode('ascii')

print(s)
print(bs)

for simbol in s:
    print(simbol, end=' = ')
    print(simbol.encode('utf-8'))

# print('\n')
#
# for simbol in bs:
#     print(simbol)
#
# print('\n')
#
# for simbol in us:
#     print(simbol)
#
# print('\n')
#
# for simbol in asc:
#     print(simbol)
