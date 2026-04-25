students={
    "student1":{
        "name":"payal",
        "age": 32
    },
     "student2":{
        "name":"avi",
        "age": 30
    }
}

#access nested dictonaries

print(students['student2']['name'])

for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")
        
#dictonary comprehension

squares = {x:x**2 for x in range(5)}
print(squares)

square = dict()
for i in range(5):
    square[i] = i**2
print(square)    
    
even={x:x**2 for x in range(10) if x%2 ==0}
print(even)

#use a dictonary to count the frrquency of elements in a list

numbers= {1,2,3,3,4,4,4,4,5,5,5,5,5}

frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)    
        
#merge 2 dictonaries
dict_1={"a":1,"b":2}
dict_2={"c":3,"d":4}

merged_dict={**dict_1,**dict_2}
print(merged_dict)
