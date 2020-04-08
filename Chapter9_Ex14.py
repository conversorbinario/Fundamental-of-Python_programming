#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:24:47 2020

@author: manuel
"""

import turtle

def positioning(figure, a, b):
    figure.penup()
    figure.setposition(a, b)
    figure.pendown()

def triangle(triangle, side):
    positioning(triangle, -150, -150)
    for n in range(3):
        triangle.forward(side)
        triangle.left(180-60) 
        ''' Remember. Turtle uses the EXTERNAL angle
        to calculate to angle. So given that we want a triangle whose angles are of 60º,
        we have to calculate the external angle with (180-anglewewant)'''
    
def star(star,side):
    positioning(star, -100, 40)
    for n in range(5):
        star.forward(side)
        star.right(180-36) 
    
def wave(wave, side):
    positioning(wave, 0, 0)
    angulo_onda=20
    wave.left(80)
    wave.forward(side)
    for n in range(4):
        wave.right(180-angulo_onda)
        wave.forward(side)
        wave.left(180-angulo_onda)
        wave.forward(side)
    wave.right(180-angulo_onda)
    wave.forward(side)
    
def square_of_squares(square, side):
    positioning(square, 80, 80)
    sides=side/5
    square.left(90)
    for n in range (5):
        if n%2==0:
            square.forward(side)
            square.right(90)
            square.forward(sides)
            square.right(90)
        else:
            square.forward(side)
            square.left(90)
            square.forward(sides)
            square.left(90)
    square.forward(side)
    square.right(90)
    for n in range (5):
        if n%2==0:
            square.forward(side)
            square.right(90)
            square.forward(sides)
            square.right(90)
        else:
            square.forward(side)
            square.left(90)
            square.forward(sides)
            square.left(90)
    square.forward(side)

def square(obj, side, howmany, pos):
        obj.penup()
        obj.setpos(pos)
        obj.pendown()
        obj.right(180)
        obj.forward(side/2)
        for n in range(3):
            obj.right(90)
            obj.forward(side)
        obj.right(90)
        obj.forward(side/2)
        pos=obj.pos()
        for n in range(1, howmany):
            obj.penup()
            obj.setpos(-70, 240)
            obj.left(360-20)
            obj.forward(40)
            pos=obj.pos()
            obj.setpos(pos)
            obj.pendown()
            obj.right(90)
            obj.forward(side/2)
            if howmany%2==0:
                for n in range(3):
                    obj.right(90)
                    obj.forward(side)
                obj.right(90)
                obj.forward(side/2)
            else:
                for n in range(3):
                    obj.left(90)
                    obj.forward(side)
                obj.left(90)
                obj.forward(side/2)
        obj.hideturtle()
           
        
                

def circle_stuff(t5):
    t6=turtle.Turtle()
    
    positioning(t5, -70, 200)
    t5.circle(40)    
     
    for n in range(18):
        t5.penup()
        t5.setpos(-70, 240)
        t5.left(360-20)
        t5.pendown()
        t5.forward(40)
    t5.hideturtle()
    square(t6,80,18,(-70, 200))
        
def main():
    t1=turtle.Turtle()
    t2=turtle.Turtle()
    t3=turtle.Turtle()
    t4=turtle.Turtle()
    t5=turtle.Turtle()
    triangle(t1,50)
    star(t2, 60)
    wave(t3, 50)
    square_of_squares(t4, 100)
    circle_stuff(t5)
turtle.clearscreen()
wn=turtle.Screen()
wn.bgcolor("lightblue")
main()
wn.exitonclick()