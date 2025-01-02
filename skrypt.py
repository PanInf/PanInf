n=int(input("test: "))
print("*"*n)
p=n//3
w2=0
w3=0
for i in range(p):
  for j in range(n):
    if (j==n//2 or j==n//2+1 or j==n//2-1):
      print("*",end="")
    else:
      print(" ",end="")
  print()
for i in range(i):
  w3=i-1
  print(" "*w3,end="")
  w2=w2-i
  print("*"*w2,end="")
  print()