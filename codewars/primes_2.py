number = raw_input("Enter a number: ")

if number.isdigit():
    for n in range(2, 100):
        if int(number) % n == 0:
            print "Your number is a composite number."
            break
    else:
        print "Your number is a prime number."
else:
    print "Not a number"
