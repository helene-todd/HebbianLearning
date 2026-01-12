#! /usr/bin/env python3

'''
PROBLEM 3
'''

import random as rand
import numpy as np
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy.ma as ma
import os
from PIL import Image

rand.seed(42)

plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 18#9
plt.rcParams['legend.fontsize'] = 12#7.
plt.rcParams['lines.markersize'] = 5
plt.rcParams['axes.labelsize'] = 18#9
plt.rcParams['axes.labelpad'] = 10
plt.rcParams['axes.linewidth'] = '0.4'
plt.rcParams['font.serif'] = 'Helvetica'

path = 'Figs'
if not os.path.isdir(path) :
    os.makedirs(path)

dir1 = 'Figs/Qu_b'
if not os.path.isdir(dir1) :
    os.makedirs(dir1)

dir2 = 'Figs/Qu_c'
if not os.path.isdir(dir2) :
    os.makedirs(dir2)

for k in range(3,11):
    dir = f'Figs/Qu_d/{k}_el' #k elements folder
    if not os.path.isdir(dir) :
        os.makedirs(dir)

def colorFader(c1,c2,mix=0):
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

# Pastels (look bad with background)
purple = '#a885ee'
blue = '#67d0dd'
green = '#9fe481'
yellow = '#f6e785'
orange = '#faafa5'
red = '#dc95dd'

# Maybe try better colours
dark_blue = '#0011da'
dark_purple = '#5c00da'

# Life In Color Color Scheme
palatinate_purple = '#62275D'
dingy_dungeon = '#C32C57'
beer = '#F38F1D'
minion_yellow = '#F5EC50'
harlequin_green = '#67D120'
celtic_blue = '#2E6FCC'


def f(vector) :
    result = []
    for el in vector :
        if el < 0 :
            result.append(-1)
        elif el >= 0 :
            result.append(1)
    return np.array(result)

def euler_one_step(x, W):
    return x + (-x + f(np.dot(W,x)))*dt + 0.1*rand.gauss(0,dt)

def pattern(path, n, colorbar=False):
    pic = Image.open(path)
    pix = np.flip(np.array(pic.getdata()))

    pattern = []
    for pixel in pix :
        pattern.append(1 if np.array_equal(pixel, [255,255,255,255]) else -1)

    pattern = np.array(pattern)
    return pattern

def output(pattern, n, size, colorbar=False):
    plt.figure(figsize=size)
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(pattern, (8,8)), cmap='viridis')
    if colorbar == True :
        cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=34)
    cbar.set_ticks([-1,0,1])
    plt.axis('off')
    plt.savefig(f'Figs/pattern_{n}.png', dpi=600)
    plt.close()

'''
Question a
'''

# Pattern 1
pattern_1 = pattern('tamagotchis/mametchi.png', 1)
output(pattern_1, 1, size=(9,8), colorbar=True)

'''
Question b
'''
"""
#simulation 1
dt = 0.1
W = (1/64)*np.outer(pattern_1, pattern_1.T)

x = -1*np.ones(64)

for i in range(len(x)) :
    if rand.random() < 0.3 :
        x[i] = 1

for k in range(40) :
    plt.figure(figsize=(8,8))
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    plt.axis('off')
    #plt.savefig(f'Figs/Qu_b/sim1_{k+1}.png', dpi=600)
    plt.close()
    x = euler_one_step(x,W)

#simulation 2
dt = 0.1
W = (1/64)*np.outer(pattern_1, pattern_1.T)

x = -1*np.ones(64)

for i in range(len(x)) :
    if rand.random() < 0.6 :
        x[i] = 1

for k in range(40) :
    plt.figure(figsize=(8,8))
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    plt.axis('off')
    #plt.savefig(f'Figs/Qu_b/sim2_{k+1}.png', dpi=600)
    plt.close()
    x = euler_one_step(x,W)
"""

'''
Question c
'''

# Pattern 2
pattern_2 = pattern('tamagotchis/kuchipatchi.png', 2)

