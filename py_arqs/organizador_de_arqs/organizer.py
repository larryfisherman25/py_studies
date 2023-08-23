import os
import shutil

path= '<SEU PATH>'
list_of_file = os.listdir(path)

disk_space_usage_percentage  = (round(int(shutil.disk_usage(path)[1]/(1024**3)) / int(shutil.disk_usage(path)[0]/(1024**3)), 2)) * 100
print(f'This directory has {disk_space_usage_percentage} used disk space.')

for file in list_of_file:
    name, extension = os.path.splitext(file)
    print(name, extension)
    extension = extension[1:]

    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
