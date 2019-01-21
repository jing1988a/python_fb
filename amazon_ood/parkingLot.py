from abc import abstractmethod  , ABCMeta
from enum import Enum
class SpotType(Enum):
    SMALL=0
    MEDIUM=1
    LARGE=2


class Vehicle(metaclass=ABCMeta):
    def __init__(self , vihecleType , spotType , spotNeed , plate):
        self.vihecleType=vihecleType
        self.spotType=spotType
        self.spotNeed=spotNeed
        self.plate=plate
        self.spotTaken=[]


    def leaveSpot(self):
        pass
    def parkAtSpot(self , spot):
        pass
    def getParkingSpot(self):
        pass
    @abstractmethod
    def canFitSpot(self , spot):
        pass
class Moto(Vehicle):
    def __init__(self , plate):
        super.__init__('Moto' , SpotType.SMALL , 1 , plate)

    def canFitSpot(self , spot):
        return True

class Car(Vehicle):
    def __init__(self , plate):
        super.__init__('Car' , SpotType.MEDIUM , 1 , plate)

    def canFitSpot(self , spot):
        if spot.type==SpotType.SMALL:
            return False
        else:
            return True
class Bus(Vehicle):
    def __init__(self , plate):
        super.__init__('Car' , SpotType.MEDIUM , 5 , plate)

    def canFitSpot(self , spot):
        if spot.type==SpotType.LARGE:
            return True
        else:
            return False




class ParkingLot:
    __instance=None
    def __init__(self , levelNumber , levels ):
        if ParkingLot.instance:
            raise Exception('this is singleton')
        else:
            self.levelNumber=levelNumber
            self.levels=levels
            ParkingLot.__instance=self
    def getInstance(self):
        if not ParkingLot.__instance:
            ParkingLot()
        return ParkingLot.__instance

    def park(self , vehicle):
        #do parking

    def dePark(self , vehicle):
        #clear vehicle

    def totalAvailableSpace(self):
        #get current available space

    def canPark(self , vehicle):


class Level:
    def __init__(self ,  spots):
        self.totalSpots=len(spots)
        self.spots=spots
        self.occupiedSpot=[]

    def park(self, vehicle):

    # do parking

    def dePark(self, vehicle):

    # clear vehicle

    def totalAvailableSpace(self):

    # get current available space

    def canPark(self, vehicle):

class Spot:
    def __init__(self , spotType , id  ):
        self.type=spotType
        self.id=id
        self.parkedVehicle=None

    def isOccupied(self):
        return False if self.parkedVehicle else  True

    def fitVehicle(self, vehicle):
        if self.isOccupied():
            return False
        return vehicle.canFitSpot(self)
    def park(self, vehicle):

    # do parking

    def dePark(self, vehicle):

# clear vehicle
