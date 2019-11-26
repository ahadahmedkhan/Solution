users=[]
if users:
    for user in users :
        if user == 'admin':
            print('hello'+user + ',would you like to see a status report?')
        else :
            print('hello '+user+',thank you for loggong in again !!')
else:
    print("we need to find some users !!")