import os 
fh=open(r"C:\Users\appub\OneDrive\Desktop\waste folder\copy_4.txt","w")

a,b,c,d=input("enter any programming language").split(",")
fh.write(a+"\n")
fh.write(b+"\n")
fh.write(c+"\n")
fh.write(d+"\n")
fh.close()
