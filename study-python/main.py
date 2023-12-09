class Person(object):
  def __init__(self, name):
    self.name = name
    print("First")
    print("{}".format(self.name))
    self.run(2)

  def run(self, num):
    print("run\n" * num)

  def say_something(self):
    print("hello")

  def __del__(self):
    print("good bye")

# person = Person()
person = Person("AA")
person.say_something()
del person
print("######")

# def person(name):
#   if name == "a":
#     print("a")

