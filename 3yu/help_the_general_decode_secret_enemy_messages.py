# https://www.codewars.com/kata/52cf02cd825aef67070008fa

_LETTERS101 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? *"

def _decrypt_one101(c, n):
    for i in range(n):
        ind = _LETTERS101.find(c)
        for j in range(len(_LETTERS101)):
            if _LETTERS101[((j+1) * 2 - 1) % len(_LETTERS101)] == c:
                c = _LETTERS101[j]
                break
    return c

def decode(s):
    return "".join(_decrypt_one101(c, i + 1) if c in _LETTERS101 else c for i, c in enumerate(s))
