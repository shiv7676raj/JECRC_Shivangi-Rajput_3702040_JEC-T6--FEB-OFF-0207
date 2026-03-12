'''File-Type of container in which we contain or store some data
->To identify the data inside a file, we use extensions(ex-.py,.mp4,.html,.jpg,etc.)
->Permissions-
    open()-open('filename.ext'/'absolute_path',mode)
    close()-var_name.close()
->Modes-
    1.write(w)
        1.1.only write(w)
        1.2.write+read(w+)
        1.3.write binary(wb)
        1.4.write and read binary(wb+)
    2.read(r)
        1.1.only read(r)
        1.2.read+write(r+)
        1.3.read binary(rb)
        1.4.read and write binary(rb+)
    3.append(a)
        1.1.only append(a)
        1.2.append+read(a+)
        1.3.append binary(ab)
        1.4.append and read binary(ab+)

for write operation:
1.write(str_data)-single line of data
2.writelines([line1,line2,...,linen])-multiple line of data
'''

'''file=open('temp.txt','w')
#file.write('This is a file handling demo!')
file.writelines(['This is the second line!',
                 '\nThis is the third line!',
                 '\nThis is the fourth line!'])
file.seek(0)    #to make python interpreter to point at a specific index, we use seek(index).
print(file.read())
file.close()'''

#1.read()-Display the file content as it is. 
#2.readline()-It reads a single line of data from the file at a time.
#3.readlines()-It reads the whole data of file and returns it in list format.
'''file=open('temp.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())    
file.close()'''

# file=open('notes.txt','r')
# print(file.read()) 
# file.close()

file=open('notes.txt','a+')
file.write('\nFile handling is very important!')
file.write('\nIt is used to store data permanently!')
file.seek(0)    
print(file.read())
file.close()