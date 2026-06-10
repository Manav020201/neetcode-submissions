class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcoutn = 0
        for number in nums:
            if number == 1:
                count+=1
                maxcoutn = max(count, maxcoutn)
            else:
                count = 0
        return maxcoutn
        