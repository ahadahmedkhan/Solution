favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
new_list = ['jen', 'paul', 'edward', 'adam']
for name in favorite_languages.keys():
    print(name)
    if name in new_list:
        print(name.title()+' thanks for reponding .')
    else:
        print(name.title()+' please take our poll.')