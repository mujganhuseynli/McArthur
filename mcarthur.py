while True:
    month = input("Enter your birth month: ")
    age = input("Enter your age: ")
    if ((not month.isdigit() or (int(month)>12 or int(month)<1)) or (not age.isdigit() or int(age)<1)):
        print("You entered wrong month or age")
        continue
    m = int(month)
    m *= 2
    m += 5
    m *= 50
    m += int(age)
    m -=365
    print("The special number is ", m)
    m += 115
    if str(m)[0]==month:
        print("Your birth month is ", str(m)[0])
        print("Your age is ", str(m)[1:])
    elif str(m)[:2]==month:
        print("Your birth month is ", str(m)[:2])
        print("Your age is ", str(m)[3:])
    ans = input("Do you want to continue? y/n ")
    if ans=="y":
        continue
    elif ans=="n":
        print("Bye!")
        break
