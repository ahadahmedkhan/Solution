def sandwich(*items):
    print("Items in a Sandwich you want : ")
    for item in items:
        print("-"+item)

sandwich('chicken')
sandwich('chees','club','chicken')