# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    ans = []
    for i in range(len(lines)):
        ans.append(f"{i + 1}: {lines[i]}")
    return ans