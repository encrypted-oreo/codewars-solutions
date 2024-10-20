# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    seen = []
    dupes = []
    res = 0
    
    for char in text.lower():
        if char not in seen:
            seen.append(char)
        elif char not in dupes:
            res += 1
            dupes.append(char)
    
    return res
