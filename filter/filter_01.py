

#filer function


x= [1,2,3,4,5,6,7,8,9,10]

#find all even nos in the list


y=list(filter(lambda x:x%2==0, x))
print(y)



#nos greater than 3 and less than 9


y=list(filter(lambda x:x>3 and x<9, x))
print(y)



people=[{"name":"payal","age":32},{"name":"avi","age":30},{"name":"sunny","age":20}]

def find_age_greater_than_30(person):
    
        return person['age']>25
        
greater_age=list(filter(find_age_greater_than_30, people))
print(greater_age)

'''filter( funtions is a powerful tool used for creating iterators that filters items out of an iterable based on a functio.it is commnly used for data cleaning, filtering objects, and removing unwanted elements from the list . by mastering filter(), you can write more consise and efiicient code for processing and maipulating collection in python)'''

