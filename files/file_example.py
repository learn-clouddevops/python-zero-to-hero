
import os


new_directory="package"
os.makedirs(new_directory,exist_ok=True)
print(f"{new_directory} directory created successfully.")
os.makedirs('new_folder',exist_ok=True)
print(f"new_folder directory created successfully.")
#listing all the files and directories in the current directory
items=os.listdir('.')
print(items)

#join paths 
dir_name="new_folder"
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)

with open(full_path,'w') as f:
    f.write("This is a sample file.")

print(full_path)


path=full_path
if os.path.exists(path):

    print(f"{path} exists.")
else:
    print(f"{path} does not exist.")



#check if path is file or directory

if os.path.isfile(path):
    print(f"{path} is a file.")
elif os.path.isdir(path):
    print(f"{path} is a directory.")
else:
    print(f"{path} is neither a file nor a directory.")


abs_path=os.path.abspath(full_path)
print(f"absolute path: {abs_path}")    

rel_path=os.path.relpath(full_path)
print(f"relative path: {rel_path}")
