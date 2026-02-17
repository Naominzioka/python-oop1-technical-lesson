# Dog model goes here
class Dog:
    def __init__(self, name, breed, age, last_checkup= None):
        self.breed = breed
        self.name = name
        self.last_checkup = last_checkup
        self.age = age

    #instance method for checkup
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date

    #instance method
    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")
        
    def get_age(self):
        return self._age
    
    def set_age(self, value):
        #checking if the age is an integer..and if 0 is less than the value,,if so age is set
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age")
    age = property(get_age, set_age)
	

fido = Dog("Fido", "Golden Retriever", 3, "05/22/2022")
clifford = Dog("Clifford", "German Shepherd", 5)
print(fido.age)
print(clifford.last_checkup)
#updating dog to have checkup date
clifford.checkup("03/02/2024")
print(clifford.last_checkup)
fido.birthday_celebration()
#testing edge case using string and negative number as age
balto = Dog("Balto", "Husky", "hi")
steele = Dog("Steele", "Husky", -10)

