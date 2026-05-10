

def square(n):
    for i in range(3):
        yield i**2
    

print(square(5))


for i in square(5):
    print(i)



def my_generator():
    yield "Hello"
    yield "World"
    yield "Welcome to Python Generators"


gen=my_generator()
next(gen)    


for val in gen:
    print(val)

##reading large files
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


file_path = 'large_file.txt'
for line in read_large_file(file_path):
    print(line)            
