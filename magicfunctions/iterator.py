#iterator
my_ist = [1,2,3,4,5]
iterator = iter([1,2,3,4,5])


print(type(iterator))


iterator = iter(my_ist)

try:
    while True:
        print(next(iterator))
except StopIteration:
    print("End of the list reached.")
