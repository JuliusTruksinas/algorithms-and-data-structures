"""
Write a function, pair_sum, that takes in a list and a target sum as arguments.
The function should return a tuple containing a pair of indices whose elements sum to the given target.
The indices returned must be unique. Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
"""

def pair_sum(numbers: list[int], target_sum: int) -> tuple[int, int]:
  previous = {}

  for i, num in enumerate(numbers):
    compliment = target_sum - num
    if compliment in previous:
      return (i, previous[compliment])

    previous[num] = i

"""
Analysis:
Time Complexity: O(n)
Space Complexity: O(n)
"""