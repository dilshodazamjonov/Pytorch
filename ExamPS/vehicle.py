class Vehicle:
    def __init__(self, id: str, maxSpeed: int, increaseAmount: int):
        self.id = id
        self.maxSpeed = maxSpeed
        self.increaseAmount = increaseAmount
        self.current_speed = 0
        self.horizontalPosition = 0
    
    def GetCurrentSpeed(self):
        return self.current_speed
    
    def GetIncreaseAmount(self):
        return self.increaseAmount
    
    def GetHorizontalPosition(self):
        return self.horizontalPosition

    def GetMaxSpeed(self):
        return self.maxSpeed

    def SetCurrentSpeed(self, new_speed):
        self.current_speed = new_speed
        return {self.current_speed}

    def SetHorizontalPosition(self, new_hp):
        self.horizontalPosition = new_hp
        return self.horizontalPosition

    def IncreaseSpeed(self):
        self.current_speed += self.increaseAmount

        if self.current_speed > self.maxSpeed:
            self.current_speed = self.maxSpeed
        
        self.horizontalPosition += self.current_speed
        return {self.increaseAmount}

class Helicopter(Vehicle):
    def __init__(self, id: str, maxSpeed: int, increaseAmount: int, verticalChange: int, maxHeight: int):
        super().__init__(id, maxSpeed, increaseAmount)
        self.__verticalPosition = 0
        self.__verticalChange = verticalChange
        self.__maxHeight = maxHeight

    def GetVerticalPosition(self):
        return self.__verticalPosition

    def IncreaseSpeed(self):
        self.current_speed += self.increaseAmount
        if self.current_speed > self.maxSpeed:
            self.current_speed = self.maxSpeed

        self.horizontalPosition += self.current_speed

        self.__verticalPosition += self.__verticalChange
        if self.__verticalPosition > self.__maxHeight:
            self.__verticalPosition = self.__maxHeight

        print(f"Current speed: {self.current_speed}, Horizontal position: {self.horizontalPosition}, Vertical position: {self.__verticalPosition}")


def PrintVehicleInfo(vehicle):
    print(f"Vehicle ID: {vehicle.id}")
    print(f"Current Speed: {vehicle.GetCurrentSpeed()}")
    print(f"Horizontal Position: {vehicle.GetHorizontalPosition()}")
    if isinstance(vehicle, Helicopter):
        print(f"Vertical Position: {vehicle.GetVerticalPosition()}")



car = Vehicle("Tiger", 100, 20)

heli = Helicopter("Lion", 350, 40, 3, 100)

car.IncreaseSpeed()
car.IncreaseSpeed()

PrintVehicleInfo(car)

heli.IncreaseSpeed()
heli.IncreaseSpeed()
PrintVehicleInfo(heli)
