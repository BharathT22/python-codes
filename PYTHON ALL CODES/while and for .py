'''num=776
sum=0
rev=0
for i in range(len(str(num))):
    rem=num%10
    sum=sum+rem
    rev=(rev*10)+rem
    num=num//10
print(rev)



num=786
temp=num
rev=sum=0
while(num>0):
  rem=num%10
  sum=sum+rem
  rev=(rev*10)+rem
  num=num//10
print(sum,"===>",rev)
if(rev==temp):
  print("pal")
else:
  print("N0")'''

'''i=1
even=[]
odd=[]
while(i<=10):
    if(i%2==0):
      even.append(i)
    else:
      odd.append(i)
    i=i+1
print(even)
print("***************")
print(odd)'''

even=[]
odd=[]
for i in range(1,11):
  if(i%2==0):
      even.append(i)
  
  else:
      odd.append(i)
print(even)
print("***************")
print(odd)
  