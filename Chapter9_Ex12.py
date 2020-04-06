#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:25:57 2020

@author: manuel
"""
from fractions import Fraction

#a)
f=Fraction(1,2)
f1=Fraction(8,10)
print(f+f1)
print(f.__add__(f1)) #object fraction as an argument. returns a fraction object

#b
f2=Fraction(8,10)
print(f1.__eq__(f2))
print(f1==f2)

#c

print(f1) #note that the function is simplified
print(f1.__neg__())
print(-f1)

#d
print(f1.__gt__(f))
print(f1>f)