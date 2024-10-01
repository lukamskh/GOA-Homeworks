# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    st = st.lower()
    for char in alphabet:
        if char not in st:
            return False
    return True