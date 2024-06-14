# Define a class, which have a class parameter and have a same instance
# parameter

class MyClass:
    def __init__(self, parameter=1):
        self.value = parameter
        
instance_1 = MyClass()
instance_2 = MyClass(2)

print(f'instance_1 value: {instance_1.value}')
print(f'instance_2 value: {instance_2.value}')
