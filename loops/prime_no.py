#prime nos.

for num in range (1,20):
    if num > 1:
        for i in range (2,num):
            if (num%i == 0):
                break
        else:
            print(f"{num} is a prime no.")
            
