# https://www.codewars.com/kata/54da539698b8a2ad76000228

is_valid_walk = lambda walk: len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e")
