try:
    number=int(input("Enter your age: "))
    if number%2==0:
        print("Your age is an even number")
    else:
        print("Your age is an odd number")

except ValueError as ex:
    print("Exception:",ex)