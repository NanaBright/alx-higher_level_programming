#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    #prc - variable to be initialised/used
    prc = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        else:
            prc += 1

    print()
    return prc
