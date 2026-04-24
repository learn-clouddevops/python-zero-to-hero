#creating tuple
lst= list()
empty_tuple=()
print(empty_tuple)
print(type(lst))
print(type(empty_tuple))


numbers=([1,2], [3,4],5,6, "hello", .33,1)
print(type(numbers[0]))
print(numbers[2])


#tuple operations
num1=(1,2,3,4,5,6)
print(list(num1))

mixed_tuple=(1,"hello world",3.14,True)
#concatenation

print(num1[1:3])

print(num1[::])

#tuple operations

print(numbers + mixed_tuple)


print(mixed_tuple *3)

#immutable nature of tuples

lst =[1,2,3,4,5]
print(lst)

lst[1]="payal"

print(lst)

#tuple methods

print(numbers.count(1))
print(numbers.index(6))


#packing and unpacking tuple
packed_tuple=1,"hi",[3,4]
print(packed_tuple)

a,b,*c=packed_tuple
print(a)
print(b)
print(c)




new_tuple=((1,2,3),(4,5,6),(7,8,9))

print(new_tuple[0][2])

#nested tuple
for i in new_tuple:
    for j in i:
        print(j, end=" ")
    print()    
