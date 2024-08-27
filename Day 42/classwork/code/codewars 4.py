# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            return False
    return True