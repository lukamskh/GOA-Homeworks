# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

def to_weird_case(string):
    ans = ''
    i = True
    for char in string:
        if i == True:
            ans += char.upper()
            i = False
        elif i == False:
            ans += char.lower()
            i = True
        if char == " ":
            ans += ""
            i = True
    return ans