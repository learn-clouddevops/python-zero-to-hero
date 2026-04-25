#dictonary class method
student ={"name":"payal","age" :20, "grade" : 'A'}
keys= student.keys()
print(keys)
values=student.values()
print(values)

items=student.items()

print(items) # it will give list of tuples

#shallow copy

student_copy=student
print(student)
print(student_copy)

student['name'] = "charu"

print(student)
print(student_copy)


student_copy1=student.copy() #shallow copy

student['name'] = "avi"

print(student)
print(student_copy1)

#iterating over dictonaries
#we can use loops to iterate
for keys in student.keys():
    print(keys)
    
for values in student.values():
    print(values)    
    
    
for key,value in student.items():
    print(key,value)
    
    
    
