import os
print(os.getcwd())
os.chdir('c:/Users/Gautam G/Python')
print(os.getcwd())
os.mkdir('-Os-demo-2')#creates a folder cannot create a file inside it if it doesnt exist
os.makedirs('Os-demo/Os-demo2')#creates a file inside a folder even if the folder is not there
os.rmdir('Os-demo2')#removes the file
os.removedirs('Os-demo/Os-demo2')#removes the folder
print(os.listdir())
