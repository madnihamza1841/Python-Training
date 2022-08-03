"""
The file contains all the report generators and the display functions 
used for the report generation
"""

from helpers import apply_month_mapping
from constants import BLUE, RED, WHITE
from report_creators import (
    get_max_temp_record, 
    get_min_temp_record, 
    get_max_humidity_record, 
    get_average_max_temperature, 
    get_average_min_temperature, 
    get_average_mean_humidity, 
    get_daily_temperatures
)

def display_yearly_report(year, metrics):
    """
    This function is used for displaying yearly report on the command line.

    Arguments:
        year (str): The year for which the report is generated, passed
        through command line by the user.
        metrics (dict): A dictionary containing all the metrics to be
        displayed with keys as the metric name and values as the metric values.

    Returns:
        None
    """
    print("")
    if not metrics:
        print("The files for the specified year: ", year,  " are not present.")
    else:
        print ("Printing report for: ", year)
        print ("Highest: " + str(metrics["max_temp"]) + "C on " 
            + str(apply_month_mapping(int(metrics["max_temp_date"].split("-")[1]))), 
            metrics["max_temp_date"].split("-")[2] )
        print ("Lowest : " + str(metrics["min_temp"]) + "C on " 
            + str(apply_month_mapping(int(metrics["min_temp_date"].split("-")[1]))), 
            metrics["min_temp_date"].split("-")[2] )
        print ("Humidity: " + str(metrics["max_humidity"]) + "% on " 
            + str(apply_month_mapping(int(metrics["max_humidity_date"].split("-")[1]))), 
            metrics["max_humidity_date"].split("-")[2] )

def display_monthly_report(month, metrics):
    """
    This function is used for displaying monthly report on the command line.

    Arguments:
        month (str): The "year/month" for which the report is generated, passed
        through command line by the user.
        metrics (dict): A dictionary containing all the metrics to be
        displayed with keys as the metric name and values as the metric values.

    Returns:
        None
    """
    print("")
    if not metrics:
        print("The files for the specified month: ", month,  " are not present.")
    else:
        print ("Printing report for: ", month)
        print ("Highest Average: ", metrics["avg_max_temp"], "C")
        print ("Lowest Average: ", metrics["avg_min_temp"], "C") 
        print("Average Mean Humidity: ", metrics["avg_mean_humidity"], "%")

def plot_weather_graph(month, dates, max_readings, min_readings):
    """
    The function is used to plot a daily weather graph using print statements, "+"  and "-"signs.

    For each day of month, the minimum temperature is plotted in blue signs and 
    the maximum temperature is plotted in red signs. 
    Given the temperature (min or max) for a given day is below 0, then the signs
    used for that part is "-" and for temperatures above 0, "+" signs are used.
    Format of each line in graph;
    "Day_No [Blue signs equal to min temp][Red Signs equal to max temp] min_temp max_temp"
    
    Arguments:
        month (str): The "year/month" for which the report is generated, passed
        through command line by the user.
        dates (list): The list contains the dates of month in string format.
        max_readings (list): The list contains the max temperatures of month in integer format.
        min_readings (list): The list contains the min temperatures of month in integer format.

    Returns:
        None
    """
    print ("Printing report for: ", month)

    l = len(dates)
    for i in range(l):
        date = dates[i].split("-")[2]
        if len(date) !=2:
            date = "0" + date 

        max_temp = max_readings[i]
        min_temp = min_readings[i]

        plot_max = ""
        if max_temp > 0:
            plot_max = plot_max + abs(max_temp)*"+"
        else:
            plot_max = plot_max + abs(max_temp)*"-"

        plot_min = ""
        if min_temp > 0:
            plot_min = plot_min + abs(min_temp)*"+"
        else:
            plot_min = plot_min + abs(min_temp)*"-"


        print(date, BLUE + plot_min +  RED + plot_max + 
                WHITE,  str(min_temp) + "C " + str(max_temp) + "C", WHITE)

def yearly_weather_report_generator(year, weather_records):
    """ 
    The function is used to generate the yearly weather report.

    This function calculates all the metrics using helper functions and
    then passes them on to the display function of yearly report in form of
    a dictionary. 

    Arguments:
        year (str): The year for which the report is generated, passed through 
        command line by the user.
        weather_records (list): The list contains all the weather records of the year.
        Each individual weather record is a class object of type WeatherRecord containing 
        information about each date.

    Returns:
        None
    """    
    if not weather_records:
        display_yearly_report(year , None)
        return None

    max_temp_record =  get_max_temp_record(weather_records)
    min_temp_record =  get_min_temp_record(weather_records)
    max_humidity_record = get_max_humidity_record(weather_records)       
    
    metrics =  {
        "max_temp": max_temp_record.max_temp, 
        "max_temp_date": max_temp_record.date, 
        "min_temp": min_temp_record.min_temp, 
        "min_temp_date": min_temp_record.date, 
        "max_humidity": max_humidity_record.max_humidity, 
        "max_humidity_date": max_humidity_record.date
    }

    display_yearly_report(year , metrics) 

def monthly_weather_report_generator(month,weather_records):
    """ 
    The function is used to generate the monthly weather report.

    This function calculates all the metrics using helper functions and
    then passes them on to the display function of monthly report in form of
    a dictionary. 

    Arguments:
        month (str): The year for which the report is generated, passed through 
        command line by the user.
        weather_records (list): The list contains all the weather records of the month.
        Each individual weather record is a class object of type WeatherRecord containing 
        information about each date.

    Returns:
        None
    """ 
    if not weather_records:
        display_monthly_report(month , None)
        return None

    avg_max_temp = get_average_max_temperature(weather_records)
    avg_min_temp = get_average_min_temperature(weather_records)
    avg_mean_humidity = get_average_mean_humidity(weather_records)

    metrics =  {
        "avg_max_temp": avg_max_temp, 
        "avg_min_temp": avg_min_temp, 
        "avg_mean_humidity": avg_mean_humidity
    }

    display_monthly_report(month, metrics)

def weather_graph_generator(month, weather_records):
    """ 
    The function is used for generating the daily weather graph.

    This function gathers all the metrics using a helper function and
    then passes them on to the plotting function of daily weather graph in 
    form of lists. 

    Arguments:
        month (str): The year for which the report is generated, passed through 
        command line by the user.
        weather_records (list): The list contains all the weather records of the month.
        Each individual weather record is a class object of type WeatherRecord containing 
        information about each date.

    Returns:
        None
    """
    if not weather_records:
        display_monthly_report(month , None)
        return None
        
    dates, max_temp, min_temp = get_daily_temperatures(weather_records)
    plot_weather_graph(month, dates, max_temp, min_temp)
