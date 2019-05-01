# Given a 32-bit signed integer, reverse digits of an integer.
class ReverseInteger(object):
    def reverse(slef, num):

        if num > 2 ** 31 - 1 or num <  0 - 2 ** 31 or num == 0:
            return 0
        positive = num > 0

        num = abs(num)

        num = int(str(num)[::-1])
        if num > 2 ** 31 - 1 or num < 0 - 2 ** 31 or num == 0:
            return 0

        if positive:
            num = num
        else:
            num = 0 - num


        return num







