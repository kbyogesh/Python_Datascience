#single inheritance
class Animal:
  def speak(self):
    print("animal speak")
class Dog(Animal):
  def bark(self):
    print("Dog barks")
dog=Dog()
dog.speak()
dog.bark()
