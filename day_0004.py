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
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#
#
#
# Example:
#
# Input: nums = [1,1,2]
#
# Output: 2, nums = [1,2]
#
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

# %%
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dup_val =[]
    for i, item in enumerate(nums):
        if (i+1)==len(nums):
            continue
        else:
            if item == nums[i+1]:
                dup_val.append(item)
    for item in dup_val:
        nums.remove(item)
    return len(nums)


# %%
nums = [1,1,1,2]
removeDuplicates(nums)
print(nums)


# %%
def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dup_value = [item 
                 for i, item in enumerate(nums) 
                 if ((i+1)!=len(nums) and item == nums[i+1])]
    for item in dup_value:
        nums.remove(item)
    return len(nums)


# %%
nums = [1,1,1,2]
removeDuplicates2(nums)
print(nums)

# %%
# apparently you can traverse input array backwards & that approach will work since the index will not change
# try looping backwards using while (when refactoring)
