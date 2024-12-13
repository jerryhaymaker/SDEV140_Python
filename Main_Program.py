from MyCarFile import Car

MyCar = Car("Ford Fusion", "2017 Sport")

for AccelerationSpeed in range(5):
    MyCar.Accelerate()
    CurrentSpeed = MyCar.Get_Speed()
    print("Your speed is increasing by: " + str(CurrentSpeed))

for DecelerationSpeed in range(5):
    MyCar.Brake()
    CurrentSpeed = MyCar.Get_Speed()
    print("Your speed is decreasing by: " + str(CurrentSpeed))
