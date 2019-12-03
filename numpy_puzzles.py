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
"""

Write a function that selects from one of two arrays based on the value in another boolean array.

x = np.array([1,    2,    3,     4,    5,     6])
y = np.array([10,   20,   30,    40,   50,    60])
b = np.array([True, True, False, True, False, True])
select_from_two_arrays(x, y, b):
    => np.array(1, 2, 30, 4, 50, 6])

"""

def select_from_two_arrays(x,y,b):
    return np.where(b, x, y)

"""

Write a function that compute the sum of squared differences between two arrays:

x = np.array([0, 1, 0, 1, 0, 1])
y = np.array([0, 1, 2, 3, 4, 5])
sum_of_squared_differences(x, y)
    => 40

"""


def sum_of_squared_differences(x,y):
    return np.sum((x-y)**2)


""" 

Write a function that consumes a two-dimensional numpy array (so, a matrix), and a label which is either "row" or "column". The function should return a one-dimensional numpy array (vector) with either the row or column averages.

X = np.array([[0, 1], [2, 1]])
row_or_column_means(X, label="row")
    => np.array([0.5, 1.5])
row_or_column_means(X, label="column")
    => np.array([1.0, 1.0])

"""

def row_or_column_means(x, label):
    if label == "column":
        ax = 0
    else:
        ax = 1
    return np.mean(x, axis=ax)

"""
Write a function that creates a square two-dimensional array of zeros, but with ones on the diagonals immediately below and above the main diagonal. For example, when n=5, you should create the following two-dimensional array

ones_above_and_below_diagonal(5)
    => np.array([
  [0, 1, 0, 0, 0],
  [1, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 0]
])

"""

def ones_above_and_below_diagonal(n):
    x = np.zeros((n,n), int)
    np.fill_diagonal(x[1:], 1)
    np.fill_diagonal(x[:, 1:], 1)
    return x
