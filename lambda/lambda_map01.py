

''' lambda functions are small anaoymous fucntions defined using the lambda they can have n no of argemnts but only one expression'''


addition=lambda a,b: a+b

print(addition(2,3))


even= lambda num: num%2==0 

print(even(12))
    


addition1=lambda a,b : a+b

print(addition1(2,3))


## map()
numbers=[1,2,3,4,5,6]


def square(x):
    return x*x

# for i in numbers:
#     i = i*i
# print(numbers)  

#map takes function name and iterator
a=list(map(square , numbers))
print(a)

#lambda with map
numbers=[1,2,3,4,5,6]
b=list(map(lambda x:x*x,numbers))

print(b)



num1=[1,2,3]
num2=[1,2,3]

res=list(map(lambda x,y:x+y, num1,num2))
print(res)
