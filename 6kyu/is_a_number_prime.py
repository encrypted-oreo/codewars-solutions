# https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(num):
    if num <= 1:
        return False
    
    if num & 1 == 0:
        return num == 2
    
    for n in range(3, int(num ** 0.5) + 1, 2):
        if n % 3 == 0:
          continue
        
        if num % n == 0:
            return False
    
    return True
