import os
from datetime import datetime
print(os.getcwd())
os.chdir('c:/Users/Gautam G/Python')
print(os.getcwd())

print(os.stat('Os-demo').st_mtime)#gives the details of the file
mod_time=os.stat('Os-demo').st_mtime
print(datetime.fromtimestamp(mod_time))#gives the date and time of the file in human readable

print(os.environ.get('HOMEPATH'))#gives the home directory of the user
filepath=os.path.join(os.environ.get('HOMEPATH'),'test.txt')#joins the home directory with the file name
print(filepath)
with open(filepath,'w') as f:
    f.write('This is a test file')
print(os.path.exists(filepath))#checks if the file exists
print(os.path.isdir("/tmp/testfile"))#checks if the path is a directory
print(os.path.dirname("/tmp/testfile"))
print(os.path.isfile("/tmp/testfile"))
print(dir(os.path))#gives the list of functions in the os.path module