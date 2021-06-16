# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        answer = ""
        for char in s:
            if char.isalnum():
                answer += char
        return answer == answer[::-1]

result = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(result)


