# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 21:52:38 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 10:58:21 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random
import time
import unittest


def shuffle_word_list(text):
    list_len = len(text) - 1
    while list_len >= 1:
        list_len = list_len - 1
        idx = int(str(time.process_time()).split('.')[-1][-1])
        if list_len == idx:
            continue
        if idx > len(text) - 1:
            idx = int(idx / 2)
        text[idx], text[list_len] = text[list_len], text[idx]
    return text


def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings. 
    Option precise if a action is performed to the substrings before it is yielded. 
    '''
    if sep ==  "":
        print("‼️  ERROR: separator is empty")
        sys.exit()

    if not isinstance(sep, str):
        print("‼️  ERROR: separator is not a string")
        sys.exit()

    if not isinstance(text, str) or option not in [None, "shuffle", "unique", "ordered"]:
        yield "‼️  ERROR: option is not valid"
    else:
        if option is None:
            word_list = text.split(sep)
        elif option == "shuffle":
            word_list = shuffle_word_list(text.split(sep))
        elif option == "unique":
            word_list = list(dict.fromkeys(text.split(sep)))
        elif option == "ordered":
            word_list = sorted(text.split(sep))
        for elem in word_list:
            yield elem


class Test(unittest.TestCase):

    def test_generator_errors_01(self):
        print("\n--------------------------")
        for i in generator(text, sep=""):
            print(i)
    
    def test_generator_errors_02(self):
        print("\n--------------------------")
        for i in generator(text, sep= 6 ):
            print(i)


if __name__ == '__main__':

    text = "Le Lorem Ipsum est simplement du faux texte. Lorem Ipsum"
    print(f"\ntext: {text}")
    print("\n-------------------------------\n")

    print("Regular split :")
    for i in generator(text):
        print(i)
    print("\n-------------------------------\n")

    print("Split with sep :")
    for i in generator(text, sep="a"):
        print(i)
    print("\n-------------------------------\n")

    print("Shuffle split :")
    for i in generator(text, option="shuffle"):
        print(i)
    print("\n-------------------------------\n")

    print("Unique split :")
    for i in generator(text, option="unique"):
        print(i)
    print("\n-------------------------------\n")

    print("Ordered split :")
    for i in generator(text, option="ordered"):
        print(i)
    print("\n-------------------------------\n")

    print("Invalid split :")
    for i in generator(text, option="invalid"):
        print(i)
    print("\n-------------------------------\n")

    print("Invalid split :")
    for i in generator(text, option = 6):
        print(i)
    print("\n-------------------------------\n")
    
    # Force ERRORS 
    time.sleep(1)
    unittest.main()
