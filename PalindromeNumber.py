# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:

        new_x = str(x)
        i = 0
        j = len(new_x) - 1
        while i < j:
            if new_x[i] == new_x[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
