class Car(object):
  def run(self):
    print("run")

class TeslaCar(Car):
  def auto_run(self):
    print("auto run")

class ToyotaCar(TeslaCar):
  pass

car = Car()
car.run()
toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

print("aaa")

toyota_car.auto_run()


