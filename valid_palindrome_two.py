'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''

class ValidPalindrome:

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(self, s, i + 1, j) or self.is_palindrome(self, s, i, j - 1)
            else:
                i += 1
                j -= 1
        return True


    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

