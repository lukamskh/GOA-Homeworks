# https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python

def reverse(st):
    new_list = []
    st = st.split()
    for i in st:
        new_list.append(i)
    return " ".join(new_list[::-1])