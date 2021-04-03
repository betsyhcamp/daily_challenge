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
# Problem Statement: (Leetcode: Reverse string)
# Write a function that reverses a string. The input string is given as an array of characters s.
#
#  
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
#
# Output: ["o","l","l","e","h"]

# %%
def reverse_list(s):
    """Must reverse in place (i.e. nothing is returned)"""
    for i, item in enumerate(s):
        n = len(s) -(i+1)
        s.append(s[n])
        s.pop(n)    


# %%
s = ["h","e","l","l","o"]
reverse_list(s)
print(s)


# %%
def reverse_list2(s):
    """Must reverse in place (i.e. nothing is returned)"""
    s.reverse()


# %%
s = ["h","e","l","l","o"]
reverse_list2(s)
print(s)
