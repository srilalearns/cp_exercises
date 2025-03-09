class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        most = max(candies)
        res = []
        for x in candies:
            res.append(x+extraCandies >= most)
        return res