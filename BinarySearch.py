#Binary search
#To apply Binary Search List must be in sorted order 

#Recursive Method

def binarySearchRecursive(data,search,low,high):
    
    if high>=low:
        
        mid=(high+low)//2
        
        if(data[mid]==search):  
            print("Element %d is found at index %d "%(data[mid],mid+1))
        
        elif(data[mid]>search):
            binarySearch(data,search,low,mid-1)
        
        else:
            binarySearch(data,search,mid+1,high)
    else:
        print("Element %d is not found"%(search))
        

#Iterative Method

def binarySearchIterative(data,search,size):
    low=0
    high=size-1
    mid=0
    
    while(high>=low):
        mid=(low+high)//2
        
        if(data[mid]>search):
            high=mid-1
        elif(data[mid]<search):
            low=mid+1
        else:
            print("Element %d is found at index %d "%(data[mid],mid+1))
            return
          
    print("Element %d is not found"%(search))       
    
  
data=[]
size=int(input("Enter number of elements in list: "))
print("Enter elements: ")

for i in range(size):
    data.append(int(input()))
    
search=int(input("Enter element to search in list: "))    
binarySearchRecursive(data,search,0,size)
binarySearchIterative(data,search,size)
