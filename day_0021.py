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
# # Python Exercise
# ### Problem statement
# You are given a string that represents some floating-point number. Write a function, digit_accumulator, that returns the sum of every digit in the string.
#
# **Example**
#
# **Input**:
#     
# ``` python
# s = "123.0045"
# ```
#
# **Output**
#
# ``` python
# def digit_accumulator(s) -> 15
# Since 1 + 2 + 3 + 0 + 0 + 4 + 5 = 15
# ```

# %%
s =  "-123.0045"


# %%
def digit_accumulator(s):
    return sum([int(character) 
                for character in s 
                if character not in ['.', '-']])


# %%
digit_accumulator(s)

# %% [markdown]
# # SQL Exercise
# ### Problem Statement
# Return a list of users with status free who didn’t make any calls in Apr 2020.
#
# Table structure `rc_calls`
#
# | column    | data type  |
# |-----------|------------|
# | user_id   | int        |
# | date      | datetime   |
# | call_id   | int        |
#
#
# Table structure for `rc_users`
#
# | column     | data type  |
# |------------|------------|
# | user_id    | int        |
# | status     | varchar    |
# | company_id | int        |
#
#
# ### SQL solution
#
# ``` sql
# SELECT DISTINCT user_id
# FROM rc_users
# WHERE status = 'free'
#       AND user_id NOT IN (SELECT user_id
#                           FROM rc_calls
#                           WHERE EXTRACT(YEAR FROM date)=2020
#                                 AND EXTRACT(MONTH FROM date)=4)
# ```
