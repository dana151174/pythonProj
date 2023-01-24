from dotenv import load_dotenv
import os
from CarProject.utils import *


class Car:
    load_dotenv()

    def __init__(self):
        self.fuel = int(os.getenv('FUEL'))
        self.fuel_con = int(os.getenv('FUEL_CON'))
        self.money = int(os.getenv('MONEY'))
        self.gear = int(os.getenv('GEAR'))
        self.gear_level = int(os.getenv('GEAR_LEVEL'))
        self.fuel_price = int(os.getenv('FUEL_PRICE'))

    def get_speed(self):
        """
        Method calculate the car's speed by multiplying the gear by the gear level
        :return: car's speed
        """
        return self.gear * self.gear_level

    def start(self):
        """
        Method starts the car
        if the car already in drive mode it will raise Exception
        :return: True if the car in stop mode and can be started otherwise raises Exception
        """
        if self.gear_level != 0:
            raise Exception(os.getenv("EXCEPTION"))
        else:
            return True

    def drive(self, distance):
        """
        Method gets distance and starts driving if has enough fuel for the given distance
        and not in drive mode already
        :param: distance: the distance for the car
        :raises: ValueError or Exception
        :return: None
        """
        if not Utils.check_positive_integer(distance):
            raise ValueError(os.getenv('VALUE_ERROR1'))

        try:
            self.start()
        except Exception as a:
            raise Exception(a)
        try:
            self.has_enough_fuel(distance)
        except ValueError as v:
            raise ValueError(v)

        self.fuel = self.fuel - distance / self.fuel_con
        self.gear_level = 1

    def stop(self):
        """
        Method stops the car by making the gear level 0
        if the car already in stop mode it will raise Exception
        :return: None
        """
        if self.gear == 0:
            raise Exception(os.getenv("EXCEPTION1"))

        self.gear_level = 0

    def has_enough_fuel(self, distance):
        """
        Method checks if the car has enough fuel do drive the given distance
        :param distance: distance per fuel amount
        :return:True if the car has enough fuel to drive the given distance otherwise raises ValueError
        """
        if not Utils.check_positive_integer(distance):
            raise ValueError(os.getenv('VALUE_ERROR1'))

        if self.fuel * self.fuel_con < distance:
            raise ValueError(os.getenv("VALUE_ERROR2"))

        return True

    def buy_fuel(self, fuel_amount):
        """
        Method gets amount of fuel and calculates if you have enough money to buy it
        if you have it updates the car's fuel and the money accordingly if not it raises Exception
        :param fuel_amount:
        :return: None
        """
        if self.money < fuel_amount * self.fuel_price:
            raise Exception(os.getenv("EXCEPTION3"))

        self.money -= fuel_amount * self.fuel_price
        self.fuel += fuel_amount

    def calc_max_distance(self):
        """
        Method calculate the max distance the car can drive with the amount of fuel left
        :return: the max distance the car can drive with the amount of fuel left
        """
        return self.fuel * self.fuel_con

    def gear_level_up(self):
        """
        Method increases the gear level. if the gear level is 0 or 6 it raises OverflowError
        :raises: OverflowError if the gear level is 0 or 6
        :return:None
        """
        if self.gear_level == 0 or self.gear_level >= int(os.getenv('MAX_GEAR_LEVEL')):
            raise OverflowError(os.getenv("OVERFLOW_ERROR1").format(os.getenv('MAX_GEAR_LEVEL')))

        self.gear_level += 1

    def gear_level_down(self):
        """
        Method lowers the gear level. if the gear level is less than 1 it raises OverflowError
        :return: None
        """
        if self.gear_level <= 1:
            raise OverflowError(os.getenv("OVERFLOW_ERROR2"))

        self.gear_level -= 1
