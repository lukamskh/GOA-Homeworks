names = ["luka", "sofo", "avto", "saba", "manana"]
print(names.index("luka"))
print(names.index("sofo"))
print(names.index("avto"))
print(names.index("saba"))
print(names.index("manana"))

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(numbers[0])
print(numbers[9])

num = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", " 20"]
print(num)
num[0:11] = ["1", "11", "1", "13", "1", "15", "1", "17", "1", "19", "1"]
print(num)

name = input("enter your name: ")
surname = input("enter your surname: ")
age = input("enter your age: ")
email = input("enter your email: ")
list = ["your name:" + name + " your surname:" + surname + " your age:" + age]
list[6:9] = [" your email:" + email]
print(list)