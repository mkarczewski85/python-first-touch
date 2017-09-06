
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:12:31 2017

@author: Maciej
"""
#%%
def compare(a, b):

    if a<0 or b<0:
        print("Wartosc nie moze byc ujemna. Zmieniam na wartosc bezwgledna!")
        a=abs(a)
        b=abs(b)
    print("Zmienna a = ", a)
    print("Zmienna b = ", b)
    if a>b:
        print(a, " jest większe od ", b)
    if b>a:
        print(b, " jest większe od ", a)
    else:
        print(a, " i ", b, "są rowne!")    
#%%
def split_string(line, option):
    words = line.split()
    for word in words:
        if word.endswith(","): word = word[:-1]
        if word.endswith("."): word = word[:-1]
        if option == True:
            print(word)
    return words
#%%
def tell_number_even(number):

    if (number%2) == 0:
        return True
    else:
        return False
#%%
def how_many_chars(words):
    words_dict = {}
    for word in words:
        words_dict[word] = len(word)
    return words_dict
#%%
def calc_average(words):
    result = sum(words.values())/len(words)
    return round(result)
#%%
def print_inv():
    line = ('Litwo, ojczyzno moja\t\n\t\tty jesteś jak \'zdrowie\'\n'
            '\tile cię trzeba cenić ten tylko\n'
            'się dowie,\t\t\n\tkto cię stracił')
    return line
#%%
def main():
    a = int(input("Wprowadz a: "))
    b = int(input("Wprowadz b: "))    
    compare(a, b)
    line = input("\nWprowadz linie tekstu: ")
    split_string(line, True)
    number = int(input("\nWprowadz wartosc do sprawdzenia: "))
    if tell_number_even(number):
        print("Wartosc jest parzysta!\n")
    else:
        print("Wartosc nie jest parzysta!\n")
    words = split_string(line, False)
    my_dict = how_many_chars(words)
    for keys,values in my_dict.items():
        print(keys, ": ", values)
    print("Srednia ilosc liter w tekscie: ", calc_average(my_dict))
    print("\n", print_inv())
    
#%%
if __name__ == "__main__":
    main()
