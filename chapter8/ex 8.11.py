magicians =['john','sara','kashif','adam']

def show_magicians(magicians):
    for magician in magicians :
        print('Hi this is '+magician.title()+ '.')

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician =  ' The Great '+magician
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

show_magicians(magicians)
print("\n")
make_great(magicians[:])
print("Great magicians : ")
show_magicians(magicians)
print("\nOriginal magicians : ")
show_magicians(magicians)