class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 0
        count = 0 

        for nums in s:
            if nums-1 not in s:
                count =1 
                current = nums

                while current+1 in s:
                    count +=1
                    current = current+1 

                longest = max(longest,count)
        return longest 
        
        