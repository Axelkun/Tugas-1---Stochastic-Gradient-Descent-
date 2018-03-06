# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:45:59 2018

@author: Antraxiana
"""
import pylab as pl
import numpy as np
import csv
import random

def read_lines():
    with open('Iris.csv', 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
            yield [ float(i) for i in row ]
x = list(read_lines())
      
n= int(input('enter epoch: '))
def q0():
    return random.uniform(-1,1)
def q1():
    return random.uniform(-1,1)
def q2():
    return random.uniform(-1,1)
def q3():
    return random.uniform(-1,1)
def b():
    return random.uniform(-1,1)
a= float(input('enter alpha: '))
ls=[[0.1]*n]*len(x)
def ha(tq0,tq1,tq2,tq3,tb,i):
    return (tq0*x[i][0])+(tq1*x[i][1])+(tq2*x[i][2])+(tq3*x[i][3])+tb
def sigmoid(h):
    return 1/(1+np.exp(-h))
def error(i,s):
    return x[i][4]-s
def loss(e):
    return e**2
def deltaq0(i,s):
    return 2*(x[i][4]-s)*(1-s)*s*x[i][0]
def deltaq1(i,s):
    return 2*(x[i][4]-s)*(1-s)*s*x[i][1]
def deltaq2(i,s):
    return 2*(x[i][4]-s)*(1-s)*s*x[i][2]
def deltaq3(i,s):
    return 2*(x[i][4]-s)*(1-s)*s*x[i][3]
def deltab(i,s):
    return 2*(x[i][4]-s)*(1-s)*s*1
def newq0(tq0,a,dq0):
    return tq0+(a*dq0)
def newq1(tq1,a,dq1):
    return tq1+(a*dq1)
def newq2(tq2,a,dq2):
    return tq2+(a*dq2)
def newq3(tq3,a,dq3):
    return tq3+(a*dq3)
def newb(tb,a,db):
    return tb+(a*db)
for i in range(0, len(x)):
    tq0=q0();tq1=q1();tq2=q2();tq3=q3();tb=b()
    for j in range (0,n):
        h=ha(tq0,tq1,tq2,tq3,tb,i)
        s=sigmoid(h)
        e=error(i,s)
        ls[i][j]=loss(e)
        dq0=deltaq0(i,s)
        dq1=deltaq1(i,s)
        dq2=deltaq2(i,s)
        dq3=deltaq3(i,s)
        db =deltab(i,s)
        nq0=newq0(tq0,a,dq0)
        nq1=newq1(tq1,a,dq1)
        nq2=newq2(tq2,a,dq2)
        nq3=newq3(tq3,a,dq3)
        nb=newb(tb,a,db)
        tq0=nq0;tq1=nq1;tq2=nq2;tq3=nq3;tb=nb
        
ls = np.asarray(ls)
epoch = np.arange(0, n).reshape(1,n)
data = np.arange(0,len(x)).reshape(1,len(x))
l=ls[0][epoch]
pl.plot(np.array(epoch.T),np.array(l.T))