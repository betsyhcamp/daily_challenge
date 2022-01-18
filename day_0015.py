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
# ## SQL Excercise:
# Facebook has developed a new programing language called Hack.
# To measure the popularity of Hack they ran a survey with their employees. 
# The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored.
# Based on the above, find the average popularity of the Hack per office location.
# Output the location along with the average popularity.
#
# My solution: 
# ``` sql
# SELECT location,
#        COALESCE(AVG(popularity),0)
# FROM facebook_employees AS employee
# LEFT JOIN facebook_hack_survey AS survey
# ON employee.id = survey.employee_id
# GROUP BY location;
# ```

# %% [markdown]
# ## Python Excercise:
# Given a list of stop words, write a function stopwords_stripped that takes a string and returns a string stripped of the stop words.
# Example:
# ``` python
# stopwords = [
#     'I', 
#     'as', 
#     'to', 
#     'you', 
#     'your', 
#     'but', 
#     'be', 
#     'a',
# ]
#
# paragraph = 'I want to figure out how I can be a better data scientist'
# ```
#
# Expected output:
# ``` python
# def stopwords_stripped(paragraph,stopwords)
#      return(stripped_paragraph) ->
#
# stripped_paragraph = 'want figure out how can better data scientist'
# ```

# %%
def stopwords_stripped(paragraph, stopwords):
    stop_set = {word.lower() for word in set(stopwords)}
    split_paragraph = paragraph.lower().split(' ')
    cleaned_paragraph = [word 
                         for word in split_paragraph 
                         if word not in stop_set]
    return ' '.join(cleaned_paragraph)


# %%
stopwords_stripped(paragraph, stopwords)
