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
# Given a string, write a function recurring_char to find its first recurring character. Return None if there is no recurring character.
#
# Treat upper and lower case letters as distinct characters.
#
# You may assume the input string includes no spaces.
#
# Example:
#
# ``` python
# input = "interviewquery"
# output = "i"
#
#
# input = "interv"
# output = None
# ```

# %%
# Solution function

def recurring_char(input):
    for ind, letter in enumerate(input):
        if ind ==0:
            pass
        elif letter in input[:ind]:
            return letter   
    return None


# %%
# spot check output
input = "interviewquery"
out = recurring_char(input)
print(out)

# %%
# spot check output
input = "interv"
out = recurring_char(input)
print(out)

# %% [markdown]
# # SQL Exercise
# ### Problem Statement:
# Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD.
# Output all details related to retrieved records.
#
#
# Table structure `lyft_drivers`:
#
# | column      | data type  |
# |-------------|------------|
# |index        | int        |
# |start_date   | datetime   |
# |end_date     | datetime   |
# |yearly_salary| int        |
#
# ### Sql solution:
#
# ``` sql
# SELECT *
# FROM lyft_drivers
# WHERE yearly_salary <= 30000
#       OR yearly_salary >= 70000;
# ```
