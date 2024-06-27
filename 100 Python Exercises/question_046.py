# Define a class named American and its subclass NewYorker.

class American:
    @staticmethod
    def print_nationality():
        print('American')
        
class NewYorker(American):
    pass

american = American()
american.print_nationality()
new_yorker = NewYorker()
new_yorker.print_nationality()

print(type(american))
print(type(new_yorker))
