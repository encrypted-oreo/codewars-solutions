# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
