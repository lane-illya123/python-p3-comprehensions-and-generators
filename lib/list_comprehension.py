#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers

def make_exclamation(sentence_list):
    add_sign = [sentence + '!' for sentence in sentence_list]
    return add_sign