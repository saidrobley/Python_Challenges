# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
# Example:
#
# Input: "Hello World"
# Output: 5
class LengthOfLastWord:
    def length_last_word(self, s):
        s = s.strip()
        count = 0

        for c in s:
            if c == ' ':
                count = 0
            else:
                count += 1
        return count

x = LengthOfLastWord()
print(x.length_last_word("Hello World"))