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
# ## SQL problem 1 - problem statement:
#
#
# Count the number of movies that Abigail Breslin was nominated for an oscar.
#
# Table structure for: oscar_nominees
#
# |Column    | Data type  |
# |----------|------------|
# | year     | float      |
# | category | varchar    |
# | nominee  | varchar    |
# | movie    | varchar    |
# | winner   | bool       |
# | id       | int        |
#
# ### SQL problem 1 answer: 
#
# ``` sql
# SELECT COUNT(DISTINCT movie) AS number_movies
# FROM oscar_nominees
# WHERE nominee = 'Abigail Breslin';
# ```
#
#
#
#
# ## SQL problem 2 - problem statement:
#
#
# Find employees in the Sales department who achieved a target greater than 150.
# Output first names of employees.
# Sort records by the first name in descending order.
#
# Table structure for: employee
#
# | Column         | Data type  |
# |----------------|------------|
# | id             | int        |
# | first_name     | varchar    |
# | last_name      | varchar    |
# | age            | int        |
# | sex            | varchar    |
# | employee_title | varchar    |
# | department     | varchar    |
# | salary         | int        |
# | target         | int        |
# | bonus          | int        |
# | email          | varchar    |
# | city           | varchar    |
# | address        | varchar    |
# | manager_id     | int        |
#
# ### SQL problem 2 answer: 
#
# ``` sql
# SELECT first_name
# FROM employee
# WHERE target > 150
#       AND department = 'Sales'
# ORDER BY first_name DESC;
# ```

# %% [markdown]
# ## Python problem - problem statement:
#
# Given a sorted list of positive integers with some entries being None, create a function to return a new list where all None values are replaced with the most recent non-None value in the list.
#
# Note: If the first entry in the list is None, assume the previous entry was 0.
#
# Example:
#
# Input
#
# ``` python
# input_list = [1,2,None,None,4,5,None]
#
# ```
#
# Output
# ``` python
# def fill_none(input_list) -> [1,2,2,2,4,5,5] 
# ```

# %%
input_list = [1,2,None,None,4,5,None]


# %%
def fill_none(input_list):
    # set initial value of previous non-None
    previous = 0
    # initialize list to output
    output_list =[]
    
    # iterate through each element in the input list; replacing None values
    for item in input_list:
        if item is None:
            output_list.append(previous)
        else:
            output_list.append(item)
            previous = item
    return output_list


# %%
fill_none(input_list)
