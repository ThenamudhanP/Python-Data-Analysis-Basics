
# class defines the Blueprint.
class Dog:
    # __init__ is a special function that runs automatically when you create a new object.
    def __init__(self, name, breed):
        self.name = name    # These are attributes
        self.breed = breed  # These are attributes

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Creating an Object from the Blueprint.
# Named arguments: We explicitly tell Python which parameter is which (name="Jerry").
jerry = Dog(name="Jerry", breed="Labrador")

# Accessing an attribute
print(f"My dog is a {jerry.breed}")

# 2. CLASS METHODS
# ==========================================
class DataValidator:
    def __init__(self):
        self.errors = []

    # Methods are functions inside a class.
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True

    def get_errors(self):
        return self.errors

validator = DataValidator()

validator.validate_email(email="bad-email")
validator.validate_age(age=200)
print(f"Validation Errors: {validator.get_errors()}")



# 3. INHERITANCE (PARENT AND CHILD CLASSES)
# ==========================================
# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
# By putting (Animal) in the parentheses, Dog inherits EVERYTHING from Animal.
class InheritedDog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

# Positional argument: We just pass "Buddy" without writing name="Buddy".
# Python knows it goes to the first parameter because of its position.
my_dog = InheritedDog("Buddy")

# Or using a named argument
my_dog2 = InheritedDog(name="Max")

print("\n--- Inheritance Test ---")
# The dog can do Animal things (Inherited methods)
print(my_dog.eat())   # Output: Buddy is eating
print(my_dog.sleep()) # Output: Buddy is sleeping

# The dog can ALSO do specific Dog things
print(my_dog.bark())  # Output: Buddy says woof!