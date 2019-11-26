class User():

    def __init__(self, first_name, last_name, age):
        self.f_name=first_name
        self.l_name=last_name
        self.age=age

    def describe_user(self) :
        full_name = self.f_name.title() +' '+ self.l_name.title()
        user_email=self.f_name+'@gmail.com'
        print('The user is '+full_name)
        print("User's eamil address is "+ user_email)
        print("user's age is "+str(self.age))

    def greet_user(self):
        print('hello '+self.f_name+'.')

obj_1  =User('ahad' , 'ahmed' , 22)
user_2 =User('sarah','amjad',20)
user_3 =User('ali','khan',20)

obj_1.describe_user()
obj_1.greet_user()
print('\n')
user_2.describe_user()
user_2.greet_user()
print('\n')
user_3.describe_user()
user_3.greet_user()
