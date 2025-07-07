import os

path_directory = '/Users/andreewmac/Downloads/'

content_directory = os.listdir(path_directory)
for file in content_directory:
    if file.endswith('.wav'):
        os.remove(os.path.join(path_directory, file))

