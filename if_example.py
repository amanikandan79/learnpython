
print("What is your first person name?")
name=input()
print("What is your first person  age?")
age=int(input())

print("What is your second person name?")
name2=input()
print("What is your second person age?")
age2= int(input())

print("\n\n")

if(age > age2) :
    print( name  +" is elder than "+ name2  )

elif(age < age2) :
    print( name+" is younger than "+ name2 )

else :
    print( name +" both are equal age "+name2 )
