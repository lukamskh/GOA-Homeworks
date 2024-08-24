
def even_and_odd_sum(numbers):
    lists_ = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            lists_.append(num)
        else: odd.append(num)
    print(lists_)
    print(sum(lists_))
    print(odd)
    print(sum(odd))
even_and_odd_sum([3,5,2,8,3,1,4,2,9,6])

