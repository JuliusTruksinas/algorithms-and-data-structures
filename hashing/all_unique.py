"""
Write a function, all_unique, that takes in a list.
The function should return a boolean indicating whether or not the list contains unique items.
"""

def all_unique(items: list[str]) -> bool:
  return len(set(items)) == len(items)


"""
Analysis:
Time Complexity:
Space Complexity:

"""