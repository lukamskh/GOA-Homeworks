numbers = []
for i in range(10):
    i = i + 1
    num = i
    print(i)
    numbers.append(num)
print(numbers)
print(len(numbers))

num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
list = []
for i in range(1):
    num3 = num1 + num2
    list.append(num3)
    num3 = num1 - num2
    list.append(num3)
    num3 = num1 * num2
    list.append(num3)
    num3 = num1 / num2
    list.append(num3)
print(list)

max = max(list)
min = min(list)
print(min + max)
print(sum(list))

num4 = int(input("enter any amount: "))
number = []
for i in range (num4):
 num3 = int(input("enter number " + str(i + 1) + ": "))
           
 number.append(num3)
print(sum(number))

fav_cars = ["ford F40", "mclaren 750s", "nissan miata", "mazda rx7", "koneggs agara"]
print(fav_cars[1:3])
print(fav_cars[-0:-2])
print(fav_cars[-3])
print(fav_cars[-4])

username = input("enter your name: ")
if username == "luka":
   print("hello admin")
else:
   print("hello" + username)