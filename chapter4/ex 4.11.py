pizzas=['pepperoni','cheese','olives']
friend_pizzas=pizzas[:]
pizzas.append('tikka')
friend_pizzas.append('afghani feast')
print("my favorite pizzas are : ")
for pizza in pizzas:
    print(pizza)
print("\nmy friend's favorite pizzas are : ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)