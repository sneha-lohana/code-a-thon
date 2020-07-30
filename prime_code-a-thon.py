n = int(input("Enter a number"))
flag=True
for i in range(2, n):
    if n%2==0:
        flag=False
if flag:
    print("Prime")
else:
    print("Not Prime")
