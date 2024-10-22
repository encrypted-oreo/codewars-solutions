# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e

def int32_to_ip(int32):
    octets = []
    for _ in range(4):
        octets.append(int32 & 0xFF)
        int32 >>= 8
    return "%d.%d.%d.%d" % tuple(octets[::-1])
