import os

variables = {'file': ""}

def print_menu():
    print("middle grip - 0")
    print("right grip - 1")
    print("left grip - 2")
    print("all of the above - 3")
    print("")
    print("write \"use\" followed by an option number")
    print("")


def clean_input(_input):

    #Removes all spaces in the beginning of input
    while(_input[0] == " "):
        _input = _input[1:len(_input)]

    #Removes all spaces in the end of input
    while(_input[len(_input)-1] == " "):
            _input = _input[0:len(_input)-1]

    _input_remove_list = []

    #Detects all double spaces and adds their location to _input_remove_list
    for i in range(1, len(_input)-1):
        if(_input[i-1] == " " and _input[i] == " "):
            _input_remove_list.append(i)

    #Removes all the indexes saved in _input_remove_list
    for i in range(len(_input_remove_list)):
        _input = _input[:_input_remove_list[i]] + _input[_input_remove_list[i] + 1:]

        for i in range(len(_input_remove_list)):
            _input_remove_list[i] -= 1

    equal_pos = _input.find("=")

    #removes spaces beside equal sign
    if(equal_pos != -1):
        if(equal_pos-1 > 0):
            if(_input[equal_pos-1] == " "):
                _input = _input[:equal_pos-1] + _input[equal_pos-1 + 1:]
                equal_pos = _input.find("=")

        if(equal_pos+1 < len(_input)):
            if(_input[equal_pos+1] == " "):
                _input = _input[:equal_pos+1] + _input[equal_pos+1 + 1:]


    return _input

def main():
    while True:
        console_input = clean_input(input("BCLU>"))

        elif(console_input.startswith("set"):
             pass

main()




