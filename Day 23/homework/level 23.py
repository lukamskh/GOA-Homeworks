def every_function(num1,num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num2 - num1)
    print(num1 * num2)
    print(num1 / num2)
    print(num2 / num1)
every_function(2,4)

def above_100 (num1, num2):
    while num1 < 100:
     num1 = num2 + num1
     print(num1)
above_100(9, 7) 

def positive_or_not(num1):
 if num1 %  2 !=0:
     print("negative")
 elif num1 % 2 == 0:
     print("positive")
positive_or_not(int(input("please enter number: ")))

def highest_number(list = [10, 6, 20]):
    print(max(list))
highest_number()

def sum_of_list(list = [20, 61, 18]):
   print(sum(list))
sum_of_list

def list_type_backwards(list = [4, "luka"]):
   type1 = print(type(list[0]))
   luka = print(type(list[1]))
   type1 = 4
   luka = "luka"
   print(luka, type1)
list_type_backwards()

def positive_or_not(num1):
 if num1 %  2 !=0:
     print("negative")
 elif num1 % 2 == 0:
     print("positive")
positive_or_not(int(input("please enter number: ")))

def longest_and_shortest():
   list = ["luka", "saba", "nata", "irakli", "gio"]
   print(max(list))
   print(min(list))
longest_and_shortest()

def positive(num1):
 if num1 %  2 !=0:
     print("negative")
 elif num1 % 2 == 0:
     print("positive")
positive(int(input("please enter number: ")))

def simple_num(num):
   if num / 2 == int() or num / 3 == int() or num / 5 == int():
      print("not simple")
   elif num / 1 == int() and num / num == int() or num == 3:
      print("simple")
simple_num(13)