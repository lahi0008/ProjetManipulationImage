# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:24:15 2020

@author: papico
"""

from pylab import *
couleurs =['b','g','r','c','m','y','k','w']
x=[-1,0,1,2]
y=[3,2,4,1]

for c in couleurs:
    i=couleurs.index(c)+1
    subplot(2,4,i)
    plot(x,y,c+'-')
    
show()