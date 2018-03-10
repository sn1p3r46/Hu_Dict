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
        print("Personal Dictionary loaded! :)")
        print("Your dictionary contains {} terms".format(len(hu_en_dict)))
        dictionary_print() 
    else:
        print("Personal Dictionary NOT loaded!")

def start_delete_term():

    if not hu_en_dict:
        print("Empty dictionary, nothing to delete here!")
        return

    to_del = input(">>>Type in Hungarian what you want to delete: ")
    hu_to_del = sanitize_input(to_del)
    en_to_del = hu_en_dict.get(hu_to_del)


    if  en_to_del is None:
        print(">>>Term '{}' not found.".format(hu_to_del))

    else:
        del hu_en_dict[hu_to_del]
        del en_hu_dict[en_to_del]
        ioh.write_dictionary(hu_en_dict)
        print(">>>'{}' has been deleted!".format(hu_to_del))
        print(">>>'{}' has been deleted!".format(en_to_del))
        print("Dictionary now contains {} term(s)".format(len(hu_en_dict)))


def main():

    print(cs._welcome_screen)

    load_data()

    process_main_menu_input()


def handle_exit():

        if handle_boolean(">>>Do you really want"
                          "to exit? Type Y[es]|[ENTER]/N[o]]:"):
            ioh.write_dictionary(hu_en_dict)
            print(">>>Szia!!!")
            exit()


def handle_boolean(question):

    while True:

        res = input(question)
        if res.lower() in cs._yes_set or res=='':
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

    def rlinput(prompt, prefill=''):
       readline.set_startup_hook(lambda: readline.insert_text(prefill))
       try:
          return input(prompt)
       finally:
          readline.set_startup_hook()

    while True:

        raw_hu_in = input("Type an Hungarian word (or \q to get back): ")

        if not raw_hu_in:
            continue

        if raw_hu_in.lower() in cs._exit_set:
            break

        while True:
            clean_hu = sanitize_input(raw_hu_in)
            raw_hu_in = rlinput("You typed: '{}', correct?"
                                "[press ENTER if correct]: ".format(clean_hu),
                                clean_hu)
            new_clean_hu = sanitize_input(raw_hu_in)

            if new_clean_hu == clean_hu:
                clean_hu = new_clean_hu
                break

        while True:

            en_in = input("Now type its meaning: ")
            raw_en_in = rlinput("You typed: '{}', correct?"
                                "[press ENTER if correct]: ".format(en_in),
                                en_in)
            new_clean_en = sanitize_input(en_in)

            if new_clean_en == en_in:
                en_in = new_clean_en
                break

        # print("You typed: '{}'".format(clean_in_0))
        # res = handle_boolean(cs._correct_question_2p
        #                      .format(clean_hu, raw_in_1))

        en_hu_dict[en_in] = clean_hu
        hu_en_dict[clean_hu] = en_in

    print(en_hu_dict)
    print(hu_en_dict)

def dictionary_print():
    print("\n\t['HU' ==> 'EN']\n")
    hu_list = list(hu_en_dict.keys())
    hu_list.sort()
    for hu in hu_list:
        print("\t'{}' ==> '{}'".format(hu, hu_en_dict[hu]))

def process_main_menu_input():

    while True:

        in_str = input(cs._main_menu)

        if in_str in cs._exit_set:
            handle_exit()

        elif in_str in cs._test_set:
            start_test() # TODO implement

        elif in_str in cs._input_mode_set:
            start_input_mode()

        elif in_str in cs._delete_set:
            start_delete_term()

        else:
            print("\nCommand not understood, maybe a typo?!? :)\n")


if __name__=="__main__":
    main()
