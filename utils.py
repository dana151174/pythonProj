import datetime as dt

class Utils:

    @staticmethod
    def check_positive_integer(distance):
        """
        Method checks if the given value is a positive integer value
        :param distance: Value to check
        :return True if the given value is a positive integer False otherwise
        """
        return isinstance(distance, int) and distance > 0

    @staticmethod
    def write_to_log(str):
        """
        Method gets a string and writs it to the LOG file
        :param str: Str to write to the LOG file
        :return: None
        """
        f = open('LogFile.txt', 'a')
        f.write(f"\n{str}, {dt.datetime.now()}")
        f.close()

