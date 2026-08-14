## What is Big-O Notation?

- A way to describe the performance of an algorithm.
- Emphasis on how performance scales with input size.
- It's an approximation; no units

## Why Use Big-O Notation?

- gives you the ability to compare different algorithms
  without relying on the environment that algorithm is ran at.

## Big-O Simplification Rules:

1. Drop any constant factors:
   - O(4n) = O(n)
   - O(999n) = O(n)
   - (n/2) = O(n) [dividing by 2 is the same as multiplying by 0.5, so also a constant]
2. Drop smaller terms in a sum:
   - O(n^2 + n) = O(n^2)
   - O(n + n^4 + n^2) = O(n^4)
   - O(n^4 - n^3) = O(n^4) [subtracting a number is the same as adding a negative number so the rule still applies.]

### Examples:

**O(4n^2 + n + 5)**

1. Drop any constant factors; O(4n^2 + n + 5) = O(n^2 + n + 5) [Removed the constant factor **4**]
2. Drop smaller terms in a sum; O(n^2 + n + 5) = O(n^2)

**O(0.5 s\* n^2 + 900)**

1. Drop any constant factors; O(0.5 \* n^2 + 900) = O(n^2 + 900)
2. Drop smaller terms in a sum; O(n^2 + 900) = O(n^2)

## Common Big-O Complexities

From best to worse:

1. O(1) - "constant"; meaning **performance does not depend on the input size**; notice it does not include any variable **n**.
2. O(log(n)) - "logarithmic"
3. O(n) - "linear"
4. O(n^c) - "polynomial"; examples: O(n^2), O(n^3), ...
5. O(c^n) - "exponential"; examples: O(2^n), O(3^n), ...
6. O(n!) - "factorial"

Knowing these common complexities is important for simplifying a Big-O notation
