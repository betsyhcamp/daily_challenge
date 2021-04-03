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
# Problem Statement: (Source Codewars.com: Highest rank number in array)
#
# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.
#
# Note: no empty arrays will be given.

# %%
def highest_rank(arr):
    """Find most frequent number in array. If ties in frequency 
       return, largest number."""
    dict_count = dict.fromkeys(arr, 0)
    for item in arr:
            val = dict_count[item]
            val+=1
            dict_count[item] = val
        
    results = [(value,key) for key,value in dict_count.items()]
    max_result = max(results)
    _, num = max_result
    return num


# %%
input_list = [12, 10, 8, 12, 7, 6, 4, 10, 12]
highest_rank(input_list)
