prompt = "\nEnter the topping for pizza you like : "
prompt += "\nEnter 'quit' to end the program. "

topping = ""
while True:
    topping = input(prompt)
    if topping=="quit":
        break
    else:
        print("you added " + topping.title()+ " in your toppings !!")