# Creating our shopping list
grocery_list = ['apples', 'bananas', 'milk', 'bread']
print (grocery_list[0])  #0 = apples
print (grocery_list[-1]) # -1 = bread(The last one in the list)


#append() method -adds an item to the end of the list
grocery_list.append('eggs')
print(grocery_list)

#insert() method - adds an item at a specific index
grocery_list.insert(1, 'oranges')
print(grocery_list)

#remove() method - removes an item from the list
grocery_list.remove('milk')
print(grocery_list)

#pop() method - removes an item at a specific index
grocery_list.pop(2)
print(grocery_list)

#sort() method - sorts the list
name = "TANJIM"
name = name.lower()
print(name)

#searching and checking in a list
if 'apples' in grocery_list:
    print("Yes, paisi")

 #couting the number of items in a list
print(len(grocery_list))