"""
Create a function named calculate() in mean_var_std.py that uses Numpy to 
output the mean, variance, standard deviation, max, min, and sum of the rows, 
columns, and elements in a 3 x 3 matrix. The input of the function should be 
a list containing 9 digits. The function should convert the list into a 3 x 3 
Numpy array, and then return a dictionary containing the mean, variance, 
standard deviation, max, min, and sum along both axes and for the flattened matrix.
The returned dictionary should follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

References:
https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator
"""

import numpy as np

mat = np.zeros((3, 3))
mat + l

l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
np.array(l).reshape(3, 3)

def calculate(l):   # l sholud be a 9 digits list

    # initialize matrix on which we will do calculations on:
    matr = np.array(l).reshape(3, 3)

    # initialize results objects:
    diz = {}
    diz['mean'], diz['var'], diz['std'], diz['max'], diz['min'], diz['sum'] = [[], [],], [[], [],], [[], [],], [[], [],], [[], [],], [[], [],]

    # loop for calculate over matrix rows:
    for row in matr:
        diz['mean'][0].append(row.mean())
        diz['var'][0].append(row.var())
        diz['std'][0].append(row.std())
        diz['max'][0].append(row.max())
        diz['min'][0].append(row.min())
        diz['sum'][0].append(row.sum())
    
    # loop for calculate over matrix columns:
    for col in matr.transpose():
        diz['mean'][1].append(col.mean())
        diz['var'][1].append(col.var())
        diz['std'][1].append(col.std())
        diz['max'][1].append(col.max())
        diz['min'][1].append(col.min())
        diz['sum'][1].append(col.sum())
    
    # flattened values:
    diz['mean'].append(matr.mean())
    diz['var'].append(matr.var())
    diz['std'].append(matr.std())
    diz['max'].append(matr.max())
    diz['min'].append(matr.min())
    diz['sum'].append(matr.sum())

    return diz

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])