import random
M = input()
op = ['+','-','*','/']
#s = random.random(op)
s = input(random.choice(op))
N = input()
if s == '+':
    A = eval('M + N')
    print("{:.2f}".format(A))
elif s == '-':
    B = eval('M - N')
    print("{:.2f}".format(B))
elif s == '*':
    C = eval('M * N')
    print("{:.2f}".format(C))
elif s == '/':
    D = eval('M / N')
    print("{:.2f}".format(D))
