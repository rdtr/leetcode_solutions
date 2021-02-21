class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append(Car(p, s))
        
        if not cars:
            return 0
        
        cars.sort()
        
        fleet = len(cars)
        prevCar = cars[-1]
        prevCarDur = (target - prevCar.pos) / prevCar.speed
        for i in range(len(cars) - 2, -1, -1):
            curCar = cars[i]
            curCarDur = (target - curCar.pos) / curCar.speed

            if curCarDur <= prevCarDur:

                fleet -= 1
                continue
            prevCar = curCar
            prevCarDur = curCarDur

        return fleet
        

class Car:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
        
    def __lt__(self, other):
        if self.pos < other.pos:
            return True
        elif self.pos > other.pos:
            return False
        return self.speed > other.speed