class Solution(object):
    def gcdOfStrings(self, str1, str2):
        '''
        algorithm:
        first check if gcd exists by seeing if str1+str2 = str2 + str1
        if the strings pass this test then gcd exists you just need to cut down the longest string
        by removing the smaller string part from it

        '''
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str2[len(str1):], str1)