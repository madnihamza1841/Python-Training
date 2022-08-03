"""
The file contains the Weather Record class.
The class can be used to store a single day weather record.
"""

class WeatherRecord:
    """
    The daily weather record class stores the daily weather data information.

    Attributes:
        date (string): The date for which the information is related.
        max_temp (int): The maximum temperature on that day.
        min_temp (int): The minimum temperature on that day.
        max_humidity (int): The maximum humidity on that day.
        mean_humidity (int): The mean humidity on that day.

    Methods:
        None  
    """
    def __init__(self, date, max_temp, min_temp, max_humidity, mean_humidity):
        """ 
        Initializes the class object and updates the public arguments.

        Arguments:
            date (string): The date for which the information is related.
            max_temp (int): The maximum temperature on that day.
            min_temp (int): The minimum temperature on that day.
            max_humidity (int): The maximum humidity on that day.
            mean_humidity (int): The mean humidity on that day.
        """
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity

