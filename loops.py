# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 08:58:37 2017

@author: Maciej
"""
from collections import Counter
#%%
def check_for_letter(string):
    flag = True
    
    while flag:
        char = input('Jakiej litery szukasz?: ')
        if len(char)>1:
            print('Możesz podać tylko jedną literę!')
        else:
            flag = False
                
    if char in string:
        print('W napisie znajduje się litera ', char)
    else:
        print('W napisie nie ma litery ', char)

#%%
def check_for_letter_file(filename):
    
    flag = True
    while flag:
        char = input('Jakiej litery szukasz?: ')
        if len(char) > 1 or str.isdigit(char):
            print('Możesz podać tylko jedną >>literę<<!')
        else:
            flag = False
    all_letters = 0
    letter_counter = 0
    with open(filename) as file:
        while file.read(1):
            next_char = file.read(1)
            if next_char != ' ': all_letters += 1
            if str.lower(next_char) == str.lower(char):
                letter_counter += 1
    
    print('W tekscie znaleziono ', letter_counter,   
    'przypadkow wystapienia znaku ', char)
    per_average = letter_counter/all_letters*100
    print('Litera ', char, ' stanowi ok ', round(per_average), 
          ' % wszystkich znakow (', all_letters, ')')
#%%
def return_wordlist(filename):
    
    with open(filename) as file:
        wordcount = Counter(file.read().split())

    for item in sorted(wordcount.items()): print("{} {}".format(*item))
#%%
def set_of_letters(filename):
    letters = {}
    with open(filename, "rt", encoding="utf-8") as file:
        while file.read(1):
            char = str.lower(file.read(1))
            if char in letters:
                letters[char] += 1
            else:
                if char != ' ' or char != ',' or char != ',':
                    letters.update({char: 1})
    for item in sorted(letters.items()): print("{} {}".format(*item))
    message = 'Najczęsciej wystepuje litera: '
    print(message, max(letters, key=lambda i: letters[i]))
            
#%%
def main():
    filename = 'slowa.txt'
#    check_for_letter_file(filename)
#    print('\n')
#    return_wordlist(filename)
#    print('\n')
    set_of_letters(filename)
#%%
if __name__ == "__main__":
    main()