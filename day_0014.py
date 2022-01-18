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
# ### Python question
# Given a list of numbers nums and an integer window_size, write a function moving_window to find the moving window average.
#
# Example:
#
# ``` python
# nums = [1,2,3,4,5,6]
# window_size = 3
# def moving_window(input, window_size) -> [1, 1.5, 2, 3, 4, 5]
#
# nums = [1,2,3,4,5,6]
# window_size = 4
# def moving_window(input, window_size) -> [1, 1.5, 2, 2.5, 3.5, 4.5]
# ```
#

# %%
def moving_window(input_list,window_size):
    result = []
    for idx, item in enumerate(input_list):
        start_idx = (idx + 1) - window_size
        end_idx = idx + 1
        if start_idx < 0:
            sub_list = input_list[: end_idx]
        else:
            sub_list = input_list[start_idx : end_idx]
    
        average = sum(sub_list)/len(sub_list)
        result.append(average)
    return result


# %%
# check w/ 1st given inputs
nums = [1,2,3,4,5,6]
window_size = 3
print(moving_window(nums,window_size))

# %%
# check w/ 2nd given inputs
nums = [1,2,3,4,5,6]
window_size = 4
print(moving_window(nums,window_size))

# %% [markdown]
# ### SQL question
# Find the details of each customer regardless of whether the customer made an order. 
# Output the customer's first name, last name, and the city along with the order details.
# You may have duplicate rows in your results due to a customer ordering several of the same items. 
# Sort records based on the customer's first name and the order details in ascending order.

# %% [markdown]
# My query answer:
#
# ``` sql
# SELECT first_name,
#        last_name,
#        city,
#        order_details
# FROM customers AS c
# LEFT JOIN orders AS o
# ON c.id = o.cust_id
# ORDER BY first_name, order_details
# ```
