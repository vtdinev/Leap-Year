year = int(input("Year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print("leap")
    elif year % 400 == 0:
        print("leap")
    else:
        print("not leap")
else:
    print("not leap")
