class Car(object):
  def __init__(self, model=None):
    self.model = model
  def run(self):
    print("run")

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




