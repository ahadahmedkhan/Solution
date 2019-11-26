glossary={
    'string':' A series of character.',
    'comment':' A note in a program that the interpreter ignores.',
    'list':' A collection of item in a particular order.',
    'loop':' Work through colection of items, one at a time.',
    'dictionary':'A collection of key-value pair.',
    }
glossary['sorted']='A function that arranges a list in order.'
glossary['set']='A function that makes a list unique.'
glossary['key']='A function for accesing all keys from a dictionary.'
glossary['value']='A function for accesing all values from a dictionary.'
glossary['del']='To completely remove a key-value pair.'

for word,meaning in glossary.items():
    print('\n'+word.title()+' : '+meaning)












