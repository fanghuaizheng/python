
def lines(file):
    for line in file:yield  line
    yield '\n'

f = open(r'D:\test\data\test01.txt')

result = lines(f)

print result