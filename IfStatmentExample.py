num = input("Enter number : ")
num = int(num)
if num % 2 == 0:
    print("Enter number", num, " is Even")
else:
    print("Enter number", num, " is Odd")

print(3 > 2 and 4 > 1)
print(not True)

fruits = ["apple", "orange", "Pineapple", "Grapes", "Mango"]
vegetables = ["tomato", "onion", "carrot"]

item = input("Enter your item : ")
if item in fruits:
    print("Item is Fruit")
elif item in vegetables:
    print("Item in Vegetable")
else:
    print("Not available")