from collections import OrderedDict


glossary = OrderedDict()
glossary['string'] = ' A series of character.'
glossary['comment'] = ' A note in a program that the interpreter ignores.'
glossary['list'] = ' A collection of item in a particular order.'
glossary['loop'] = ' Work through colection of items, one at a time.'
glossary['dictionary'] = 'A collection of key-value pair.'
glossary['sorted'] = 'A function that arranges a list in order.'
glossary['set'] = 'A function that makes a list unique.'
glossary['key'] = 'A function for accesing all keys from a dictionary.'
glossary['value'] = 'A function for accesing all values from a dictionary.'
glossary['del'] = 'To completely remove a key-value pair.'
for word, meaning in glossary.items():
    print('\n' + word.title() + ' : ' + meaning)
