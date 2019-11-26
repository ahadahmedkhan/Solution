invitation=['sara', 'john', 'farooq', 'eric', 'ahmed', 'amjad']

print("\nsorry !! i have place for only two person .\n")

#remove the extra names by using pop() function

print("Sorry "+invitation.pop()+" you are not invited !! ")
print("Sorry "+invitation.pop()+" you are not invited !! ")
print("Sorry "+invitation.pop()+" you are not invited !! ")
print("Sorry "+invitation.pop()+" you are not invited !! ")

print("\n"+invitation[0] +" you are still invited ..")
print("\n"+invitation[1] +" you are still invited ..\n\n")

# now delete a list
del invitation

#or it can be done by this way
#del invitation[0]
#del invitation[1]

# when program is compiled an error is occur "invitation is not defined" when we delete every elemnet of list it will become empty .
print(invitation)
