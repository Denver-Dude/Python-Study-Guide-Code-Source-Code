#FILE MANAGEMENT

s = "The Quick Brown Fox Jumped Over A Lazy Dog\n"
#his string u want to write in a file
#there is multiple ways to handle files
#first method
df=open("trash.txt","w")
#text mode will take care of text files
#binary mode will allow you to use any other file extenstion
#if opened in write mode, then the file will be created
#if files already exist, then the already exiting files will be gone


#adding text
for _ in range(10):
    df.write(s)
    #the text is added 10 times

#this is important as servers can relax and not to keep it open all time
df.close

############# So far the file has been destroying what was there eariler

df = open("trash.txt","rt")
#r - read
# t - text
st1 = df.read()
df.close()
print(st1)


#specifying that we need only 10 characters
df = open("trash.txt","rt")
st1 = df.read(10)
df.close()
print(st1)


df = open("trash.txt","rt")
while True:#infinte group
    data = df.read(10)
    if not data:
        break #
    print(data)
df.close()



#######Read Line
df = open("trash3.txt","w")
for _ in range(10):
    df.write(s)

df.close()
fdr = open("trash3.txt","rt")
for data in fdr.readlines():
    print(data,end="")
fdr.close()



#METHOD 2
with open ("test.txt","wt") as fd:#this is called context manager
    for _ in range(1):
        fd.write(s)

with open("test.txt","rt") as fdr:
    data = fdr.read()
print(data)
#NO NEED TO CLOSE FILES in context mangaer









#Copying content from file and putting in another
with open ("test.txt","rt") as dfr, open("trash.txt.txt","wt") as fdw:
    data = dfr.read()
    fdw.write(data)
with open("test.txt","r") as fd:
    print(fd.read())



#Doing calulation
with open("tear.txt","rt") as fd:
    for data in fd.readlines():
        a,b = data.split()
        m,n= int(a), int(b)
        fnb ="{0:6d} {1:6d} {2:6d} {3:6d}".format(m,n,m+n,n*m)
        print(fnb)





