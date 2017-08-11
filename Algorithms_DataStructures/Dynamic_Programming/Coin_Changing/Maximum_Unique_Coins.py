"""
@author: David Lei
@since: 11/08/2017
@modified: 


Given a value and denomination of coins, what it the maximum number of unique ways to make up the value.
"""

value = 10
denominations = [1, 2, 5, 10]

""" Ways to make 10: 11
- 1 (x 10)
- 2 (x 1) + 1 (x 8)
- 2 (x 2) + 1 (x 6)
- 2 (x 3) + 1 (x 4)
- 2 (x 4) + 1 (x 2)
- 2 (x 5)
- 5 (x 1) + 1 (x 5)
- 5 (x 1) + 2 (x 1) + 1 (x 3)
- 5 (x 1) + 2 (x 2) + 1 (x 1)
- 5 (x 2)
- 10 (x 1)

1. For DP problems identify a pattern that uses sub solutions to build up a solution.

Above translated to a table
        0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    0   0   0   0   0   0   0   0   0   0   0   0
    1   0   1   1   1   1   1   1   1   1   1   1
    2   0   1   2   2   3   3   4   4   5   5   6
    5   0   1   2   2   3   4   5   6   7   8   10
    10  0   1   2   2   3   4   5   6   8   9   11

    max_unique_ways = (above + 1 if col==coin + index - coin if in range)

Working out for coins of denomination 1 & 2.

value 4:
- 1 (x 4)
- 2 (x 1) + 1 (x 2)
- 2 (x 2)

value 5:
- 1 (x 5)
- 2 (x 1) + 1 (x 3)
- 2 (x 2) + 1 (x 2)

value 6:
- 1 (x 7)
- 2 (x 1) + 1 (x 4)
- 2 (x 2) + 1 (x 2)
- 2 (x 3)

value 7:
- 1 (x 7)
- 2 (x 1) + 1 (x 5)
- 2 (x 2) + 1 (x 3)
- 2 (x 3) + 1 (x 1)

value 8:
- 1 (x 8)
- 2 (x 1) + 1 (x 6)
- 2 (x 2) + 1 (x 4)
- 2 (x 3) + 1 (x 2)
- 2 (x 4)

value 9:
- 1 (x 9)
- 2 (x 1) + 1 (x 7)
- 2 (x 2) + 1 (x 5)
- 2 (x 3) + 1 (x 3)
- 2 (x 4) + 1 (x 1)

value 10:
- 1 (x 10)
- 2 (x 1) + 1 (x 8)
- 2 (x 2) + 1 (x 6)
- 2 (x 3) + 1 (x 4)
- 2 (x 4) + 1 (x 2)
- 2 (x 5)

Working out for coins of denomination 1 & 2 & 5.

value 5:
- 1 (x 5)
- 2 (x 1) + 1 (x 3)
- 2 (x 2) + 1 (x 1)
- 5 (x 1)

value 6:
- 1 (x 6)
- 2 (x 1) + 1 (x 4)
- 2 (x 2) + 1 (x 2)
- 2 (x 3)
- 5 (x 1) + 1 (x 1)

value 7:
- 1 (x 7)
- 2 (x 1) + 1 (x 5)
- 2 (x 2) + 1 (x 3)
- 2 (x 3) + 1 (x 1)
- 5 (x 1) + 1 (x 2)
- 5 (x 1) + 2 (x 1)

value 8:
- 1 (x 8)
- 2 (x 1) + 1 (x 6)
- 2 (x 2) + 1 (x 4)
- 2 (x 3) + 1 (x 2)
- 2 (x 4)
- 5 (x 1) + 1 (x 3)
- 5 (x 1) + 2 (x 1) + 1 (x 1)

value 9:
- 1 (x 9)
- 2 (x 1) + 1 (x 7)
- 2 (x 2) + 1 (x 5)
- 2 (x 3) + 1 (x 3)
- 2 (x 4) + 1 (x 1)
- 5 (x 1) + 1 (x 4)
- 5 (x 1) + 2 (x 1) + 1 (x 2)
- 5 (x 1) + 2 (x 2)

value 10:
- 1 (x 10)
- 2 (x 1) + 1 (x 8)
- 2 (x 2) + 1 (x 6)
- 2 (x 3) + 1 (x 4)
- 2 (x 4) + 1 (x 2)
- 2 (x 5)
- 5 (x 1) + 1 (x 5)
- 5 (x 1) + 2 (x 1) + 1 (x 3)
- 5 (x 1) + 2 (x 2) + 1 (x 1)
- 5 (x 2)

"""