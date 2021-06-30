#1 STAR PATTERN 

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


#2 Rotate STAR PATTERN

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


#3 TRIANGLE PATTERN using stars

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


#4 FLOYD'S TRIANGLE

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


#5 print number 1 in the first row, number 2 in the second row, number 3 in the third row, and so on

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

#6

n= int(input("Enter a number: "))
for i in range(n):
  n=1
  for j in range(i+1):
    print(n,end=" ")
    n=n+1
  print()
  
#Output:
Enter a number: 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


#7 Reverse of above patterns

n= int(input("Enter a number: "))
for i in range(1,n+1):
  for j in range(i,0,-1):
    print(j,end=" ")
  print()

#Output:
Enter a number: 5
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1


# CHARACTER PATTERNS

#1 
n= int(input("Enter a number: "))
a=65 # if we want to print alphabets in lowercase we use ascii value from 97-122 and for uppercase 65-90
for i in range(n):
  for j in range(i+1):
    print(chr(a),end=" ")
    a=a+1
  print()
  
#Output:
Enter a number: 5
A 
B C 
D E F 
G H I J 
K L M N O


#2
n= int(input("Enter a number: "))
a=65
for i in range(n):
  for j in range(i+1):
    print(chr(a),end=" ")
  a=a+1
  print()
  
 #Output:
Enter a number: 5
A 
B B 
C C C 
D D D D 
E E E E E
