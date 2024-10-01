# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
 
def clean_string(s):
    ans = []
    for c in s:
        if c == '#' and ans: 
            ans.pop()
        elif c!='#':
            ans.append(c)
    return ''.join(ans)