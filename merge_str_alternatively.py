class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                res.append(word1[p1])
                p1 += 1
            if p2 < len(word2):
                res.append(word2[p2])
                p2 += 1
        return "".join(res)