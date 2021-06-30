# STAR PATTERN 

n= int(input("Enter a number: "))
for i in range(n):
  for j in range(i+1):
    print("*",end="")
  print()
  
#Output:
Enter a number: 4
*
**
***
****


# Rotate STAR PATTERN

n= int(input("Enter a number: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
    
#Output:
Enter a number: 5
    *
   **
  ***
 ****
*****


# TRIANGLE PATTERN using stars

n= int(input("Enter a number: "))
for i in range(n):
    for j in range((n - i) - 1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
  
#Output:
Enter a number: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * *


# FLOYD'S TRIANGLE

k=1
n= int(input("Enter a number: "))
for i in range(n):
  for j in range(i+1):
    print(k,end=" ")
    k=k+1
  print()
  
#Output:
Enter a number: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 


# print number 1 in the first row, number 2 in the second row, number 3 in the third row, and so on

n= int(input("Enter a number: "))
for i in range(n):
  for j in range(i+1):
    print(i+1,end="")
  print()
  
#Output:
Enter a number: 4
1
22
333
4444
