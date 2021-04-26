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
# ### Problem Statement:  
#
#
# Write a function which will take a percentage and convert it to a grade by using a specific flavor of the A-F grading system used in the US.
#
# The rules:
#
# Below 60 is F
# From 60 to below 70 is D
# From 70 to below 80 is C
# From 80 to below 90 is B
# 90 and above is A
#
# percent_to_grade(72.5)  
# 'C'
#
# percent_to_grade(89.6)  
# 'B'
#
# percent_to_grade(60)  
# 'D'
#
# percent_to_grade(100)  
# 'A'
#
# percent_to_grade(2)  
# 'F'
#
#
# ### Bonus 1
#
# For the first bonus I'd like you to allow a keyword-only suffix argument to be passed to your percent_to_grade function. When suffix is True, you should add - and + suffixes to the grade according to another set of rules:
#
# 97 and above is A+  
# From 93 to below 97 is A  
# From 90 to below 93 is A-  
# From 87 to below 90 is B+  
# From 83 to below 87 is B  
# From 80 to below 83 is B-  
# From 77 to below 80 is C+  
# From 73 to below 77 is C  
# From 70 to below 73 is C-  
# From 67 to below 70 is D+  
# From 63 to below 67 is D  
# From 60 to below 63 is D-  
# Below 60 is F (no + or -)  
#
# percent_to_grade(72.5, suffix=True)  
# 'C-'
#
# percent_to_grade(89.6, suffix=True)  
# 'B+'
#
# percent_to_grade(60, suffix=True)  
# 'D-'
#
# percent_to_grade(100, suffix=True)  
# 'A+'
#
# percent_to_grade(2, suffix=True)  
# 'F'
#
# ### Bonus 2
#
# For the second bonus, I'd like you to accept another optional keyword-only argument: round. When round is True you should round percentages to their nearest whole number before calculating grades, with .5 always rounding upward.
#
# percent_to_grade(69.4, round=True)  
# 'D'
#
# percent_to_grade(69.6, round=True)  
# 'C'
#
# percent_to_grade(72.5, suffix=True, round=True)  
# 'C'
#
# percent_to_grade(89.6, suffix=True, round=True)  
# 'A-'
#
# ### Bonus 3
#
# For the third bonus, I'd like you to create another function called calculate_gpa which accepts a sequence of letter grades and returns the grade point average based on the following rules:
#
# A+ is worth 4.33  
# A is worth 4.00  
# A- is worth 3.67  
# B+ is worth 3.33  
# B is worth 3.00  
# B- is worth 2.67  
# C+ is worth 2.33  
# C is worth 2.00  
# C- is worth 1.67  
# D+ is worth 1.33  
# D is worth 1.00  
# D- is worth 0.67  
# F is worth 0.00  
#
# calculate_gpa(['D+', 'C', 'A-', 'B'])   
# 2.5
#
# calculate_gpa(['B+', 'A', 'C+', 'F'])  
# 2.415
#

# %%
# brute force approach to base problem
def percent_to_grade(percent):
    if percent < 60:
        return 'F'
    elif percent < 70: 
        return 'D'
    elif percent < 80:
        return 'C'
    elif percent < 90:
        return 'B'
    else:
        return 'A'


# %%
percent_to_grade(2)


# %%
# slightly more refined approach to base problem
def percent_to_grade(percent):
    grade_cutoff = [60, 70, 80, 90, 1000]
    grade_letter =['F','D', 'C', 'B', 'A']
    for cutoff, letter in zip(grade_cutoff,grade_letter):
        if percent < cutoff:
            return letter
        elif percent > grade_cutoff[-2]:
            return grade_letter[-1]


# %%
percent_to_grade(90)


# %%
# build off 2nd approach to try to accomplish bonus 1 & 2
def percent_to_grade(percent, *, suffix=False, round = False):
    
    if suffix:
        grade_cutoff = [60, 63, 67, 70, 73, 77, 80, 83, 87, 90, 93, 97, 1000]
        grade_letter =['F','D-', 'D', 'D+','C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
    else:
        grade_cutoff = [60, 70, 80, 90, 1000]
        grade_letter =['F','D', 'C', 'B', 'A']
    if round:
        from decimal import Decimal, ROUND_HALF_UP
        percent = Decimal(percent).to_integral_value(rounding=ROUND_HALF_UP)
        
    for cutoff, letter in zip(grade_cutoff,grade_letter):
        if percent < cutoff:
            return letter
        elif percent > grade_cutoff[-2]:
            return grade_letter[-1]


# %%
percent_to_grade(0, suffix = True, round=True)

# %%
