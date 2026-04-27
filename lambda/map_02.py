##map 

#convert list of strings to integer

a= '1'
print(int(a))


str_number=['1','2','3','4','5']
int_number=list(map(int,str_number))

print(int_number)


#convert to upper case

words=['apple','banana','mango']
upper_word=list(map(str.upper,words))

print(upper_word)
people=[{"name":"payal","age":32},{"name":"avi","age":30}]

def get_name(persons):
    return persons['name']
    
res=list(map(get_name,people))   
print(res)
  




'''map () is a powerful tool for applying transformation to the iterable data structures.It can be used with regular functions,lambda functions, and even multiple iterable , providing a versatile approach to data processing in python. by understanding and utilizing map() you can write more efficient and readable code'''
