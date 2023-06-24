print("My {0} name is {1}".format("name","Hemachandiran"))

" find prime number in python"

num = int(input())
for i in range(2,num+1):
    if(num%i)==0:
        print("not prime")
        break
print("Prime")