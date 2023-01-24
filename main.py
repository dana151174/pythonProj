from car import Car
from CarProject.utils import *

if __name__ == '__main__':

    try:
        x = Car()
        x.gear_level=6
        x.gear_level_up()


    except OverflowError as o:
        print(o)
    except ValueError as v:
        print(v)
    except Exception as e:
        print(e)
