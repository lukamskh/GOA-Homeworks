for i in range(5):
    print(i)

print("next")
num = 0
while num != 5:
    num = num + 1
    print(num)

lists = []
for i in range(2):
    print(list("Hello"))

i = 0
while i == 1:
    i = i + 1
    print(list("Hello"))

for i in range(1,4):
    print(i)

while num == 3:
    print(num)
    num = num + 1

for i in range(3):
    print("python is fun")

num = 0
while num == 3:
    print("python is fun")
    num = num + 1

lists = []
for num in range(3):
    num = num + 1
    lists.append(num)
print(lists)

lists = []
while num == 3:
    lists.append(num)
    num = num + 1
print(lists)

lists = [1, 2, 3, -4, 5]
for i in range(len(lists)):
    print("hi")

list_amount = len(lists)
while len(lists) == len(lists) + len(lists):
    print("hi")
    num = num + 1
    lists.append(num)

num = num
for i in range(len(lists)):
    if lists[i] > 0:
        print(lists[i])
    elif lists[i] < 0:
        print(num)
    i = i + 1

numbers = []
for i in range(3):
    numbers.append(i)
    num = numbers[::-1]
print(num)

while i == 3:
    numbers.append(i)
    i = i + 1
num = numbers[::-1]
print(num)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters = []
for i in range(4):
    letters.append(alphabet[i])
print(letters)

while i == 4:
    letters.append(alphabet[i])
    i = i + 1
print(letters)

for i in range(4):
    print("looping")

while i != 4:
    i = i + 1
    print("looping")

for i in range(4):
    numbers.append(i)
    numbers = numbers[1:5]
print(numbers)

while i != 4:
    i = i + 1
    numbers.append(i)
    numbers = numbers[0:3]
print(numbers)

numbers = []
for i in range(6):
    numbers.append(i)
    num = numbers[::-1]
    num = num[0:5]
print(num)

while i != 5:
    i = i + 1
    numbers.append(i)
    num = numbers[::-1]
    num = num[0:5]
print(num)

for i in range(1):
    fruit = ["apple", "banana", "cherry"]
    print(fruit)

while i != 2:
    i = i + 2
    fruit = ["apple", "banana", "cherry"]
    print(fruit)

numbers = []
for i in range(4):
    numbers.append(i)
    num = numbers[1:4]
print(num)

i = 0
while i != 4:
    i = i + 1
    numbers.append(i)
    num = numbers[1:4]
print(num)

numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    print("loop")

print("next")
i = 0
while i < len(numbers):
    print("loop")
    i = i + 1

word = ("abc")
for i in range(1):
    print(list(word))

while i < 1:
    print(list(word))
    i = i + 1

word = ["x", "y", "z"] 
for i in range(1):
    print(word[0:2])

while i < 1:
    print(word[0:2])
    i = i + 1

for i in range(2):
    print("hello world")

i = 0
while i < 2:
    i = i + 1
    print("hello world")

numbers = [1, 2, 3]
for i in range(1):
    print(numbers)

while i < 1:
    i = i + 1
    print(numbers)

numbers = []
num = 0
for i in range(3):
    num = num + 10
    numbers.append(num)
print(numbers)

while num <= 20:
    num = num + 10
    numbers.append(num)
print(numbers)

for i in range(1):
    print("done")

while i < 1:
    i = i + 1
    print("done")

some_numbers = [[1, 2], [3, 4]]
for i in range(1):
    print(some_numbers)

while i > 1:
    i = i + 1
    print(some_numbers)

for i in range(6):
    print(i)

while i < 5:
    print(i)
    i = i + 1

for i in range(1):
    print(list("loop"))

while i < 1:
    print(list("loop"))
    i = i + 1