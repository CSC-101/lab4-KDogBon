class Pet:
    def __init__(self, __name, __animal_type, __age):
        self.name = __name
        self.animal_type = __animal_type
        self.age = __age


    def __str__(self) -> str:
        return "name: {}, type: {}, age: {}".format(self.name, self.animal_type, self.age)


    def __repr__(self) -> str:
         return "name: {}, type: {}, age: {}".format(self.name, self.animal_type, self.age)

    '''getting code'''

    def get_nameThis(self) -> str:
        return self.name



    def get_anmial_typeThis(self) -> str:
         return self.animal_type


    def get_ageThis(self):
        return self.age

    ''' setting code'''

    def set_nameThis(self, x):
        self.name = x


    def set_anmial_typeThis(self, x):
        self.animal_type = x


    def set_ageThis(self, x):
        self.age = x


myDog = Pet("bodi", "dog", 100)
print(myDog)