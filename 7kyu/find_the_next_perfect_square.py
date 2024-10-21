# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

def find_next_square(sq):
    sqrt = sq ** 0.5
    
    if sqrt - int(sqrt) != 0:
        return -1
    
    return int(sqrt) * 2 + 1 + sq
