"""
TODO- Heap, Two pointer, Binary search
Leetcode-https://leetcode.com/problems/find-k-closest-elements/
TC- SC-
FAQ-
How do I do binary search for closest to target element?


Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

from heapq import heappush as hpush
from heapq import heappop as hpop


class Obj:
    def __init__(self, val, diff):
        self.val = val
        self.diff = diff


class Solution:
    """
    Ideation-Heap solution TC- (NlogK (traverse and heapify) + KlogK (sorting)) = O(NlogK), SC- O(K)

    Maintain a max heap of length K and pop the elements from it when the length exceeds. In the end, you will have the
    minimum values in heap left.

    NOTE-The heap should be based on the difference value of abs(num-x).
    Sort the remaining heap and return.
    """

    def findClosestElements(self, arr, k, x):
        # defining comparator of the nums object
        def comp(a, b):
            # since we are using max heap, we want larger value to go and smaller value to remain, so adding it to heap.
            # Even in the scenario of equal difference.
            return b.diff <= a.diff

        # overriding comparator
        Obj.__lt__ = comp

        # max heap of length k
        hq = []
        for num in arr:
            diff = abs(num - x)
            numObj = Obj(num, diff)
            hpush(hq, numObj)
            if len(hq) > k:
                hpop(hq)

        result = [obj.val for obj in hq]
        result.sort()
        return result
