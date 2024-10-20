# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(value):
    res = 0
    for d in str(value):
        res += int(d) ** len(str(value))
    return res == value
