#hierrarchical inheritance:
class Animal:
  def speack(self):
    print("Animal Speak")
class Dog(Animal):
  def bark(self):
    print("Dog barks")
class Cat(Animal):
  def meow(self):
    print("cat mews")
dog=Dog()
cat=Cat()
dog.speack()
cat.speack()
