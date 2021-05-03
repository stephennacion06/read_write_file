# define an empty list


while True:
    value_list = []
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            value_list.append(int(currentPlace))
    print(value_list)
