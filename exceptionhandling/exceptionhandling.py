

try:
    x = y
except NameError as e:
    print(e)


try:
    result=1/0
    a = b
except ZeroDivisionError as e:
    print(e)
except Exception as ex1:
    print(ex1)



try:
    num =int(input("Enter a number: "))
    res = 10/num
    print(res)
except ZeroDivisionError as e:
    print("You cannot divide by zero.")
except Exception as e:
    print(e)


#try except else
    try:
        num =int(input("Enter a number: "))
        res = 10/num
        print(res)
    except ZeroDivisionError as e:
        print("You cannot divide by zero.")
    except Exception as e:
        print(e)
    else:
        print("No exceptions occurred.")


#try except, else,finally    
try:
    num =int(input("Enter a number: "))
    res = 10/num
    print(res)
except ZeroDivisionError as e:
    print("You cannot divide by zero.")
except Exception as e:
    print(e)
else:
    print("No exceptions occurred.")
finally:
    print("This block will always execute.")


    #file exception handling
    try:
        with open("example1.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        print("The file was not found.")
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
            print("File closed.")
        else:
            print("File already closed.")    
