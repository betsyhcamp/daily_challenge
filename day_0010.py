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
# Problem statement: 
# If you're faced with an input box, like this:
#
#                                            
#   Enter the price of the item, in dollars: |______________|
#                                            
# do you put the \\$ sign in, or not? Inevitably, some people will type a $ sign and others will leave it out. The instructions could be made clearer - but that won't help those annoying people who never read instructions anyway.
#
# A better solution is to write code that can handle the input whether it includes a \\$ sign or not.
#
# So, we need a simple function that converts a string representing a number (possibly with a $ sign in front of it) into the number itself.
#
# Remember to consider negative numbers (the - sign may come either before or after the \\$ sign, if there is one), and any extraneous space characters (leading, trailing, or around the \\$ sign) that the users might put in. You do not need to handle trailing characters other than spaces (e.g. "1.2 3"). If the given string does not represent a number, (either with or without a \\$ sign), return 0.0 .

# %%
def money_value(s):
    string =''
    for char in s:
        if char not in [' ', '$']:
            string += char
            
    try:
        return float(string)
    except:
        return float(0)
    


# %%
money_value( " $ -5.s7 ")

# %%
money_value( " $ -5.27 ")
