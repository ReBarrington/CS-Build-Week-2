# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occurances = dict()
        
        for num in nums:
            if num not in occurances:
                occurances[num] = 1
            else:
                occurances[num] += 1
        
        for value in occurances.values():
            if value >= 2:
                return True
        
        return False
        