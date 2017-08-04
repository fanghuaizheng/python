from subprocess import Popen, PIPE

text = open(r'D:\test\data\messy.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
# print tidy

tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read()