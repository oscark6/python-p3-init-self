#!/usr/bin/env python3

      # Define the Person class
class Person:
    def __init__(self, name):
        self.name = name

# Create instances of Person with different names
person1 = Person("Daniel")
person2 = Person("Bob")

# Print out the name of each person instance
print(f"Person 1: {person1.name}")
print(f"Person 2: {person2.name}")