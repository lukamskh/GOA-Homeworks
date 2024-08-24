num = int(input("enter amount of seconds: "))
num2 = int(input("enter amount: "))
for i in range (num):
    i = i + 1
    print(i)
if num2 <= 10:
    print("your number is below number 10")
else:
    print("your number is above number 10")

amount = int(input("enter any amount: "))
number = []
for i in range (amount):
 num3 = int(input("enter number " + str(i + 1) + ": "))
           
 number.append(num3)
print(sum(number))

number = int(input("enter number: "))
num4 = int(input("enter second number: "))
number = str(number)
num4 = str(num4)

if number > num4:
 str(print(number + " is above" + " " + num4))
elif number < num4:
 str(print(number + "is below " + num4))

for num in range (10):
   print(num)

if num == number:
   print(str(num) + " is equal to " + str(number))
elif num != number:
   print(str(num) + " isnt equal to " + str(number))