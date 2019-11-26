sandwich_orders=['tuna','pastrami','chicken','italiano','French','pastrami','pastrami']
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches=[]
i=0
while i<len(sandwich_orders):
    print("I made your "+sandwich_orders[i]+" sandwich .")
    finished_sandwiches.append(sandwich_orders[i])
    i+=1
for made in finished_sandwiches:
    print(made)