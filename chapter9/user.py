class User:

    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.f_name.title() + ' ' + self.l_name.title()
        user_email = full_name+'@gmail.com'
        print('The user is ' + full_name)
        print("User's eamil address is " + user_email)
        print("user's age is "+str(self.age))