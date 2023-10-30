# Class to demonstrate classes and objects
class Dog:
    # Class Variable
    animal = 'dog'

    # The constructor method
    def __init__(self, breed, color):
        # Instance Variables
        self.breed = breed
        self.color = color

# Create objects of the Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

# Display details of Rodger
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed:', Rodger.breed)
print('Color:', Rodger.color)

# Display details of Buzo
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed:', Buzo.breed)
print('Color:', Buzo.color)

# Access class variable using class name
print("\nAccessing class variable using class name")
print(Dog.animal)
