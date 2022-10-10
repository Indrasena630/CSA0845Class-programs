num=float(input("enter the number:"))
result=0
for i in (1,num):
    if(num%i==0):
        result=result+i
if(result==num):
    print(num,"it is aperfect number")
else:
    print(num,"it is not a perfect number")
