f = open('first.txt', 'w')

f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])
f.close()

# f = open('first.txt', 'r')
# print(f.read())
# f.close()
#
# f = open('first.txt', 'r')
# for line in f:
#     print(line)
# f.close()
#
# f = open('first.txt', 'r')
# print(f.readlines())
# f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line)

print('end')
