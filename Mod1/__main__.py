"""
Allison Valdez
Time complexity: O(n) where n is the total number of elements in the array
Space complexity: O(d) where d is the level of depth required of the array
"""


def product_sum(array, multiplier=1):
    summation = 0
    for x in array:
        if type(x) is list:
            summation += product_sum(x, multiplier + 1)
        else:
            summation += x
    return summation * multiplier


print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))