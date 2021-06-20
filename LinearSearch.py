#Linear Search 

def linearSearch(l,a):
    for i in l:
        if(a==i):
            return 1 
    return 0
  
l=[]
n=int(input("Enter number of elements in list: "))
print("Enter elements: ")
for i in range(n):
    l.append(int(input()))
a=int(input("Enter element to search in list: "))    
b=linearSearch(l,a)  
if(b==0):
    print("Element",a,"is not present in list")
else:
    print("Element",a,"is present in list")
    
  
