# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:15:38 2017

@author: Maciej
"""
#%%
class Name_Class(object):
       
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
    
    def display(self):
        print('Name:', self._name, 'Surname:', self._surname, 'Age:', self._age)
    

#%%
class Info_Class(Name_Class):
    
    def __init__(self, name, surname, age, salary):
        Name_Class.__init__(self, name, surname, age)
        self._salary = salary
    
    def display(self):
        super().display()
        print('Salary:', self._salary)
#%%
class Storage_Class(object):
    
    employed = None
    unemployed = None
    
    def __init__(self, employed = [], unemployed = []):
        self.employed = employed
        self.unemployed = unemployed
        
    def add_item(self, item):
        self.item = item
        if isinstance(self.item, Info_Class):
            self.employed.append(self.item)
        elif isinstance(self.item, Name_Class):
            self.unemployed.append(self.item)
        else:
            print('Błędny obiekt!')
       
    def get_employed(self, index):
        if index < len(self.employed):
            return self.employed[index]
        else: return None
    
    def get_unemployed(self, index):
        if index < len(self.unemployed):
            return self.unemployed[index]
        else: return None
#%%
def diff_objects(data):
    if len(data) < 4:
        return True
    else: return False
#%%
def read_file(filename):
    tmp_item = None
    storage = Storage_Class()
    with open(filename, "rt", encoding="utf-8") as file:
        for line in file:
            data = line.split(',')
            if diff_objects(data):
                tmp_item = Name_Class(data[0], data[1], data[2])
            else: 
                tmp_item = Info_Class(data[0], data[1], data[2], data[3])
            storage.add_item(tmp_item)
    return storage
            
#%%
def main():
    """       
    dane1 = Info_Class('Jan', 'Kowalski', '35', '3400')
    dane2 = Info_Class('Bernard', 'Nowak', '50', '4400')
    dane3 = Name_Class('Michał', 'Wisniewski', '21')
    dane4 = Name_Class('Adam', 'Zawadzki', '54')
   
    set_of_data = [dane1, dane2, dane3]
    
    set_of_data[0].display()
    set_of_data[1].display()

    storage = Storage_Class()
    storage.add_item(dane1)
    storage.add_item(dane2)
    storage.add_item(dane3)
    storage.add_item(dane4)
    
    storage.get_employed(0).display()
    storage.get_employed(1).display()
    storage.get_unemployed(0).display()
    storage.get_unemployed(1).display()
    """
storage = read_file('dane.txt')

for item in storage.employed:
    item.display()

for item in storage.unemployed:
    item.display()
#%%
if __name__ == "__main__":
    main()