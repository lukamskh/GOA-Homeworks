# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python

def distinct(seq):
    ans = []
    for i in seq:
        if i not in ans:
            ans.append(i)
    return ans