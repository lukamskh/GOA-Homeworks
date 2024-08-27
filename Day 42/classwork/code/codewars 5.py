# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

def remove_duplicate_words(s):
    ans = []
    s = s.split()
    for i in s:
        if i not in ans:
            ans.append(i)
    return " ".join(ans)