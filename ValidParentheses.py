# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
class ValidParentheses(object):
    def is_valid(self, s: str) -> bool:
        par_dict = {"(": ")", "[": "]", "{": "}"}
        cur_stack = []
        for a in s:
            if a in par_dict:
                cur_stack.append(a)
            elif cur_stack == [] or par_dict[cur_stack.pop()] != a:
                return False
        return cur_stack == []



