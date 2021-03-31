# -*- coding: utf-8 -*-
__author__ = 'ouyangmin'
__time__ = '2021/2/15 13:47'

a = 20       #年收入减去花销剩余
b = 1.04     #年收益加上本金
c = 60       #初始存款
d = c*pow(b, 8)      #计算60万在15年之后的本息之和
print(d)

sum = 0
for i in range(1, 8):
    sum = sum+a*pow(b, i)
    print(sum)            #打印出每年本息之和
print(sum)    #年剩余20万，理财收益10%，15年之后的本息之和

sum1 = d+sum  #计算60万在15年之后的本息之和加上年剩余20万，理财收益10%，15年之后的本息之和
print(sum1)  #打印总储存
