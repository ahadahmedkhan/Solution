class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name= restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print('Welcome to '+self.name+'.'+
              'We serves '+self.type)
    def open_restaurant(self):
        print('Our Restaurant is open.')

# my_restaurant=restaurant('Salwa','Italian')
# print(my_restaurant.name)
# print(my_restaurant.type)
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()