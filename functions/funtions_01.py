


def even_or_odd(num):
    """this function prforms a finds even or odd"""
    if num%2 ==0:
        print("the no. is even")
    else:
        print("the no. is odd")


##call this function
even_or_odd(28)



def add(a,b):
    "add two variables"
    return(a+b)
    
result =add(2,4)        


def greet(name="guest"): # it will assign default value if its not passed

    print(f"hello {name}")
    
    
greet("payal")




# positional and keywords arguments

def positional_arguments(*args):
    for i in args:
        print(i)


positional_arguments(1,2,3,45,6,"hello")



#keyword arguments all parameters will in in form of key value pair


def keyword_arg(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        

keyword_arg(name="payal",age="30")    

#return multiple va;ues
    

def multiply(a,b):
    "add two variables"
    return a*b,a
    
result =multiply(2,4)  
print(result)
        
