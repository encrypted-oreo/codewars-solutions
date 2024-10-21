# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    return ("%2X%2X%2X" % (min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))).replace(" ", "0")
