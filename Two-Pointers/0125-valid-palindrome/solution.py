class Solution(object):
    def isPalindrome(self, s):
        clean = ""
        for char in s:
            if char.isalnum():
                clean+=char.lower()
        return clean==clean[::-1]
        