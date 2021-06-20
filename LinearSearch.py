#Linear Search 

def linearSearch(data,search,size):
    for i in range(size):
        if data[i]==search:
            print("Element %d found at %d:"%(data[i],i))
            return
    print("Element %d is not found"%search)       

  
data=[]
size=int(input("Enter number of elements in list: "))
print("Enter elements: ")

for i in range(size):
    data.append(int(input()))
    
search=int(input("Enter element to search in list: "))    
linearSearch(data,search,size)  
