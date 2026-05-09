with open('example.txt', 'w') as file:
    file.write('Hello, World!')


with open('example1.txt', 'r') as file:
    content = file.read()
print(content)  

#read line by line

with open('example1.txt', 'r') as file:
    for line in file:
        print(line. strip())

with open('example.txt', 'a') as file:
    file.write('Hello, World!\n')
    file.write('this is a new line.\n')

#binary file
data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)


with open('example.bin', 'rb') as file:
    content = file.read()
print(content)      




with open('example.txt', 'r') as source_file:
    content = source_file.read()
print(content)      

with open('example.txt', 'w') as dest_file:
    dest_file.write(content)
    
#read the text file and count the no of lines words and characheters
# 
with open('destination.txt', 'r') as file:
   content = file.read()
   lines = content.splitlines()
   print(f'Number of lines: {len(lines)}')
   words = content.split()
   print(f'Number of words: {len(words)}')
   characters = len(content)
   print(f'Number of characters: {characters}')
