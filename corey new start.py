import os

print(os.getcwd())

os.chdir('C:\\Users\\efkan\\Desktop')
print(os.getcwd())
print(os.listdir())
os.mkdir('the new file i created')
os.makedirs('can create sub folders with this/look at this')
print(os.listdir())
#also can delete folders with this
os.rmdir('the new file i created')
os.removedirs('can create sub folders with this/look at this')
os.rename('original file name', 'new name')
os.stat('gives information about folder')

import os
for dirpath, dirnames, filenames in os.walk('C:\\Users\\efkan\\Desktop'):
    print(f"Current Path:  {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
#this lets you see every file and folder in the directory you want

+ os.getcwd()                                            => get current working directory
+ os.chdir(<path>)                                    => change directory
+ os.listdir()	                                            => list directory
+ os.mkdir(<dirname>)                           => create a directory
+ os.makedirs(<dirname>)                    => make directories recursively
+ os.rmdir(<dirname>)	                   => remove directory
+ os.removedirs(<dirname>)                => remove directory recursively
+ os.rename(<from>, <to>)                   => rename file
+ os.stat(<filename>)                            => print all info of a file
+ os.walk(<path>)	                          => traverse directory recursively
+ os.environ		                                 => get environment variables
+ os.path.join(<path>, <file>)              => join path without worrying about /
+ os.path.basename(<filename>)     => get basename
+ os.path.dirname(<filename>)         => get dirname
+ os.path.exists(<path-to-file>)         => check if the path exists or not
+ os.path.splitext(<path-to-file>)      => split path and file extension
+ dir(os)			                               => check what methods exists

f = open('test_file.txt', 'r')
print(f.name)
print(f.mode)
f.close()

#or you can
with open('test_file.txt', 'r') as f:
    #f_contents = f.read() gives everything in file, you can say read(100) it will show the first 100 characters.
    #f_contents = f.readlines() gives content as a list
    #f_contents = f.readline() gives one by one
    for line in f:
        print(line, end='') #or you can just do this to get lines from doc
    print(f_contents, end='') #to prevent script to add extra new empty line

with open('test_file.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
        #f.seek(0) if you want to start over the file again
with open('it will create itself', 'w') as f:
    f.write('created') #it will overwrite a file, instead of adding. it will create the file if it does not exist
    f.seek(0)
    f.write('created') #second one will be overwritten on the first one
with open('new_test_file.txt', 'r') as rf: #to write from one file to another
    with open('new_test_file.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
with open('picture_file.jpg', 'rb') as rf: #pictures should be opened in binary mode
    with open('picture_file_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
with open('picture_file.jpg', 'rb') as rf: #pictures should be opened in binary mode
    with open('picture_file_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write()   #another way of copying just like we did before
