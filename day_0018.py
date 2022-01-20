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
# ### SQL problem statement 1:
#
# The events table tracks every time a user performs a certain action (like, post_enter, etc.) on a platform (android, web, etc.).
#
# Write a query to determine the top 5 actions performed during the month of November 2020, for actions performed on an Apple platform (iphone, ipad).
#
# The output should include the action performed and their rank in ascending order. If two actions performed equally, they should have the same rank. 
#
# **events** table structure:
#
# | column     | type     |
# |------------|----------|
# | user_id    |	int     |
# | created_at | datetime |
# | action	 | string   |
# | platform	 | string   |
#
# **output**: 
#
# | column |	type  |
# |--------|--------|
# | action | string |
# | ranks  |	int   |
#
# ### SQL answer 1:
# ``` sql
# WITH counts AS (
# SELECT action,
#        COUNT(*) as action_count
# FROM events
# WHERE EXTRACT(YEAR FROM created_at) = 2020
#       AND EXTRACT(MONTH FROM created_at) = 11
#       AND platform IN ('iphone', 'ipad')  
# GROUP BY action
# ORDER BY action_count DESC
# )
#
# SELECT action,
#        DENSE_RANK() OVER (ORDER BY action_count DESC) AS ranks
# FROM counts
# LIMIT 5;
# ```
#
# ### SQL problem statement 2:
# Find the base pay for Police Captains.
# Output the employee name along with the corresponding base pay.
#
# **sf_public_salaries** table structure:
#
# | column           | data type   |
# |------------------|-------------|
# | id               | int         |
# | employeename     | varchar     |
# | jobtitle         | varchar     |
# | basepay          | float       |
# | overtimepay      | float       |
# | otherpay         | float       |
# | benefits         | float       |
# | totalpay         | float       |
# | totalpaybenefits | float       |
# | year             | int         |
# | notes            | datetime    |
# | agency           | varchar     |
# | status           | varchar     |
#
#
#
# ### SQL answer 2:
# ``` sql
# SELECT employeename,
#        basepay
# FROM sf_public_salaries
# WHERE jobtitle ILIKE '%captain%'
#       AND jobtitle ILIKE '%police%';
# ```

# %% [markdown]
# ### Python problem statement: 
# Given two nonempty lists of user_ids and tips, write a function most_tips to find the user that tipped the most.
#
# Example:
#
# Input:
# ``` python
# user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102]
# tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]
# ```
#
# Output:
# ```python
# def most_tips(user_ids,tips) -> 105
# ```

# %%
user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102]
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]


# %%
def most_tips(user_ids,tips):
    # zip to create tuple (user_id, tip), then sort this list & unpack
    *_,(max_tip, max_tip_id) = sorted(list(zip(tips, user_ids)))

    return max_tip_id


# %%
most_tips(user_ids,tips)
