#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if x > len(my_list):
            raise IndexError

        for i in my_list[0:x]:
            print(i, end="")
        return x
    except IndexError:
        for i in my_list[0:len(my_list)]:
            print(i, end="")
        return len(my_list)
    finally:
        print()
