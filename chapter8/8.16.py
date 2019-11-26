import printing_function
printing_function.print_name('ahad')

from printing_function import print_name
print_name('ahad')

from printing_function import print_name as pn
pn('ahad')

import printing_function as pf
pf.print_name('ahad')

from printing_function import*
print_name('ahad')
