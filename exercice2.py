from collections import OrderedDict

x = x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 

y = OrderedDict(sorted(x.items(), key=lambda t : [1]))

print(y)
