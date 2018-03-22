# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:46:35 2018

@author: IC020549
"""

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()