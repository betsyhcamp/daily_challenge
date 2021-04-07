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
# Problem Statment: (Codewars "multiplication table" kata):    
# Your task, is to create NxN multiplication table, of size provided in parameter.
#
# for example, when given size is 3:
#
# 1 2 3  
# 2 4 6   
# 3 6 9  
#
#
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

# %%
size = 3


# %%
def multiplication_table(size):
    l=[]
    for i in range(1, size+1):
        temp = []
        for j in range(1, size+1):
            temp.append(i * j)
        l.append(temp)
    return l


# %%
multiplication_table(3)

# %%
multiplication_table(2)
