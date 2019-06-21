fruits = ["apple", "orange", "Pineapple", "Grapes", "Mango"]
vegetables = ["tomato", "onion", "carrot"]

items = fruits + vegetables

for item in items:
    if item in fruits:
        print("Fruit : ", item)
    elif item in vegetables:
        print("Vegetable : ", item)

for i in range(1, 11):
    # for i in range(11)
    print(i)

isAvailable = "Mango"

for item in items:
    if item in fruits:
        print("Fruit : ", item)
        if fruits == "Mango":
            break

for x in range(6):
    if x % 2 == 0:
        continue
    print(x*x)

