#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self,name='name',breed='Chihuahua'):
        self.name = name
        self.breed = breed
        
    def get_name(self):
        return self._name    
    
    def set_name(self,name):
        if ((type(name) is str) and (len(name) > 1 and len(name) < 25)):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    name = property(get_name,set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self,breed):
        self._breed = None
        for approvedBreed in APPROVED_BREEDS:
            if breed == approvedBreed:
                self._breed = breed
                break
        if self._breed == None:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed,set_breed)                       
    pass