# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ### Problem Statement
#
# Write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.
#
# It should work something like this:
#
# matrix1 = [[1, -2], [-3, 4]]  
# matrix2 = [[2, -1], [0, -1]]  
# add(matrix1, matrix2)  
# [[3, -3], [-3, 3]]  
#
# matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]  
# matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]    
# add(matrix1, matrix2)  
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]  
#
# Try to solve this exercise without using any third-party libraries (without using pandas for example).
#
# Before attempting any bonuses,put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.
#
# There are two bonuses for this exercise.
#
# ### Bonus 1
#
# For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️
#
# matrix1 = [[1, 9], [7, 3]]   
# matrix2 = [[5, -4], [3, 3]]   
# matrix3 = [[2, 3], [-3, 1]]  
# add(matrix1, matrix2, matrix3)    
# [[8, 8], [7, 7]]  
#
# ### Bonus 2
#
# For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️
#
# add([[1, 9], [7, 3]], [[1, 2], [3]])     
# Traceback (most recent call last):  
#   File "<stdin>", line 1, in <module>  
#   File "add.py", line 10, in add  
#     raise ValueError("Given matrices are not the same size.")  
# ValueError: Given matrices are not the same size.  
#

# %%
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

# %%
# solution 1 to base problem
result = []
for row1, row2 in zip(matrix1,matrix2):
    row_temp = []
    for item1, item2 in zip(row1,row2):
        row_temp.append(item1+item2)
    result.extend(row_temp)

# %%
# solution 2 to base problem
result = []
for row1, row2 in zip(matrix1,matrix2):
    row_temp = [item1+item2 
                for item1, item2 in zip(row1,row2)]
    result.extend(row_temp)

# %%
# solution 3 to base problem
result = [[item1+item2 
           for item1, item2 in zip(row1,row2)]
           for row1,row2 in zip(matrix1, matrix2)]

# %%
result


# %%
def add(matrix1, matrix2):
    result = [[item1+item2 
           for item1, item2 in zip(row1,row2)]
           for row1,row2 in zip(matrix1, matrix2)]
    return result


# %%
add(matrix1, matrix2)

# %%
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]


# %%
# solution 1 to bonus 1
def add(*matrices):
    result = []
    for rows in zip(*matrices):
        row_temp = []
        for items in zip(*rows):
            row_temp.append(sum(items))
        result.append(row_temp)
    return result


# %%
# solution 2 to bonus 1
def add(*matrices):
    result = []
    for rows in zip(*matrices):
        row_temp = [sum(items) for items in zip(*rows)]
        result.append(row_temp)
    return result


# %%
# solution 3 to bonus 1
def add(*matrices):
    result = [[sum(items) 
               for items in zip(*rows)]
               for rows in zip(*matrices)]
    return result


# %%
add(matrix1, matrix2, matrix3)
