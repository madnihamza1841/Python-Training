"""
This is the main file for the WeatherMan Reporting. 
The main file only calls the functions for parsing arguments 
and report generation.
"""

import glob   
import sys

from helpers import parse_arguments  
from report_creators import prepare_weather_records
from report_generators import (
    yearly_weather_report_generator, 
    monthly_weather_report_generator, 
    weather_graph_generator
)

def main():
    """
    This is the main function for the weather reporting

    The main functions calls the following functions; 
    parse_arguments for command line argument parsing and validation 
    report_generators for creating the monthly or yearly report for the arguments passed 
    graph_generator for plotting the daily weather graph

    Arguments:
        None

    Returns:
        None
    """
    arguments = parse_arguments()

    filepaths = glob.glob(arguments.directory + "/*.txt")

    if arguments.yearly_report:
        weather_records = prepare_weather_records(filepaths,arguments.yearly_report)
        yearly_weather_report_generator(arguments.yearly_report, weather_records)
    if arguments.monthly_report:
        weather_records = prepare_weather_records(filepaths,arguments.monthly_report)
        monthly_weather_report_generator(arguments.monthly_report, weather_records)
    if arguments.monthly_graph:
        weather_records = prepare_weather_records(filepaths,arguments.monthly_graph)
        weather_graph_generator(arguments.monthly_graph,weather_records)

if __name__ == "__main__":
    main()
