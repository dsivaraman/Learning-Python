fruits = ["apple", "orange", "Pineapple", "Grapes", "Mango"]

print(fruits)
print(fruits[1])
fruits[1] = "Watermelon"
print(fruits)
print(fruits[0:2])
print(fruits[-1])
print(fruits[-1:])

fruits.append("orange")
print(fruits)
fruits.insert(1, "Kiwi")
print(fruits)

vegetables = ["tomato", "onion", "carrot"]

items = fruits + vegetables

print(items)
items1 = [fruits, vegetables]
print(items1[1][0])

# vegetables + "Curry leaves" Can't add string to list.

print(len(items))
print("apple" in fruits)
print("onion" in vegetables)