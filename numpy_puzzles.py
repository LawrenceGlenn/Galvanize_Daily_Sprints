"""
Write a function that creates a column vector (an array of shape (n, 1)) containing the sequence of numbers 0, 1, 2, ..., n-1:

column_vector(3)
    => [[0], [1], [2]]

"""

import numpy as np
def column_vector(n):
    return np.linspace(0,n,n)



"""

Write a function that creates an array of random floating point numbers between zero and one of a given shape:

random_array(4, 3)
    => array([
        [ 0.30159734,  0.46366088,  0.78706666],
        [ 0.26946135,  0.80638833,  0.25265662],
        [ 0.82426648,  0.46202413,  0.20735323],
        [ 0.19923862,  0.4677537 ,  0.60799465]])

"""
def random_array(row,col):
    return np.random.rand(row,col)

