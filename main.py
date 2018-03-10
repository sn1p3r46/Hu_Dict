#!/usr/bin/python3

import constants as cs
import io_handler as ioh
import readline 

hu_en_dict = {}
en_hu_dict = {}

def load_data():

    global hu_en_dict
    global en_hu_dict
    
    print ("Trying to load the personal dictionary! :) ")
    res = ioh.load_dictionary()
    if res:
        hu_en_dict, en_hu_dict = res
        print("Personal Dictionary loaded!)")
    else:
        print("Personal Dictionary NOT loaded!")

def main():

    print(cs._welcome_screen)
    
    load_data()

    process_main_input()

    a_i = sanitize_input(a)
    print('You wrote: "{}"'.format(a_i))


def handle_exit():

        if handle_boolean(">>>Do you really want to exit? Type Y[es]/N[o]]"):
            print(">>>Szia!!!")
            ioh.write_dictionary(hu_en_dict)
            exit()

def handle_boolean(question):
    
    while True:
            
        res = input(question)
        if res.lower() in cs._yes_set:
            return True
        elif res.lower() in cs._no_set:
            return False
        else:
            print("Sorry, I did not understand! :(")


def sanitize_input(in_str):

    for i in range(cs._n_of_v):
        in_str = in_str.replace(cs._input_chars[i], cs._output_chars[i])

    in_str = in_str.replace("'", "")
    return in_str


def start_input_mode():

    while True:

        raw_in_0 = input("Type an Hungarian word (or \q to get back): ")

        if not raw_in_0:
            continue

        if raw_in_0.lower() in cs._exit_set:
            break

        clean_in_0 = sanitize_input(raw_in_0)
        print("You typed: '{}'".format(clean_in_0))
        raw_in_1 = input("Now type its meaning: ")
        print("You typed: '{}'".format(clean_in_0))
        
        res = handle_boolean(cs._correct_question_2p.format(clean_in_0, raw_in_1))
        if res:
            en_hu_dict[raw_in_1] = clean_in_0
            hu_en_dict[clean_in_0] = raw_in_1

    print(en_hu_dict)
    print(hu_en_dict)
        

def process_main_input():

    while True:

        in_str = input(cs._help)
        
        if in_str in cs._exit_set:
            handle_exit()

        if in_str in cs._test_set:
            start_test()

        if in_str in cs._input_mode_set:
            start_input_mode()

        else:
            print("\nCommand not understood, maybe a typo?!? :)\n")


if __name__=="__main__":
    main()
