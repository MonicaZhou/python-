#使用turtle库，绘制一个叠边形，其中，叠边形内角为100度
'''
import turtle as t
t.setup(650,350,200,200)
t.pu()
t.fd(50)
t.left(-90)
t.fd(100)
t.right(90)
t.pd()
t.pensize(5)
t.pencolor("black")
for i in range(9):
    t.right(80)
    t.fd(150)
t.done()
'''

#TwoRoundDraw.py
import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(150)
    t.left(80)  #720/9
