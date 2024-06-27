# Define a class Person and its two child classes: Male and Female. All classes
# have a method "getGender" which can print "Male" for Male class and "Female"
# for Female class.

class Person:
    def get_gender(self):
        print(self)
        
class Male(Person):
    def __str__(self):
        return 'Male'

class Female(Person):
    def __str__(self):
        return 'Female'
    
john = Male()
mary = Female()
john.get_gender()
mary.get_gender()
