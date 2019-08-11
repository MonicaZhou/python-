'''
人民币和美元间汇率固定为：1美元 = 6.78人民币。
'''
a = input()
if a[:3] == 'RMB':
    R = eval(a[3:]) / 6.78
    print("USD{:.2f}".format(R))
elif a[:3] == 'USD':
    U = eval(a[3:]) * 6.78
    print("RMB{:.2f}".format(U))
