# https://www.codewars.com/kata/55ee3ebff71e82a30000006a

from functools import reduce

def title_to_number(chars):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return reduce(lambda r, x: r * 26 + x + 1, map(alphabet.index, chars), 0)
