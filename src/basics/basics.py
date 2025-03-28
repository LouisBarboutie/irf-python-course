"""
Remember to install the local package with:
    > py -m pip install -e . 
from the directory where the .toml file is located
"""

import tutorialpackage.examplemodules as pkg
#from tutorialpackage.examplemodules import string, plot, io


"""
    Own package utilization
"""

STR1 = 'VOG!lo olH'
STR2 = 'el,Wrd ROY' 

res = pkg.string.interleave(STR1, STR2)
print(res)



"""
    File I/O
"""

path = 'testfile.bin'
text = 'This is the first line\nThis is the second line'

pkg.io.binarywrite(path, text)
content = pkg.io.binaryread(path)
print(content)



"""
    Plotting
"""

pkg.plot.quickplot_sine()