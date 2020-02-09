import os

for path, subdirs, files in os.walk('ml-tensorflow-samples/data'):
    for name in files:
        filename = os.path.join(path, name)
        if name.endswith('class0.png'):
            destination_class = '0'
        else:
            destination_class = '1'
        os.rename(filename, os.path.join('ml-tensorflow-samples/data', destination_class, name))