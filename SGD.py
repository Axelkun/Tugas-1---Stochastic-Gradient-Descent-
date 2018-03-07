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
def tq0():
    return random.uniform(-1,1)
def tq1():
    return random.uniform(-1,1)
def tq2():
    return random.uniform(-1,1)
def tq3():
    return random.uniform(-1,1)
def tb():
    return random.uniform(-1,1)
a= float(input('enter alpha: '))
def ha(tq0,tq1,tq2,tq3,tb,i):
    return (tq0*x[i][0])+(tq1*x[i][1])+(tq2*x[i][2])+(tq3*x[i][3])+tb
def sigmoid(h):
    return 1.0/(1+np.exp(-h))
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
def newq(numb,a,theta):
    return numb+(a*theta)
def newb(tb,a,db):
    return tb+(a*db)
q0=tq0();q1=tq1();q2=tq2();q3=tq3();b=tb()
    #q0=0.2;q1=0.2;q2=0.2;q3=0.2;b=0.2
err=[]
for i in range (0,n):
   te=0
   for i in range (0,len(x)):
        h=ha(q0,q1,q2,q3,b,i)
        s=sigmoid(h)
        e=error(i,s)
        te+=e
        dt0=deltaq0(i,s);dt1=deltaq1(i,s);dt2=deltaq2(i,s);dt3=deltaq3(i,s)
        db=deltab(i,s)
        q0=newq(q0,a,dt0);q1=newq(q1,a,dt1);q2=newq(q2,a,dt2);q3=newq(q3,a,dt3)
        b=newb(b,a,db)
   err.append(te/100.0)
        
pl.plot(err)
pl.legend(['Accuracy'], loc='upper right')
pl.xlabel('Epoch')
pl.ylabel('Error')
pl.show()
