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
# # Python exercise:
# ### Problem statement
#
# Given a 2-D matrix P of predicted values and actual values, write a function precision_recall to calculate precision and recall metrics.
#
# Return the ordered pair (precision, recall).
#
# **Example:**
#
# **Input:**
# ``` python
# P = [[121, 9],
#     [17, 144]]
# ```
# where `P` represents the following table
#
# |             | Predicted =TRUE |	Predicted =FALSE|
# |-------------|-----------------|-------------------|
# |Actual =TRUE |	121             |	9               |
# |Actual =FALSE|	17              |	144             |
#
# **Output:**
#
# ``` python
# def precision_recall(P) -> (0.931, 0.877,)
# ```

# %%
def precision_recall(P):
    [[TP, FN],[FP, TN]] = P
    precision = TP / (TP + FP)
    recall = TP / (FN + TP)
    return (round(precision,3), round(recall,3))


# %%
P = [[121, 9],
    [17, 144]]
precision_recall(P)

# %% [markdown]
# # SQL Exercise
# ### Problem statement:
# To improve sales, the marketing department runs various types of promotions. The marketing manager would like to analyze the effectiveness of these promotional campaigns. In particular, what percentage of sales had a valid promotion applied? Only the promotions found in the facebook_promotions table are valid.
#
#
# Table structure for `facebook_promotions`:
#
# |column       | data type |
# |-------------|-----------|
# |promotion_id | int       |
#
# Table struture for `facebook_sales`:
#
# |column         | data type |
# |---------------|-----------|
# |product_id     | int       |
# |promotion_id   | int       |
# |cost_in_dollars| int       |
# |customer_id    | int       |
#
# ### Solution A:
#
# ``` sql
#
# WITH promo_sales AS (
# SELECT sales.*
# FROM facebook_sales AS sales
# INNER JOIN facebook_promotions AS promotions
# USING(promotion_id))
# ```
#
# ### Solution B:
#
# ``` sql
# SELECT (SELECT COUNT(*) FROM promo_sales)::float/ COUNT(*) *100.0 AS percent_promo_sales
# FROM facebook_sales;
#
# SELECT COUNT(promo.promotion_id)/(COUNT(*)::float) *100 AS percent_promo
# FROM facebook_sales
# LEFT JOIN facebook_promotions AS promo
# USING(promotion_id)
# ```
