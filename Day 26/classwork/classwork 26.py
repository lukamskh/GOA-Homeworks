name = input("enter your name: ")
name1 = name.upper()
print(name1)
#lower გვეხმარება ყველა დიდად დაწერილი ასო დაიპრინტოს როგორც მისი პატარა ფორმა
name1 = name1.lower()
print(name1)

name2 = name1.capitalize()
print(name2)

#count ფუნქცია გვეხმარება დავთვალოთ რაიმე ასოს ან სიტყვის რაოდენობა წინადადებაში
name2 = input("enter sentance and I will count every Vowel: ")
amount = name2.count("a")
amount1 = name2.count("e")
amount2 = name2.count("i")
amount3 = name2.count("o")
amount4 = name2.count("u")
sum = amount + amount1 + amount2 + amount3 + amount4
print(sum)

name1 = input("re enter your name: ")
surname = input("enter your surname: ")
age = str(input("enter your age: "))
full = (name1 + " " + surname + " " + age)
location1 = int(input("enter 1 if you want to know location of your name 2 for surname and 3 for age: "))
print(location1)
if location1 == 1:
    location = full.index(name1)
    print(location)
elif location1 == 2:
    location = full.index(surname)
    print(location)
elif location1 == 3:
    location = full.index(age)
    print(location)
elif location1 > 3 or location1 < 1:
    print("I said 1-3 not more or less")


lists = []
amount_emails = int(input("enter number of how many emails do you want to enter: "))
for i in range(amount_emails):
    email = input("enter your email: ")
    if email.endswith("gmail.com") == True:
        lists.append(email)
    else:
        nothing = nothing