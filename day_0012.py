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
# ### Problem Statement
#
# Write a function that will accept paragraphs of text as input and will return that text wrapped at the end of each sentence.
#
# Your semantic_wrap function should work like this:
#
# semantic_wrap("Sentence one. Sentence two. Sentence three.")  
# 'Sentence one.\nSentence two.\nSentence three.'  
#
# ### Bonus 1
#
# For the first bonus, make sure you handle sentences separated by more than one space character and sentences that end in ? or !:
#
# print(semantic_wrap("What?  No!  Eh, maybe."))  
# What?  
# No!   
#
# Eh, maybe.  
#
# ### Bonus 2
#
# For the second bonus, create a command-line interface for this function. Your module, semantic_wrap.py should accept a filename as a command-line argument and should print out the "wrapped" version of that file.
#
# Given the file my_file.txt:
#
# I teach Python.  Online.  In-person.  In outer space?
#
# Just kidding, I only teach Python on Earth.  
# $ python semantic_wrap.py my_file.txt  
# I teach Python.  
# Online.  
# In-person.  
# In outer-space?  
#  
# ### Bonus 3
#
# For the third bonus, try to make sure your program can end with quotations just outside the end of your sentences:
#
# print(semantic_wrap('This sentence has "quoted text." This one does not.'))  
# This sentence has "quoted text."  
# This one does not.  
#

# %%
# base problem
def semantic_wrap(string):
    string_split = ['\n'+ sentence.strip()+'.' 
                    for sentence in string.split('.') 
                    if sentence != '']
    string_out =''
    return string_out.join(string_split)



# %%
# base problem
def semantic_wrap(string):
    return string.replace('. ', '.\n')


# %%
semantic_wrap("Sentence one. Sentence two. Sentence three.")


# %% [markdown]
# Description:
#
# Some new cashiers started to work at your restaurant.
#
# They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
#
# All the orders they create look something like this:
#
# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
#
# The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
#
# Their preference is to get the orders as a nice clean string with spaces and capitals like so:
#
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
#
# The kitchen staff expect the items to be in the same order as they appear in the menu.
#
# The menu items are fairly simple, there is no overlap in the names of the items:
#
# 1. Burger
# 2. Fries
# 3. Chicken
# 4. Pizza
# 5. Sandwich
# 6. Onionrings
# 7. Milkshake
# 8. Coke

# %%
def get_order(order):
    
    menu = ['burger',
            'fries',
            'chicken',
            'pizza',
            'sandwich',
            'onionrings',
            'milkshake',
            'coke']
    dict_count = dict.fromkeys(menu,0)
    i =3
    while len(order)>0:
        i+=1
        if order[:i] in menu:
            word = order[:i]
            count =dict_count[word]
            count+=1
            dict_count[word]=count
            order = order[i:]
            i = 3
    result = []
    for key, value in dict_count.items():
        for repeat in range(value):
            result.append(key.capitalize())  
    return ' '.join(result)


# %%
get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
