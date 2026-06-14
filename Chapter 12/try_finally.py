def main():  
    try:
        a = int(input("Enter a number: "))
        print(a)
    except Exception as e:
                print(e)
                
    finally:  # finally is used to execute this block if try/except meets with an error 
                # this is most used in function like def or some.
                # when try/except gets wrong input it fails to print below line if finally is not used
     print("I am inside finally.")
     
main()