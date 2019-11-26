
class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name= restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print('Welcome to '+self.name+'.'+
              'We serves '+self.type)
    def open_restaurant(self):
        print('Our Restaurant is open.')

class Icecream_stand(restaurant):
        def __init__ (self,restaurant_name,cuisine_type):
            super().__init__(restaurant_name,cuisine_type)
            self.flavors=['mango','pine_apple','vanilla','chocolate']

        def display_flavor(self):
            print(self.flavors)


obj=Icecream_stand('peshawri','icecream parlour')
obj.display_flavor()