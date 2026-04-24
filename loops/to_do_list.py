to_do_list = ["buy grocery" , "clean" , "sleep" , ]
print(to_do_list)
to_do_list.append("walk" )

print(to_do_list)

to_do_list.remove("buy grocery")
print(to_do_list)

if "clean" in to_do_list:
    print("do not forgot to clean the house")

print("remaining to do list")

for task in to_do_list:
  print(f"-{task}")
    
