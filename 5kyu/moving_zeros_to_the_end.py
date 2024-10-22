# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    res = [el for el in lst if el != 0]
    return res + [0] * (len(lst) - len(res))
