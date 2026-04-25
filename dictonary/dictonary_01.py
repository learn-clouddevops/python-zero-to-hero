
# cook your dish here
#create empty dictonary

empty_dict ={}
print(empty_dict)

empty_dict2=dict()
print(type(empty_dict2))


#dont create key with the same name
student ={"name":"payal","age" :20, "grade" : 24, "name" : "gupta"}

print(student)

student ={"name":"payal","age" :20, "grade" : 'A'}
#accessing dictonay elements


print(student['grade'])


#DEFAULT GET MEHTOD TO ACCESS THE VALUE

print(student.get('grade'))
print(student.get('name'))
print(student.get('last_name')) #it will return null but if we want ot #get default value then do below

print(student.get('last_name', "Not Available"))

#modifying dictonary elements , dictonary are mutable so we can add update delete elements

student['age'] = 33
print(student)

student['country'] = 'India'

print(student)

del student['age']

print(student)
