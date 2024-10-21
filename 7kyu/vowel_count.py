# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    return sum(sentence.count(c) for c in "aeiou")
