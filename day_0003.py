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


# %% [markdown]
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
#
# Examples:
#
# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

# %%
def iq_test(number_str):
    arr = number_str.split(' ')
    class_list = ['even' if float(item) %2 ==0 else 'odd' for item in arr]
    dict_count = dict.fromkeys(class_list, 0)
    for even_odd in class_list:
        val = dict_count[even_odd]
        val += 1
        dict_count[even_odd] = val
    
    for key, val in dict_count.items():
        if val==1:
            unique = key
    return class_list.index(unique) + 1


# %%
iq_test("2 4 7 8 10")


# %%
def iq_test2(number_str):
    even = [int(item) % 2 == 0 for item in number_str.split()]
    if even.count(True)==1:
        return even.index(True) + 1
    else:
        return even.index(False) + 1
    


# %%
iq_test2("2 4 7 8 10")
