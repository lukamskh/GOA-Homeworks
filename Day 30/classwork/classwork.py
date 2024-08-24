def filter_odd(num):
    odd = []
    even = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else: odd.append(i)
    print(odd)
    print(sum(odd))
    print(even)
    print(sum(even))
filter_odd([4,3,6,7,3,6,6,7,2,5,7,1])