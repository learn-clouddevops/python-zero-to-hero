my_set = {1,2,3,4,5,5 , "hello" ,"world" ,"hello" , 100, 50, 75}

print(type(my_set))

print(my_set)


my_set.add(6)

print(my_set)


# Real world: Find common friends between two people
rahul_friends = {"Amit", "Priya", "Neha", "Raj", "Vikram"}
priya_friends = {"Amit", "Neha", "Deepa", "Kiran", "Raj"}

# Common friends
common = rahul_friends & priya_friends
print(common)
