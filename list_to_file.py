
list_value = [1] * 13

print(list_value)
with open('listfile.txt', 'w') as filehandle:
    for listitem in list_value:
        filehandle.write('%s\n' % listitem)
