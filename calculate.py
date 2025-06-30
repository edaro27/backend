
#Compute sum of list of numbers [1,...,n]
l=[1,2,3,4,5]
print(sum(l))

#Function to check if string is palindrome
def pal(x):
    x=x.lower()
    x=x.replace(" ","")
    return print(x == x[::-1])

test="anita lava la tina"
pal(test)
    
#Dictionary mapping names to ages and print oldest person
people={"Mary": 22, "Joe": 13, "Mike": 28}
for name, age in people.items():
    oldest=0
    if age>oldest: 
        oldest=age
        oldname=name
print("The oldest person is",oldname,"at", oldest)

