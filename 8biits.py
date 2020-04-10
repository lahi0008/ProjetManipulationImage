# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:20:36 2020

@author: papico
"""

import matplotlib.image as mpimg 
import numpy as np 


image=mpimg.imread("babouin.png")

from scipy.ndimage import convolve
img = mpimg.imread("babouin.png") 
kernel = np.array([[1/8,1/8,1/8],[1/8,0,1/8],[1/8,1/8,1/8]])
img_conv = convolve(img, kernel, mode="constant")
mpimg.imsave("flourapide-hibiscus.png", img_conv, cmap="gray")

a=1