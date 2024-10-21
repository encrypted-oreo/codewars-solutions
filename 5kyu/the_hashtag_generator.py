# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    res = "#"
    
    for w in s.split():
        if w == " ":
            continue
        res += w.capitalize()
        
    if len(res) > 140:
        return False
    
    return res if s else False
