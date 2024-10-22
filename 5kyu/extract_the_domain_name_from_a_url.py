# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    url = url.removeprefix("https://")
    url = url.removeprefix("http://")
    
    domain_name = url.split("/")[0]
    domain_name = domain_name.removeprefix("www.")
    domain_name = domain_name.split(".")[0]
    
    return domain_name
