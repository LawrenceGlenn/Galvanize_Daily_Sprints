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

"""

Given an integer numpy array of 0's and 1's, write a function that creates a new array where 0's are replaced with the word "red" and 1's are replaced with the word "blue".

x = np.array([0, 0, 1, 0, 1]) 
color_replace(x)
    => np.array(["red", "red", "blue", "red", "blue"])

"""
def color_replace(x):
    x = np.where(x==0, "red", "blue")
    return x

"""

Given two equal length arrays, x with some general numeric data, and b an array of booleans, write a function that computes the sum of the data in x at the same positions where b is True, and the sum of the values in x at the positions where b is false.

x = np.array([0,    1,    2,     3,    4,     5])
b = np.array([True, True, False, True, False, False])
compute_true_false_sums(x, b)
    => {True: 4, False: 11}

"""

def compute_true_false_sums(x,b):
    return {True: np.sum(x[b]), False: np.sum(x[np.invert(b)])}
