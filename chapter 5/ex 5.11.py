Ordinal_numbers=list(range(1,10))
for Ordinal_number in Ordinal_numbers:
    if Ordinal_number==1:
        print(str(Ordinal_number) + "st")
    elif Ordinal_number == 2:
        print(str(Ordinal_number) + "nd")
    elif Ordinal_number == 3:
        print(str(Ordinal_number) + "rd")
    else:
        print(str(Ordinal_number)+ "th")