"""
dt = 0.1
W = (1/64)*(np.outer(pattern_1, pattern_1.T) + np.outer(pattern_2, pattern_2.T))

# close to p
x = pattern_1
for i in range(len(x)) :
    if rand.random() < 0.25 :
        x[i] = -x[i]

for k in range(40) :
    plt.figure(figsize=(8,8))
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    plt.axis('off')
    plt.savefig(f'Figs/Qu_c/sim1_{k+1}.png', dpi=600)
    plt.close()
    x = euler_one_step(x,W)

# close to -p
x = pattern_1
for i in range(len(x)) :
    if rand.random() < 0.75 :
        x[i] = -x[i]

for k in range(40) :
    plt.figure(figsize=(8,8))
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    plt.axis('off')
    plt.savefig(f'Figs/Qu_c/sim2_{k+1}.png', dpi=600)
    plt.close()
    x = euler_one_step(x,W)

#close to q
x = pattern_2
for i in range(len(x)) :
    if rand.random() < 0.25 :
        x[i] = -x[i]

for k in range(40) :
    plt.figure(figsize=(8,8))
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    plt.axis('off')
    plt.savefig(f'Figs/Qu_c/sim3_{k+1}.png', dpi=600)
    plt.close()
    x = euler_one_step(x,W)

# close to -q
x = pattern_2
for i in range(len(x)) :
    if rand.random() < 0.75 :
        x[i] = -x[i]

for k in range(40) :
    plt.figure(figsize=(8,8))
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    plt.axis('off')
    plt.savefig(f'Figs/Qu_c/sim4_{k+1}.png', dpi=600)
    plt.close()
    x = euler_one_step(x,W)
"""

'''
Question d
'''

# Pattern 3
pattern_3 = pattern('tamagotchis/maskutchi.png', 3)

# Pattern 4
pattern_4 = pattern('tamagotchis/pyonkotchi.png', 4)

# Pattern 5
pattern_5 = pattern('tamagotchis/imotchi.png', 5)

# Pattern 6
pattern_6 = pattern('tamagotchis/tsubutchi.png', 6)

# Pattern 7
pattern_7 = pattern('tamagotchis/tsunotchi.png', 7)

# Pattern 8
pattern_8 = pattern('tamagotchis/ichigotchi.png', 8)

# Pattern 9
pattern_9 = pattern('tamagotchis/mohitamatchi.png', 9)

# Pattern 10
pattern_10 = pattern('tamagotchis/teletchi.png', 9)
output(pattern_10, 10, size=(9,8), colorbar=True)

dt = 0.1

'''
-> interesting to use same initial condition for each simulation to compare.
initial condition will be very close to pattern
'''

p = [pattern_1, pattern_2, pattern_3, pattern_4, pattern_5, pattern_6, pattern_7, pattern_8, pattern_9, pattern_10]

# list with initial conditions close to pattern
x_init = []
for pattern in p:
    x = pattern.copy() # otherwise, passed as reference
    for i in range(len(x)) :
        if rand.random() < 0.06 :
            x[i] = -x[i]
    x_init.append(x)

for x in x_init :
    plt.pcolor([k for k in range(9)], [k for k in range(9)], np.reshape(x, (8,8)), cmap='viridis')
    #plt.show()
'''
storing k patterns (some are similar to others), note that addind tetechi in the inital 2 patterns already leads to
mistakes in its retrieval, even for very close initial conditions. likely to be because patterns 1&3 are similar.
'''

# k is number of patterns
for k in range(5,6):
    print(f"we're at {k} patterns")

    W = 0
    for j in range(k):
        W += np.outer(p[j], p[j].T)
    W = (1/64)*W

    for j in range(k):
        x = x_init[j] #starting pattern is exactly the pattern.

        for t in range(80) :
            plt.figure(figsize=(8,8))
            plt.pcolor([n for n in range(9)], [n for n in range(9)], np.reshape(x, (8,8)), cmap='viridis')
            plt.axis('off')
            plt.savefig(f'Figs/Qu_d/{k}_el/sim{j+1}_{t+1}.png', dpi=600)
            plt.close()
            x = euler_one_step(x,W)
