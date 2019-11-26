class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name= restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print('Welcome to '+self.name+'.'+
              'We serves '+self.type)
    def open_restaurant(self):
        print('Our Restaurant is open.')
# making 3 different instance

my_restaurant1=Restaurant('Salwa','Italian')
my_restaurant2=Restaurant('PAk','Desi')
my_restaurant3=Restaurant('Meat Eat','Chinese')

my_restaurant1.describe_restaurant()
my_restaurant1.open_restaurant()
print('\n')
my_restaurant2.describe_restaurant()
my_restaurant2.open_restaurant()
print('\n')
my_restaurant3.describe_restaurant()
my_restaurant3.open_restaurant()
