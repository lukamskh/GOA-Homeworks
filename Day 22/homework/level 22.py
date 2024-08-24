def addup(num1):
    print(num1 + 5)
addup(1)

def combine(num1,num2):
    print(num1 * num2)
combine(2,5)

def string(name):
    print(len(name))
string("luka")

def lists(name1, name2):
    print(len(name1 + name2))
lists("luka", "nata")

name = str(input("enter anithing: "))
name1 = str(input("enter anithing: "))
name2 = str(input("enter anithing: "))
list = [name, name1, name2]
if len(name) > len(name1) and len(name) > len(name2):
    print(name)
elif len(name) < len(name1) and len(name1) > len(name2):
    print(name1)
elif len(name1) < len(name2) and len(name2) > len(name):
    print(name2)

def not_negative (number):
    if number >= 0:
        print("your number is factorial")
    elif number < 0:
        print("your number is not factorial")
not_negative(int(input("enter number: ")))


num = int(input("enter number: "))
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
num3 = int(input("enter number: "))
list1 = [num, num1]
list2 = [num2, num3]
if num > num1:
    biggest_list1 = num
else:
    biggest_list1 = num1
if num2 > num3:
    biggest_list2 = num2
else:
    biggest_list2 = num3
print(biggest_list1 + biggest_list2)

if num < num1:
    smallest_list1 = num
else:
    smallest_list1 = num1
if num2 < num3:
    smallest_list2 = num2
else:
    smallest_list2 = num3
print(smallest_list1 - smallest_list2)

print(biggest_list1 - smallest_list1)
print(biggest_list2 - smallest_list2)

print(sum(list1))
print(sum(list2))

def squere(num4):
    print(num4 * num4)
squere(5)

num5 = int(input("enter number: "))
if num5 %  2 !=0:
    print("false")
elif num5 % 2 == 0:
    print("true")

num4 = int(input("enter number last time: "))
calculate = [num, num1, num2, num3, num4, num5]
amount = len(calculate)
combineed = sum(calculate)
print(combineed / amount)