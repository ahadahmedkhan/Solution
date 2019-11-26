from user import User
class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilege = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["add post", "delete post", "add user", "delete user"]

    def show_privileges(self):
            print(' Privileges of Admin')
            for privilege in self.privileges:
                print(privilege)