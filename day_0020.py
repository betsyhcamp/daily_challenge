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
# ## Python exercise
# ### Problem statement:
# Given a list of strings of letters from 'a' to 'z', create a function, sum_alphabet, that returns a list of the alphabet sum of each word in the string.
#
# The alphabet sum is the sum of the ordinal position of each of the string’s letters in the standard English alphabet ordering. So, the letter 'a' will have a value of 1, 'z' will have a value of 26 and so on.
#
# As an example of the alphabet sum of a string, the string 'sport' will have an alphabet sum of 19 + 16 + 15 + 18 + 20 = 88.
#
# **Example**
#
# **Input:**
# ``` python
# words = ["sport" , "good" , "bad"]
# ```
# **Output:**
# ``` python
# def sum_alphabet(words) -> [88 , 41 , 7]
# ```

# %%
def sum_alphabet(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = [letter for letter in alphabet]
    scores = []
    for word in words:
        score = 0
        for letter in word:
            score += (alphabet_list.index(letter)+1)
        scores.append(score)
    return scores


# %%
words = ["sport" , "good" , "bad"]
sum_alphabet(words)

# %% [markdown]
# ## SQL exercise:
# ### Problem statement:
# Count the number of users who made more than 5 searches in August 2021.
#
# Table structure for fb_searches:
#
# | column       | data type  |
# |--------------|------------|
# | date         | datetime   |
# | search_id    | int        |
# | user_id      | int        |
# | age_group    | varchar    |
# | search_query | varchar    |
#
#
# ### Solution:
# ``` sql
# WITH searches AS (
# SELECT user_id,
#        COUNT(*) as count_searches
# FROM fb_searches
# WHERE EXTRACT(MONTH FROM date) = 8
#       AND EXTRACT(YEAR FROM date) = 2021 
# GROUP BY user_id
# HAVING COUNT(*) >5
# )
# SELECT COUNT(*) count_users
# FROM searches
# ```
#
#

# %%
