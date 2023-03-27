#!/usr/bin/python3
def magic_calculation(a, b):
    prc = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception("Too far")
            else:
               prc += (a ** b) / i
        except:
            prc = b + a
            break
    return (prc)
