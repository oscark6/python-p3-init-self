#!/usr/bin/env python3

# Define the Dog class
class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
# Create instances of Dog with different combinations of arguments
dog1 = Dog("Fido")
dog2 = Dog("Buddy", "Golden Retriever")

# Print out the name and breed of each dog instance
print(f"Dog 1: {dog1.name}, {dog1.breed}")
print(f"Dog 2: {dog2.name}, {dog2.breed}")