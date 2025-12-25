#PATTERN-1
n=5
for i in range(n):
   print(" "*(n-i)+(str(i+1)+" ")*(i+1))

#PATTREN-2
n=5
for i in range(n):
   for j in range(n):
     print(" "*(n-i)+(str(i+1)+" ")*(i+1))

#PATTERN-3
n=6
for i in range(n):
    print((chr(65+i)+' ')*(i+1))
#pattern-4
n=6
for i in range(n,0,-1):
   print(" "*(n-i)+(str(i+1)+" ")*(i+1))

