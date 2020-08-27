# https://leetcode.com/problems/find-the-duplicate-number/submissions/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 0
            else:
                return num