class Person(object):
  def __init__(self, age=1):
    self.age = age
  def drive(self):
    if self.age >= 18:
      print("ok")
    else:
      raise Exception("no drive")

class Baby(Person):
  def __init__(self, age=1):
    if age < 18:
      super().__init__(age)
    else:
      raise ValueError

class Adult(Person):
  def __init__(self, age=18):
    if age >= 18:
      super().__init__(age)
    else:
      raise ValueError

baby = Baby()
adult = Adult()



class Car(object):
  def __init__(self, model=None):
    self.model = model
  def run(self):
    print("run")

  def ride(self, person):
    person.drive()

car = Car()
car.ride(adult)

class ToyotaCar(Car):
  pass

class TeslaCar(Car):
  def run(self):
    print("run fast")
  def auto_run(self):
    print("auto run")


car = Car()
car.run()
toyota_car = ToyotaCar("ssss")
print(toyota_car.model)
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()




