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
# ## Python excercise
# ### Problem Statement:
# Given two lists of release dates, return the list with more dates past a certain input variable date D.
#
# Note: Both lists could be of unequal length and in any order.
#
# Example;
# ``` python
# D = "2020-03-01"
# L1 = [
#     "2020-01-21", 
#     "2020-01-09",
#     "2020-01-10",
#     "2020-02-14",
#     "2020-03-01"
# ]
# L2 = [
#     "2020-01-20", 
#     "2020-04-02",
#     "2020-02-08",
#     "2020-03-01"
# ]
#
#
# def greater_release_dates(L1, L2, D) -> L2
# ```
#
# ### Solution:

# %%
D = "2020-03-01"
L1 = [
    "2020-01-21", 
    "2020-01-09",
    "2020-01-10",
    "2020-02-14",
    "2020-03-01"
]
L2 = [
    "2020-01-20", 
    "2020-04-02",
    "2020-02-08",
    "2020-03-01"
]

# %%
from datetime import datetime
def date_count(D, list_in):
    date_limit = datetime.strptime(D, '%Y-%m-%d')
    count = 0
    for date in list_in:
        date_datetime = datetime.strptime(date, '%Y-%m-%d')
        if date_datetime > date_limit:
            count += 1
    return count

def greater_release_dates(L1, L2, D):
    count1 = date_count(D, L1)
    count2 = date_count(D, L2)
    if count1 > count2:
        return L1
    else:
        return L2


# %%
greater_release_dates(L1, L2, D)

# %% [markdown]
# ## SQL Exercise:
#
# ### Problem statement
#
# Find the price of the cheapest property for every city.
#
# Table structure: airbnb_search_details
#
# |    column              |   data type  |
# |------------------------|--------------|
# | id                     | int          |
# | price                  | float        |
# | property_type          | varchar      |
# | room_type              | varchar      |
# | amenities              | varchar      |
# | accommodates           | int          |
# | bathrooms              | int          |
# | bed_type               | varchar      |
# | cancellation_policy    | varchar      |
# | cleaning_fee           | bool         |
# | city                   | varchar      |
# | host_identity_verified | varchar      |
# | host_response_rate     | varchar      |
# | host_since             | datetime     |
# | neighbourhood          | varchar      |
# | number_of_reviews      | int          |
# | review_scores_rating   | float        |
# | zipcode                | int          |
# | bedrooms               | int          |
# | beds                   | int          |
#
# ### Solution A:
# ``` sql
# WITH price_order AS (
# SELECT city,
#        price,
#        ROW_NUMBER() OVER (PARTITION BY city ORDER BY price) AS price_rank
# FROM airbnb_search_details
# )
# SELECT city,
#        price AS minimum_price
# FROM price_order
# WHERE price_rank = 1;
# ```
#
# ### Solution B:
# ``` sql
# SELECT city,
#        min(price) AS minimum_price
# FROM airbnb_search_details
# GROUP BY city;
# ```
