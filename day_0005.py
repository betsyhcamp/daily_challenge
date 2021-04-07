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
# **Problem Statement (Python morsels: excercise called "count_words")**
#
# Write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.
#
# Your function should work like this:
#
#
# count_words("oh what a day what a lovely day")
#
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
#
#
#
# count_words("don't stop believing")
#
# {"don't": 1, 'stop': 1, 'believing': 1}
#
#
# **Bonus 1**
#
# As a bonus, make sure your function works well with mixed case words:
#
# count_words("Oh what a day what a lovely day")
#
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
#
# **Bonus 2**
#
# For even more of a bonus try to get your function to ignore punctuation outside of words:
#
# count_words("Oh what a day, what a lovely day!")
#
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

# %%
def count_words(string):
    split_list = string.split(' ')
    dict_count = dict.fromkeys(split_list,0)
    for word in split_list:
        count = dict_count[word]
        count += 1
        dict_count[word] = count
    return dict_count


# %%
count_words('oh what a day what a lovely day')


# %%
# bonus 1: works on mixed case
def count_words(string):
    split_list = string.lower().split(' ')
    dict_count = dict.fromkeys(split_list,0)
    for word in split_list:
        count = dict_count[word]
        count += 1
        dict_count[word] = count
    return dict_count


# %%
count_words('don"t what a day what a lovely day')


# %%
# bonus 2: works on mixed case and with puctuation outside words
def count_words(string_in):
    import re
    import string
    string_in = string_in.encode('ascii', 'ignore')
    string_in = string_in.decode()
    split_list = [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w)
                  for w in string_in.lower().split()]
    dict_count = dict.fromkeys(split_list,0)
    for word in split_list:
        count = dict_count[word]
        count += 1
        dict_count[word] = count
    return dict_count


# %%
count_words("¿te don't a day what a lovely day!")

# %%
