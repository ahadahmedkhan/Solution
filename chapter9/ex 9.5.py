
class User():

    def __init__(self,first_name , last_name , age):
        self.f_name=first_name
        self.l_name=last_name
        self.age=age
        self.login_attempts=0

    def describe_user(self) :
        full_name = self.f_name.title() +' '+ self.l_name.title()
        user_email=full_name+'@gmail.com'
        print('The user is '+full_name)
        print("User's eamil address is "+ user_email)
        print("user's age is "+str(self.age))

    def greet_user(self):
        print('hello '+self.f_name+'.')


    def increment_login_attempts(self):
        self.login_attempts+=1
        print(self.login_attempts)


    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)

user_1  =User('ahad' , 'ahmed' , 22)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()