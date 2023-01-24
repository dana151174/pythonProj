import pytest
from pytest import fixture, mark
from CarProject.car import Car
from CarProject.utils import Utils


@pytest.fixture
def car():
    """
    :return:
    """
    return Car()

def test_something(car):
    """
    Method tests if the car has 50 liter fuel
    :param car:
    :return:
    """
    try:
        assert car.fuel == 50
        Utils.write_to_log("PASS: tPASS: new car has 50 liters fuel")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: {a}")

def test_start(car):
    """
    Method tests start()
    :param car:
    :return:
    """
    try:
        assert car.start() == True
        Utils.write_to_log("PASS: with gear level 0 the car starts")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: with gear level 0 the car should start {a}")


def test_start_failure(car):
    """
    Method tests start() failure and the exception it throws
    gear level is set to 5
    :param car:
    :return:
    """
    car.gear_level = 5
    try:
        with pytest.raises(Exception):
            car.start()
        Utils.write_to_log("PASS: Exception was raised when the car starts in gear level 5")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: Exception was not raised when the car starts in gear level 5 - {a}")

def test_stop(car):
    """
    Method tests stop() checks that after the car stops the gear level is 0
    :param car:
    :return:
    """
    try:
        car.stop()
        assert car.gear_level == 0
        Utils.write_to_log("PASS: after stopping the gear level is 0")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: the gear level should be 0 after stopping - {a}")

def test_stop2(car):
    """
    Method tests stop() checks that after the car stops the speed is 0
    :param car:
    :return:
    """
    try:
        car.stop()
        assert car.get_speed() == 0
        Utils.write_to_log("PASS: after stopping the speed is 0")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: the speed should be 0 after stopping - {a}")


def test_has_enough_fuel(car):
    """
    Method checks if the car has enough fuel to complete the given distance
    :param car:
    :return:
    """
    try:
        assert car.has_enough_fuel(500) == True
        Utils.write_to_log("PASS: the car can drive 500 kl with 50 l fuel")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: the car should be able to complete 500 kl with 50 l fuel - {a}")

def test_has_enough_fuel2(car):
    """
    Method checks if the car has enough fuel to complete the given distance (1000)
    :param car:
    :return:
    """
    try:
        assert car.has_enough_fuel(500) == False
        Utils.write_to_log("PASS: the car can drive 500 kl with 50 l fuel")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: the car should be able to complete 500 kl with 50 l fuel - {a}")

def test_calc_max_distance(car):
    """
    Method checks if the max distance that the car can drive with 50 l fuel is 1000
    :param car:
    :return:
    """
    try:
        assert car.calc_max_distance() == 1000
        Utils.write_to_log("PASS: with 50 l fuel max distance is 1000 km")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: the max distance with 50 l fuel, should be 1000 - {a}")

def test_calc_max_distance2(car):
    """
    Method checks that the max distance that the car can drive with 50 l fuel is not 1200
    :param car:
    :return:
    """
    try:
        assert car.calc_max_distance() == 1200
        Utils.write_to_log("PASS: with 50 l max distance is 1000 km")
    except AssertionError as a:
        Utils.write_to_log(f"FAIL: the max distance should be 1000 - {a}")


