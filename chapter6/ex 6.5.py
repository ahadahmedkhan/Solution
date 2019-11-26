Rivers={'nile':'egypt','indus':'pakistan','jehlum':'pakistan'}

for river,country in Rivers.items():
    print('The '+river.title()+' runs through '+country.title()+'.')

print('\n List of rivers :')
for river in Rivers.keys():
    print(river.title())

print('\n List of countries :')
for country in Rivers.values():
    print(country.title())