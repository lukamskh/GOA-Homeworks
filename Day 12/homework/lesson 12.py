for i in range(20):
    print(i)

num2 = int(input("please enter any number: "))


if num2 % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")

num = 2
print("start")
for number in range (10):
   print(num)
   num1 = num + 1
   num = num1 + 1

num3 = sum(range(50, 101))
print(num3)
    
print("start")
num4 = 0
for number in range(11):
    print(num4)
    num4 = num4 + 5

num5 = int(input("please enter number: "))
num6 = int(input("enter any number: "))
if num5 > num6:
    for i in range(num6, num5):
        print(i)
elif num5 < num6:
    for i in range(num5, num6):
        print(i)

num7 = 1
for i in range(5, 11):
    num7 *=i
print(num7)