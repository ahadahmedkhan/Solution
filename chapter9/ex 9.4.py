class Restaurant:


    def __init__(self,restaurant_name,cuisine_type):
        self.name= restaurant_name
        self.type=cuisine_type
        self.number_served = 0

    # def set_number_served(self,number):
        # self.number_served=number
        # print('we served ' + str(self.number_served) + ' customers.')



    def increment_number_served(self,number):
        if number>=self.number_served:
            self.number_served += number
            print('we served ' + str(self.number_served) + ' customers.')
        else:
            print('your served number never reamin same')



    def describe_restaurant(self):
        print('Welcome to '+self.name+'.'+
              'We serves '+self.type)


    def open_restaurant(self):
        print('Our Restaurant is open.')

my_restaurant=Restaurant('Salwa','Italian')
print(my_restaurant.name)
print(my_restaurant.type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(30)


# changing num_served by call method(passing a value)
# my_restaurant.set_number_served(30)

# calling before change the num_served
# print('we served '+str(my_restaurant.number_served)+' customers.')

# after directly change the value
# my_restaurant.number_served=10
# print('we served '+str(my_restaurant.number_served)+' customers.')