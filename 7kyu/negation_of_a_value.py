# https://www.codewars.com/kata/58f6f87a55d759439b000073

def negation_value(s, val):
    for _ in range(len(s)):
        val = not val
    return val
