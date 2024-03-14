import numpy as np

arr = np.array(['python', 'is', 'cool!'])
spaced = np.char.join(" ", arr)
print (spaced)