#! /usr/bin/env python3

'''
MOSAIC
'''

import random as rand
import numpy as np
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy.ma as ma
import os
from PIL import Image

'''
Mosaics question a
'''
"""
fig, ax = plt.subplots(5,8, figsize=(8,6))

filenames=[f'Figs/Qu_b/sim1_{i+1}.png' for i in range(40)]
print(filenames)

t = 0
for i in range(5):
    for j in range(8):
        print(j+i*8)
        image=Image.open(open(filenames[j+i*8],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        ax[i][j].text(0.5,-0.15, f'$t = {round(t,1)}$', size=10, ha="center", #f'step {j+i*8+1}'
         transform=ax[i][j].transAxes)
        t+= .1

fig.tight_layout()
fig.savefig('figure_1.png', dpi=600)
plt.close()

fig, ax = plt.subplots(5,8, figsize=(8,6))

filenames=[f'Figs/Qu_b/sim2_{i+1}.png' for i in range(40)]
print(filenames)

t = 0
for i in range(5):
    for j in range(8):
        print(j+i*8)
        image=Image.open(open(filenames[j+i*8],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        ax[i][j].text(0.5,-0.15, f'$t = {round(t,1)}$', size=10, ha="center", #f'step {j+i*8+1}'
         transform=ax[i][j].transAxes)
        t+= .1

fig.tight_layout()
fig.savefig('figure_2.png', dpi=600)
"""

'''
Mosaics question b
'''
"""
fig, ax = plt.subplots(1, 9, figsize=(10,1.6))
time = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9]

for k in range(1,5):
    filenames = []
    filenames += [f'Figs/Qu_c/sim{k}_1.png']
    filenames += [f'Figs/Qu_c/sim{k}_{i*5}.png' for i in range(1,9)]
    print(filenames)

    t, j = 0, 0
    for name in filenames :
        image=Image.open(open(name,'rb'))
        ax[j].axis('off')
        ax[j].imshow(image)
        ax[j].text(0.5,-0.2, f'$t = {time[j]}$', size=10, ha="center",
         transform=ax[j].transAxes)
        t, j =  t+.1, j+1

    fig.tight_layout()
    fig.savefig(f'figure_{2+k}.png', dpi=600)
    plt.close()
"""
'''
Mosaics question d
'''

'''
All patterns mosaic
'''

fig, ax = plt.subplots(1, 9, figsize=(10,1.6))

filenames=[f'Figs/pattern_{i}.png' for i in range(1,10)]
print(filenames)

str = [f'$p_{k}$' for k in range(1,10)]+['$p_{10}$' ]
for i in range(1):
    for j in range(9):
        print(j)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[j].axis('off')
        ax[j].imshow(image)
        ax[j].text(0.5,-0.15, str[j], size=10, ha="center", #f'step {j+i*8+1}'
        transform=ax[j].transAxes)

fig.tight_layout()
fig.savefig('patterns.png', dpi=600)
plt.close()

'''
3 patterns
'''
"""
fig, ax = plt.subplots(3, 9, figsize=(10,4))
time = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9]

filenames = []
for k in range(1,4):
    filenames += [f'Figs/Qu_d/3_el/sim{k}_1.png']
    filenames += [f'Figs/Qu_d/3_el/sim{k}_{i*5}.png' for i in range(1,9)]

print(filenames)

for i in range(3):
    for j in range(9):
        print(j+i*9)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 2 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_7', dpi=600)
plt.close()
"""

'''
4 patterns
'''
"""
fig, ax = plt.subplots(4, 9, figsize=(10,5))
time = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9]

filenames = []
for k in range(1,5):
    filenames += [f'Figs/Qu_d/4_el/sim{k}_1.png']
    filenames += [f'Figs/Qu_d/4_el/sim{k}_{i*5}.png' for i in range(1,9)]

print(filenames)

for i in range(4):
    for j in range(9):
        print(j+i*9)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 3 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_8', dpi=600)
plt.close()
"""

