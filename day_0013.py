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
# ### Problem Statement:
# Write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) with adjacent duplicate values removed.
#
# For example:
# ```python
# >>> compact([1, 1, 1])
# [1]
# >>> compact([1, 1, 2, 2, 3, 2])
# [1, 2, 3, 2]
# >>> compact([])
# []
# ```
# There are two bonuses for this exercise.
#
# #### Bonus 1
#
# For the first bonus, make sure you accept any iterable as an argument, not just a sequence (which means you can't use index look-ups in your answer). 
#
# Here's an example with a generator expression, which is a lazy iterable:
# ```python
# >>> compact(n**2 for n in [1, 2, 2])
# [1, 4]
# ```
#
# #### Bonus 2
#
# As a second bonus, make sure you return an iterator from your compact function instead of a list. 
#
# ```python
# >>> c = compact(n**2 for n in [1, 2, 2])
# >>> iter(c) is c
# True
# ```
#
# This should allow your compact function to accept infinitely long iterables (or other lazy iterables).

# %%
from itertools import tee
def compact(in_list):
    
    result = []
    it = iter(in_list)
    it, it2 = tee(it)
    
    try:
        next(it2)
    except:
        return result
    
    for ind, (previous, item) in enumerate(zip(it, it2)):
        if ind == 0:
            result.append(previous)
        if previous != item:
            result.append(item)
            
    return result


# %%
compact([1, 1, 1])

# %%
compact([1, 1, 2, 2, 3, 2])

# %%
compact([1,1])

# %%
compact(n**2 for n in [1, 2, 2])
