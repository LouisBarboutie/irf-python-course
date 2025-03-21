"""
Remember to install the local package with:
    > py -m pip install -e . 
from the directory where the .toml file is located
"""
import matplotlib.pyplot as plt
import numpy as np
import example_package_louis.stringutils as pkg

"""
    Own package utilization
"""

STR1 = 'VOG!lo olH'
STR2 = 'el,Wrd ROY' 

res = pkg.stringutils.interleave(STR1, STR2)
print(res)

"""
    File I/O
"""
with open('testfile.bin', 'wb') as file:
    text = 'This is the first line\nThis is the second line'
    content = text.encode(encoding='utf-8', errors='strict')
    file.write(content)

with open('testfile.bin', 'rb') as file:
    content = file.read()
    text = content.decode(encoding='utf-8', errors='strict')
    print(text)



"""
    Plotting
"""

# Generate the data for the plot.
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Setup and display the plot.
fig, ax = plt.subplots()
fig.suptitle('A simple sine wave')
ax.plot(x, y)
ax.set_xlabel('Angle [rad]')
ax.set_ylabel('Amplitude')
plt.show()