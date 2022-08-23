# Write a python script to print first N even natural numbers in reverse order

n=int(input("Enter a number="))
i=n
while i>=1:
    print(i*2,end=" ")
    i-=1