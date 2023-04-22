# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:04:52 2022

@author: Nenchin
"""
import matplotlib.pyplot as plt
import numpy as np
def gradientDescent(X,y):
    m_curr = b_curr = 0
    iteration = 10
    n = len(X)
    learning_rate = 0.08
    for i in range(iteration):
        y_predicted = m_curr * X + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        m_D = -(2/n)*sum(X*(y-y_predicted))
        b_D = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * m_D
        b_curr = b_curr - learning_rate * b_D
        print('m {}, b {}, cost {}, iteration {}'.format(m_curr, b_curr,
                                                         cost,i))

X = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])


gradientDescent(X,y)
plt.plot(X,y)