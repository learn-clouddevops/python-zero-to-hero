set1= {1,2,3,4,5,6,7}
set2= {4,5,6,7,8,9,0}
my_set = {1,2,3}
#add and remove elements
my_set.add(4)
print(my_set)
my_set.remove(3)
print(my_set)

#discard will not give error
my_set.discard(0)

removed_element=my_set.pop()
print(removed_element)

#clear all elements

my_set.clear()
print(my_set)

#set memebership def test_description(self):
my_set={1,2,3,4,5}
print (3 in my_set)# TODO: write code...
print(10 in my_set)


#union 

set2.union(set1)
print(set2)

#update whatever common elements set1 will be updated
set1.intersection_update(set2)

print(set1)
#intersection
#difference work like from set1 it will remove the common element but it will not update the set but intersection_update will update the set
print(set1.intersection(set2))


#intersection_update

print(set1.intersection_update(set2))

#symmetric difference from bioth set remove common elements and combine the bioth
print(set1.symmetric_difference(set2))


#sets methods

set1={1,2,3}
set2={3,4,5}

print(set1.issubset(set2)) #is set2 parent of set1 means set1 elements present in set2

print(set1.issuperset(set2)) #whether set2 has all lements of set1 means is set1 parent of set 2


#convert list to set1
my_list=[1,2,3,453,221,2,1]
my_list=set(my_list)

print(type(my_list))
print(my_list)

### counting unique words in try:
    
text ="hi this is devops this is learning course"

words = text.split()
unique_words = set(words)
print(words)

print(unique_words)
print(len(unique_words))

