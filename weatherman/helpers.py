"""
The file contains all the generic helpers used for WeatherMan Reporting.
"""

import glob
import argparse
import pathlib
import os
from datetime import datetime

from constants import REQ_FIELDS, BLUE, RED, WHITE

def get_filepaths_for_argument(filepaths, argument):
    """
    The function is used to check the presence of the file(s) in the dictionary
    for which the user has requested the report.

    Arguments:
        filepaths (list): A list of all filepaths for weather files.
        argument: The argument passed by the user such that it can be either
        the year or the "year/month".
         
    Returns:
        filepath_indexes (list): If the filepath matching the argument found, then index(es)
        of the filepath(s) returned.
        None: If nothing found
    """
    filepath_indexes = []
    if len(argument.split("/")) == 2:
        year = argument.split("/")[0]
        month = int(argument.split("/")[1])
        for i in range(len(filepaths)):
            if filepaths[i].split("_")[2] == year and apply_month_mapping(filepaths[i].split("_")[3].split(".txt")[0]) == month:
                filepath_indexes.append(i)
    
    elif len(argument.split("/")) == 1:
        year = argument
        for i in range(len(filepaths)):
            if filepaths[i].split("_")[2] == year:
                filepath_indexes.append(i)
    if len(filepath_indexes) == 0:
        return None
    else:
        return filepath_indexes

def apply_month_mapping(month):
    """
    The function returns the mapping for the months.

    Arguments:
        month (int): An integer from 1 to 12 denoting the month of year.
        month (str): The short month name denoting the month of year.
         
    Returns:
        If month is an integer from 1-12 then returns the short month name
        Else if month is a short month name then returns the integer (1-12) corresponding
        to the month name.
    """
    if isinstance(month, str):
        return int(datetime.strptime(month, '%b').strftime("%m"))
    elif isinstance(month, int):
        return datetime.strptime(str(month), '%m').strftime("%b")

def validate_year_format(year):
    """
    This function validates the format of the year argument passed through command line.

    The function is being used in the argument parser and raises an exception in case
    of incorrect format of year.

    Arguments:
        year (str): The year argument passed through command line by user.
         
    Returns:
        If correct format then; datetime object of year validated and then
        converted into string
        Else; raises an exception stating invalid format.
    """
    try:
        return str(datetime.strptime(year, "%Y").year)
    except:
        raise argparse.ArgumentTypeError(f"Given Year:( {year} ) not valid")

def validate_month_format(month):
    """
    This function validates the format of the month argument passed through command line.

    The function is being used in the argument parser and raises an exception in case
    of incorrect format of month.

    Arguments:
        month (str): The month argument passed through command line by user.
         
    Returns:
        If correct format then: datetime object of year/month validated and then
        converted into string
        Else raises an exception stating invalid format.
    """
    try:
        return str(datetime.strptime(month, '%Y/%m').strftime("%Y/%m"))
    except:
        raise argparse.ArgumentTypeError(f"Given Month:( {month} ) not valid")

def validate_path_format(path):
    """
    The function validates the format of the directory argument passed through command line.

    The function is being used in the argument parser and raises an exception in case
    of incorrect format of path.

    Arguments:
        path (str): The directory argument passed through the command line by user.

    Returns:
        If directory can be opened then it returns the path string as it is
        Else raises an exception stating invalid format.
    """
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"Directory: {path} is not a valid path")

def parse_arguments():
    """
    The function creates an argument parser object.

    The function reads the cmd line arguments, validates them, and raises exceptions
    if necessary. If all arguments are valid then it returns them in form dict.

    Arguments:
        None
         
    Returns:
        arguments (Argumentparser class obj): Contains all the command line arguments stored
        within public parameters.
    """
    parser = argparse.ArgumentParser(description = "Process command line arguments.")
    parser.add_argument("directory", type = validate_path_format, help= "filepaths for weatherfiles")
    parser.add_argument("-e","--yearly_report", required = False, type = validate_year_format,help= "flag for yearly stats report")
    parser.add_argument("-a","--monthly_report", required = False, type = validate_month_format ,help= "flag for monthly stats report")
    parser.add_argument("-c","--monthly_graph", required = False, type = validate_month_format ,help= "flag for monthly stats graph")
    arguments = parser.parse_args()
    return arguments
