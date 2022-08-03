"""
The file contains all the report creation and calculation helpers
for weatherman report generations. 
"""

from operator import attrgetter

from weather_record import WeatherRecord 
from helpers import get_filepaths_for_argument, apply_month_mapping
from constants import REQ_FIELDS, BLUE, RED, WHITE 


def prepare_weather_records(filepaths,argument):
    """ 
    The function reads the weather files and creates weather records for each day separately.

    This function calls a helper function to get indexes of filepaths for the given argument.
    Incase of year, the number of weather records created is 365 and incase of month it is equal 
    to the number of days in that month. 

    Arguments:
        filepaths (list): A list of all filepaths for weather files.
        argument: The argument passed by the user such that it can be either
        the year or the "year/month".

    Returns:
        If no files present for the specified argument then returns None 
        Else weather_records (list): The list contains all the weather records of the year or month.
        Each individual weather record is a class object of type WeatherRecord containing 
        information about of each day.
    """
    
    filepath_indexes = get_filepaths_for_argument(filepaths, argument)
    if not filepath_indexes:
        return None

    weather_records = []

    for index in filepath_indexes:

        file = open(filepaths[index], "r")
        line = file.readline()[:-1].replace(", ", ",").split(",")
        
        column_names = []
        column_name_indexes = []
        for i in range(len(line)):
            if line[i] in REQ_FIELDS:
                column_names.append(line[i])
                column_name_indexes.append(i)
        
        for line in file:
            values = line[:-1].replace(", ", ",").split(",")

            date = values[column_name_indexes[column_names.index("PKT")]]
            metrics = [
                values[column_name_indexes[column_names.index("Max TemperatureC")]],
                values[column_name_indexes[column_names.index("Min TemperatureC")]],
                values[column_name_indexes[column_names.index("Max Humidity")]],
                values[column_name_indexes[column_names.index("Mean Humidity")]]
            ]
            
            max_temp = int(metrics[0]) if metrics[0] != "" else None  
            min_temp = int(metrics[1]) if metrics[1] != "" else None
            max_humidity = int(metrics[2]) if metrics[2] != "" else None         
            mean_humidity = int(metrics[3]) if metrics[3] != "" else None

            weather_records.append(WeatherRecord(date, max_temp, min_temp, max_humidity, mean_humidity))
        
    return weather_records

def get_max_temp_record(records):
    """ 
    The function finds the record with the highest max_temp value and returns the record.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        max_temp_record (WeatherRecord): The record with the highest max_temp
        value from the list of records provided.
    """
    return max(records, key=attrgetter('max_temp'))

def get_min_temp_record(records):
    """ 
    The function finds the record with the lowest min_temp value and returns the record.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        min_temp_record (WeatherRecord): The record with the lowest min_temp
        value from the list of records provided.
    """
    return min(records, key=attrgetter('min_temp'))

def get_max_humidity_record(records):
    """ 
    The function finds the record with the highest max_humidity value and returns the record.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        max_humidity_record (WeatherRecord): The record with the highest max_humidity
        value from the list of records provided.
    """
    return max(records, key=attrgetter('max_humidity'))

def get_average_max_temperature(records):
    """ 
    The function calculates the average of all max_temps for the weather records.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        average_max_temperature (int): The average of all the max_temperatures for
        the records.
    """
    max_temps = [record.max_temp for record in records if record.max_temp or record.max_temp == 0]
    average_max_temperature = sum(max_temps)//len(max_temps)
    
    return average_max_temperature

def get_average_min_temperature(records):
    """ 
    The function calculates the average of all min_temps for the weather records.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        average_min_temperature (int): The average of all the min_temperatures for
        the records.
    """
    min_temps = [record.min_temp for record in records if record.min_temp or record.min_temp == 0]
    average_min_temperature = sum(min_temps)//len(min_temps)

    return average_min_temperature

def get_average_mean_humidity(records):
    """ 
    The function calculates the average of all mean_humidity for the weather records.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        average_mean_humidity (int): The average of all the mean_humidity for
        the records.
    """
    mean_humidities = [record.mean_humidity for record in records if record.mean_humidity or record.mean_humidity == 0]
    average_mean_humidity =  sum(mean_humidities)//len(mean_humidities)

    return average_mean_humidity

def get_daily_temperatures(records):
    """ 
    The function gathers all the matrics required for plotting daily weather graph.

    Arguments:
        records (list): the list of weather record class objects. 

    Returns:
        dates (list): The list contains the dates of month in string format.
        max_readings (list): The list contains the max temperatures of month in integer format.
        min_readings (list): The list contains the min temperatures of month in integer format.
    """    
    dates = [record.date for record in records 
        if record.date and (record.max_temp or record.max_temp == 0) 
        and (record.min_temp or record.min_temp ==0)]
    max_temps = [record.max_temp for record in records if record.max_temp or record.max_temp == 0]
    min_temps = [record.min_temp for record in records if record.min_temp or record.min_temp == 0]

    return dates, max_temps, min_temps