def xo(s):
    count_x = 0
    count_o = 0
    s = s.lower()
    for char in s:
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1
    return count_x == count_o