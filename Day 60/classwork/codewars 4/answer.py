# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    width = n_floors * 2 - 1
    ans = [("*" * x).center(width) for x in range(1,width + 1,2)]
    return ans