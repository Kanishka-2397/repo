print( "temperature converter")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
choice = input("choose an option[1,2]:")

if choice == "1":
    celsius = float(input("enter the number:"))
    print (celsius * (9/5)+ 32)
elif choice == "2":
    fahrenheit = float(input("enter the number:"))
    print (fahrenheit - 32 * (5/9))
else:
    print("invalid choice")
