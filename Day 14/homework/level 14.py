num = int(input("type number from 1 to 100: "))
while num != 64:
   num = int(input("wrong enter number again: "))
   if num == 64:
      print("correct you won")

i = int(input("type number: "))
if i < 100:
  print("wrong you had 1 try")
elif i > 100:
   print("good guess")

num1 = 0
number = 0
for number in range (100):
   number = number + 1
   number = number * number
   print(number)
   
for number in range (5, 10):
   print(number)
   number = num1 + 1
   num1 = number + 1

print("hey")
print("you")
print("yes you do you want to play")
answer = str(input("yes or no:"))
if answer == "yes":
   print("good...")
elif answer == "no":
   print("no?... you will stil play")

print("game 1")
num = int(input("guess the number from 1 to 100: "))
print("come on dont be shy")
if num != 72:
   print("wrong try again")
elif num == 72:
   print("1.you are lucky 2.you looked at code")



