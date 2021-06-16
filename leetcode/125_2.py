# https://leetcode.com/problems/valid-palindrome/
import collections
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


result = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(result)


