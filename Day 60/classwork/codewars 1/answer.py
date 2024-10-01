# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    min_number = min(a,b)
    max_number = max(a,b)
    sum = 0
    for num in range(min_number, max_number + 1):
        sum = sum + num
    return sum