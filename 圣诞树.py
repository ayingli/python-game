# -*- coding: utf-8 -*-
__author__ = 'ouyangmin'
__time__ = '2021/2/25 22:48'
# 如果该代码不能满足你的日常工作需求，可发邮件到lyycoder@163.com ，说清楚需求，我尽力帮你实现~
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()
circle.goto(0, 280)
circle.stamp()
k = 0
for i in range(1, 17):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()
    if i % 4 == 0:
        x = 30 * (j + 1)
        circle.color('red')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
        k += 2
    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
square.color('brown')
for i in range(17, 20):
    y = 30 * i
    for j in range(3):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()
turtle.exitonclick()

