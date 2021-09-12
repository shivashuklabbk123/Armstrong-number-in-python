n = int(input("Enter the number n::"))
temp = n
sum = 0
while(n>0):
    #first separate the number
    dig = n%10
    n= n//10
    #then sum the number of cube
    sum = sum + dig**3
if(sum == temp):
    print("The number is Armstrong number")
else:
    print("It is not Armstrong number")        