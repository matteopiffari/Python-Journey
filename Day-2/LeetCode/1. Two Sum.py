# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Easy but inefficient way

        """for i, element in enumerate(nums):
            for y, secondElement in enumerate(nums):
                if (element+secondElement) == target and i != y:
                    return [i,y]"""
        

        # Efficient way with hashmap

        hashMap = {}

        for i, element in enumerate(nums):
            hashMap[element] = i

        for i, element in enumerate(nums):
            if (target-element) in hashMap and i != hashMap[target - element]:
                return [i, hashMap[target - element]]