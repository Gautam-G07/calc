import os
print(dir(os))#gives the list of functions in the os module
print(os.getcwd())
os.chdir('c:/Users/Gautam G/Python')
print(os.getcwd())
os.mkdir('-Os-demo-2')#creates a folder cannot create a file inside it if it doesnt exist
os.makedirs('Os-demo/Os-demo2')#creates a file inside a folder even if the folder is not there
os.rmdir('Os-demo/Os-demo2')#removes the file
os.rename('test.py','day1.py')#renames the file
os.removedirs('Os-demo/Os-demo2')#removes the folder
print(os.stat('Os-demo').st_mtime)#gives the details of the file
for dirpath, dirnames, filenames in os.walk('c:/Users/Gautam G/Python'):#walks through the directory and gives the path, directories and files in it    
    print('Current Path:',dirpath)
    print('Directories:',dirnames)
    print('Files:',filenames)
    print()
print(os.listdir())
