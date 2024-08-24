def amount_of_words(words):
    amount = words.split(" ")
    print(len(amount))
amount_of_words("hello my name is luke")

def every_A_in_a_sentence(sentence):
    new_amount = sentence.split("a" or "A")
    amount = len(new_amount) - 1
    print(amount)
every_A_in_a_sentence("welcome")

def split_name(name):
    letter = input("enter which letter do you want to count: ")
    sliced = name.split(letter)
    splited = len(sliced) - 1
    print(splited)
split_name("luke")

def more_than_1_string():
    str1 = input("type enithing: ")
    str2 = input("type enithing: ")
    str3 = input("type enithing: ")
    str4 = input("type enithing: ")
    str5 = input("type enithing: ")
    str6 = input("type enithing: ")
    str7 = input("type enithing: ")
    count = input("what do you want to count: ")
    string = str1
    def do_it():
     sliced = string.split(count)
     splited = len(sliced) - 1
     print(string)
     print(splited)
    do_it()
    string = str2
    do_it()
    string = str3
    do_it()
    string = str3
    do_it()
    string = str4
    do_it()
    string = str5
    do_it()
    string = str6
    do_it()
    string = str7
    do_it()
more_than_1_string()