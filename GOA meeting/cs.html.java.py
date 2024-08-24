#10
def squre(num):
    print(num * num)
squre(int(input("please enter number: ")))
    
#7
def palindrome(word):
    if word == word[::-1]:
        print("your word is palidrome")
    elif word != word[::-1]: print("your word isnt palindrome")
palindrome(input("enter anithing: "))


#5
def amount(word):
    num = 0
    for i in range(len(list(word))):
        if list(word[i]) == "a" or "e" or "i" or "u":
            num = num + 1
        else: num = num
    i = i + 1
amount("luka")

#11
def uppercase(word):
   word1 = word.upper()
   print(word1)
uppercase(input("enter word: "))

#12
def from_kmh_to_mph(speed):
    speed = speed * 0.621371
    print(speed)
from_kmh_to_mph(int(input("enter speed: ")))

#16
def manual_min(num1,num2,num3,num4,num5):
    if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5:
        print(num1)
    elif num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5:
        print(num2)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5:
        print(num3)
    elif num4 <= num2 and num4 <= num3 and num4 <= num1 and num4 <= num5:
        print(num4)
    elif num5 <= num2 and num5 <= num3 and num5 <= num4 and num5 <= num1:
        print(num5)
print(manual_min(5, 3, 1, 20, 11))

def manual_max(list):
    num = int(input("enter number: "))
    max_number = list[num]
    for num in (list):
        if num > max_number:
            max_number = num

    print(max_number)

def squere_2():
 num1 = int(input("enter number: "))
 num2 = int(input("enter number: "))
 num3 = int(input("enter number: "))
 num4 = int(input("enter number: "))
 num = [num1 ,num2 ,num3, num4]
 num2 = []
 for i in range (len(num)):
     num1 = num[i] * num[i]
     num2.append(num1)
     i = i + 1
 print(num2)
