import os
fh=open("C:/Users/appub/OneDrive/Documents/Arduino/code007/code007.ino","w")
fh.write("in sms center")
fh.close()
fh=open("C:/Users/appub/OneDrive/Documents/Arduino/code007/code007.ino","r")
print(fh.read)
fh.close()

os.chdir("C:/Users/appub/OneDrive/Documents/Arduino/code007/")#creates a file in the folder
file=open("mi 002.txt","w")
file.write("hi ,how r u")
file.close()
os.mkdir#creates a folder
os.remove#to remove the file