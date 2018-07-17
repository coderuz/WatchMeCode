import os
files = os.listdir('..')
print(files)
print(os.path.isdir('../'+files[2]))
