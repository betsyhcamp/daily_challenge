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
# Problem description:(From pythonmorsels.com)
#
#  I'd like you to compare the date strings, but allow invalid dates while comparing them.
#
# I want you to write a function that takes two strings representing dates and returns the string that represents the earliest point in time. The strings are in the US-specific MM/DD/YYYY format... just to make things harder. Note that the month, year, and day will always be represented by 2, 4, and 2 digits respectively.
#
# Your function should work like this:
#
# get_earliest("01/27/1832", "01/27/1756")
# '01/27/1756'
#
# get_earliest("02/29/1972", "12/21/1946")
# '12/21/1946'
#
# get_earliest("02/24/1946", "03/21/1946")
# '02/24/1946'
#
# get_earliest("06/21/1958", "06/24/1958")
# '06/21/1958'
#
#
# There's a catch though. Your exercise should work with invalid month and date combinations. What I mean by that is that dates like 02/40/2006 should be supported. By that I mean 02/40/2006 is before 03/01/2006 but after 02/30/2006 (dates don't roll over at all). I'm adding this requirement so you can't rely on Python's datetime module.
#
# There are many ways to solve this. See if you can figure out the clearest and most idiomatic way to solve this exercise. 
#
#
# Bonus
#
# If you complete the main exercise, there's also a bonus for you to attempt: allow the function to accept any number of arguments and return the earliest date string of all provided. ✔️
#
# So if you complete the bonus, this should work:
#
# get_earliest("02/24/1946", "01/29/1946", "03/29/1945")
# '03/29/1945'

# %%
def get_earliest(date_1, date_2):
    list_1 = date_1.split('/')
    list_2 = date_2.split('/')
    
    if list_1[2] != list_2[2]:
        if list_1[2] < list_2[2]:
            return date_1
        
        else:
            return date_2
        
    elif list_1[0] != list_2[0]:
        if list_1[0] < list_2[0]:
            return date_1
        
        else:
            return date_2
        
    else:
        if list_1[1] < list_2[1]:
            return date_1
        
        else:
            return date_2


# %%
get_earliest("01/27/1832", "01/27/1756")


# %%
def get_earliest(*args):
    split_in =[item.split('/') for item in args]
    years = [item[2] for item in split_in]
    min_years=min(years)
    dup_years = [i for i, item in enumerate(years) if item == min_years]
    if len(dup_years)==1:
        print('a', args[dup_years[0]])
        return args[dup_years[0]]
    
    else:
        list_subset = [args[i] for i in dup_years]
        split_subset = [item.split('/') for item in list_subset]
        print(list_subset)
        months_subset = [item[0] for item in split_subset]
        min_months = min(months_subset)
        dup_months = [i for i, item in enumerate(months_subset) if item == min_months]
        print(dup_months)
        if len(dup_months) ==1:
            print('b', list_subset[dup_months[0]])
            return list_subset[dup_months[0]]
        else:
            list_subset2 = [list_subset[i] for i in dup_months]
            print(list_subset2)
            split_subset2 = [item.split('/') for item in list_subset2]
            days_subset = [item[1] for item in split_subset2]
            min_day = min(days_subset)
            dup_days = [i for i, item in enumerate(days_subset) if item == min_day]
            print('c', list_subset2[dup_days[0]])
            return list_subset2[dup_days[0]]


# %%
get_earliest('02/30/2006', '02/29/2006')
