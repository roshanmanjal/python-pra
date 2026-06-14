a = int(input("Enter your age:- "))  
# if else and multiple if else [elif]

# multiple if also 
# if(a == 0):
#     print("OK go to end")

if(a >= 18):
    print("You are an adult...")
elif(a <= 0):
    print("You have entered an invalid negative age try again and enter your valid age..!!!")
elif(a == 0):
    print("You have entered 0 age ehich is not valid so try again and enter your valid age..!!!")
else:
    print("You are not an ADULT ")
    
print("End of program")