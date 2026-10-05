from typing import List

def read_integers() -> List[int]:
    string = input()
    elements = string.split(",")
    my_list = []
    for element in elements:
       element = int(element)
       my_list.append(element)
    return my_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
