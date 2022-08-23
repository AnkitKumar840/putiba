# Write a python script to print first N odd natural numbers in reverse order

n=int(input("Enter a number="))
i=n
print()
print("Odd natural numbers:")
while i>=1:
    print(i*2-1,end=" ")
    i-=1