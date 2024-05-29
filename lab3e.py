#!/usr/bin/env python3

#AuthorID: mcini

my_list = [100,200,300,'six hundred']

def give_list():
    return my_list

def give_first_item():
    output = str(my_list[0])
    return output

def give_first_and_last_item():
    output_list = [my_list[0], my_list[-1]]
    return output_list

def give_second_and_third_item():
    output_list = [my_list[1], my_list[2]]
    return output_list

if __name__ == '__main__': 
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())