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
# ## Python problem statement
# Say we have a list of existing_ids that we have already scraped. Let’s say we also have two lists, one of names and another of urls that correspond to names with the id of the names in the url.
#
# Write a function new_resumes to return the names and ids for ids that we haven’t scraped yet.
#
# Example:
# ``` python
#
# existing_ids = [15234, 20485, 34536, 95342, 94857]
#
# names = ['Calvin', 'Jason', 'Cindy', 'Kevin']
# urls = [
#     'domain.com/resume/15234', 
#     'domain.com/resume/23645', 
#     'domain.com/resume/64337', 
#     'domain.com/resume/34536',
# ]
#
# def new_resumes(existing_ids,names,urls) ->
# output = [('Jason', 23645), ('Cindy', 64337)]
# ```

# %%
def new_resumes(existing_ids,names,urls):
    ids = [int(id_to_scrape) 
           for *_, id_to_scrape in [url.split('/') 
                                    for url in urls]] 
    
    to_scrape = [(name, id_num) 
                 for name, id_num in list(zip(names, ids)) 
                 if id_num not in existing_ids]
    return to_scrape


# %%
new_resumes(existing_ids,names,urls)

# %% [markdown]
# ## SQL Problem statement & table organization
# Find whether hosts or guests give higher review scores based on their average review scores. Output the higher of the average review score rounded to the 2nd decimal spot (e.g., 5.11).
#
# Table name: airbnb_reviews
#
# | Column name  | Data type |
# |--------------|-----------|
# | from_user    | int       |
# | to_user      | int       |
# | from_type    | varchar   |
# | to_type      | varchar   |
# | review_score | int       |
#
#
#
# ### My answer:
# ``` sql
# SELECT from_type,
#        ROUND(AVG(review_score),2) AS winner
# FROM airbnb_reviews
# GROUP BY from_type
# ORDER BY winner DESC
# LIMIT 1;
# ```
