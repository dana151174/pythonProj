import unittest
from CarProject.car import Car
from CarProject.utils import Utils

class TestCar(unittest.TestCase):

    def setUp(self):
        """
        Method set up the car for testing
        :return:
        """
        self.the_car = Car()

    def test_something(self):
        """
        Method tests if the car has 50 liter fuel
        :return:
        """
        try:
            self.assertEqual(self.the_car.fuel, 50)
            Utils.write_to_log("PASS: new car has 50 liters fuel")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: {a}")

    def test_get_speed(self):
        """
        Method tests get_speed()
        :return:
        """
        self.the_car.gear_level = 3
        try:
            self.assertEqual(self.the_car.get_speed(), 90)
            Utils.write_to_log("PASS: with gear level 3 the speed is 90")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: with gear_level 3 the speed should be 90 {a}")

    def test_start(self):
        """
        Method tests start()
        :return:
        """
        try:
            self.assertIs(self.the_car.start(), True)
            Utils.write_to_log("PASS: with gear level 0 the car starts")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: with gear level 0 the car should start {a}")

    def test_start_failure(self):
        """
        Method tests start() failure and the exception it throws
        gear level is set to 5
        :return:
        """
        self.the_car.gear_level = 5
        try:
            with self.assertRaises(Exception):
                self.the_car.start()
            Utils.write_to_log("PASS: Exception was raised when the car starts in gear level 5")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: Exception was not raised when the car starts in gear level 5 - {a}")

    def test_drive_gear_level(self):
        """
        Method tests drive() with distance 1000 and checks that the gear level is 1
        :return:
        """
        try:
            self.the_car.drive(1000)
            self.assertEqual(self.the_car.gear_level, 1)
            Utils.write_to_log("PASS: when the car drives the gear level is 1")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: when the car drives the gear level should be 1 - {a}")

    def test_drive_fuel(self):
        """
        Method tests drive() with distance 1000 that the fuel after driving is 0
        :return:
        """
        try:
            self.the_car.drive(1000)
            self.assertEqual(self.the_car.fuel, 0)
            Utils.write_to_log("PASS: after the car drives 1000 km the fuel is 0")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: when the car drives 1000 km the fuel should be 0 - {a}")

    def test_drive_failure(self):
        """
        Method tests that drive() failure raises ValueError if can't drive anymore
        :return:
        """
        self.the_car.drive(1000)
        try:
            with self.assertRaises(Exception):
                self.the_car.drive(1)
            Utils.write_to_log("PASS: Exception was thrown after trying to drive without fuel")
        except AssertionError as a:
            Utils.write_to_log(f"FAIL: Exception was not thrown after trying to drive without fuel - {a}")

if __name__ == '__main__':
    unittest.main()