'''
5 patterns
'''
"""
fig, ax = plt.subplots(5, 9, figsize=(10,6))
time = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9]

filenames = []
for k in range(1,6):
    filenames += [f'Figs/Qu_d/5_el/sim{k}_1.png']
    filenames += [f'Figs/Qu_d/5_el/sim{k}_{i*5}.png' for i in range(1,9)]

print(filenames)

for i in range(5):
    for j in range(9):
        print(j+i*9)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 4 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_9', dpi=600)
plt.close()
"""

'''
6 patterns
'''
"""
fig, ax = plt.subplots(6, 9, figsize=(10,6))
time = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9]

filenames = []
for k in range(1,7):
    filenames += [f'Figs/Qu_d/6_el/sim{k}_1.png']
    filenames += [f'Figs/Qu_d/6_el/sim{k}_{i*5}.png' for i in range(1,9)]

print(filenames)

for i in range(6):
    for j in range(9):
        print(j+i*9)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 5 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_10', dpi=600)
plt.close()
"""

'''
we've (kinf of) lost one pattern !
'''
"""
fig, ax = plt.subplots(1, 9, figsize=(10,1.6))
time = [0, 0.1, 0.5, 1.0, 1.5, 2.0, 3.0 , 4.0, 4.9]

filenames = [f'Figs/Qu_d/6_el/sim7_{int(t*10+1)}.png' for t in time]
print(filenames)

for j in range(9):
    print(j)
    image=Image.open(open(filenames[j],'rb'))
    ax[j].axis('off')
    ax[j].imshow(image)
    ax[j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
    transform=ax[j].transAxes)

fig.tight_layout()
fig.savefig('figure_11', dpi=600)
plt.close()
"""

'''
7 patterns
'''
"""
fig, ax = plt.subplots(7, 9, figsize=(10,7))
time = [0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.5, 4.9]

filenames = []
for k in range(1,8):
    filenames += [f'Figs/Qu_d/7_el/sim{k}_{int(t*10+1)}.png' for t in time]

print(filenames)

for i in range(7):
    for j in range(9):
        print(j+i*9)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 6 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_12', dpi=600)
plt.close()
"""

'''
we've lost two patterns!
'''
"""
fig, ax = plt.subplots(2, 9, figsize=(10,3))
time = [0, 1.0, 2.0, 4.0, 6.0, 7.0, 8.0, 9.0, 9.9]

filenames = [f'Figs/Qu_d/7_el/sim8_{int(t*10+1)}.png' for t in time]+[f'Figs/Qu_d/7_el/sim9_{int(t*10+1)}.png' for t in time]
print(filenames)

for i in range(2):
    for j in range(9):
        print(j)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 1 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_13', dpi=600)
plt.close()
"""

'''
8 patterns
'''
"""
fig, ax = plt.subplots(8, 9, figsize=(10,8))
time = [0, 1., 2., 3., 4., 5., 6., 7., 7.9]

filenames = []
for k in range(1,9):
    filenames += [f'Figs/Qu_d/8_el/sim{k}_{int(t*10+1)}.png' for t in time]

print(filenames)

for i in range(8):
    for j in range(9):
        print(j+i*9)
        image=Image.open(open(filenames[j+i*9],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 7 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_14', dpi=600)
plt.close()
"""

'''
9 patterns
'''
"""
fig, ax = plt.subplots(9, 10, figsize=(11,9))
time = [0,2.,4.,6.,8.,10.,12.,14.,16.,18.]

filenames = []
for k in range(1,10):
    filenames += [f'Figs/Qu_d/9_el/sim{k}_{int(t*10+1)}.png' for t in time]

print(filenames)

for i in range(9):
    for j in range(10):
        print(j+i*10)
        image=Image.open(open(filenames[j+i*10],'rb'))
        ax[i][j].axis('off')
        ax[i][j].imshow(image)
        if i == 8 :
            ax[i][j].text(0.5,-0.15, f'$t = {time[j]}$', size=10, ha="center", #f'step {j+i*8+1}'
            transform=ax[i][j].transAxes)

fig.tight_layout()
fig.savefig('figure_15', dpi=600)
plt.close()
"""
