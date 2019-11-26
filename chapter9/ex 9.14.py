from random import randint

class Die:
    def __init__(self):
        self.sides=6

    def roll_6_sided_die(self):
        print('Die has ' + str(self.sides) + ' sides')
        x = randint(1, 6)
        print(x)
    def roll_10_sided_die(self):
        self.sides=10
        print('Die has ' + str(self.sides) + ' sides')
        x = randint(1, 10)
        print(x)

    def roll_20_sided_die(self):
        self.sides=20
        print('Die has ' + str(self.sides) + ' sides')
        x = randint(1, 20)
        print(x)


die=Die()
i=0
for i in range(10):
    print(die.roll_6_sided_die())
for i in range(10):
    print(die.roll_10_sided_die())
for i in range(10):
    print(die.roll_20_sided_die())
