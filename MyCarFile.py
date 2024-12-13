


class Car:
    def __init__(self, __Make, __Year_Model):
        self.__Make =__Make
        self.__Year_Model = __Year_Model
        self.__Speed = 0

    def Accelerate(self):
        self.__Speed += 5
    def Brake(self):
        self.__Speed -= 5
    def Get_Speed(self):
        return self.__Speed

