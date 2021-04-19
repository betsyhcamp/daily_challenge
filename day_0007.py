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
# ## Problem Statement: Python Morsels is_anagram
# This exercise includes 3 bonuses and 8 hints (hover over the hint links before clicking on them).
#
# Write a function that accepts two strings and returns True if the two strings are anagrams of each other.
#
# Your function should work like this:
#
# is_anagram("tea", "eat")   
# True  
#
# is_anagram("tea", "treat")  
# False  
#
# is_anagram("sinks", "skin")  
# False  
#
# is_anagram("Listen", "silent")  
# True  
#
# Make sure your function works with mixed case.
#
# Before you try to solve any bonuses, try to find at least two ways to solve this problem.
#
# Okay now to the bonuses...
#
# ### Bonus 1
#
# For the first bonus, make sure your function ignores spaces ✔️:
#
# is_anagram("coins kept", "in pockets")  
# True  
#
# ### Bonus 2
#
# For a second bonus, make sure your function also ignores punctuation ✔️:
#
# is_anagram("a diet", "I'd eat")  
# True  
#
# ### Bonus 3
#
# If you solved this one really quickly, here's a more challenging third bonus for you: try allowing accented latin1 characters but ignoring the accent marks. ✔️
#
# is_anagram("cardiografía", "radiográfica")  
# True  
#

# %%
def is_anagram(s1,s2):
    s2_list = [letter.lower() for letter in s2 if letter.isalpha()]
    s1_list = [letter.lower() for letter in s1 if letter.isalpha()]
    for letter in s1_list:
        if (len(s2_list)>0) and (letter in s2_list):
            s2_list.remove(letter)
        else:
            return False
    return len(s2_list)==0


# %%
def make_dict(word):
    word_dict = {}
    for letter in word.lower():
        if letter.isalpha():
            word_dict.setdefault(letter,0)
            word_dict[letter] += 1
                
    return word_dict

def is_anagram(word1, word2):
    return make_dict(word1) == make_dict(word2)
    


# %%
is_anagram("tea", "eat")

# %%
is_anagram("tea", "treat")

# %%
is_anagram("sinks", "skin")

# %%
is_anagram("Listen", "silent")

# %%
is_anagram("a diet", "I'd eat")

# %%
