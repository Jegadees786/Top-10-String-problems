str1=input("Enter the string:")
arr=str1.split(' ')
temp=0
for i in range(len(arr)-1):
    if(arr[i]<arr[i+1]):
        temp=len(arr[i])
    else:
        i +=1
print("The closest string is ",temp)