"""
The file contains all helper functions for typing tester feature.
"""

import json
import time
import sys

import requests
from getch import getch, getche

from constants import (
	AVG_HOVER_TIME, 
	AVG_KEYSTROKE_TIME, 
	ENTER_KEY, 
	DELETE_KEY
)

def display_helper(flag, argument):
	"""
	The function is a generic display helper that hanles all cases of print statements.

	Arguments:
		flag (str): A flag that denotes which print statement to display.
		argument (*): The value that is required to be printed.

	Returns:
		None
	"""
	if flag == "word":
		print (f"\n Word", ": ", argument)
		print (f"No. of letters: {len(argument)} \n")
	elif flag == "user_typed":
		print(f" User Typed: ", end="")
		sys.stdout.flush()
	elif flag == "delete_key":
		print((len(argument)+1)*"\b" + argument + " " + "\b",end = "")
		sys.stdout.flush()
	elif flag == "enter_key":
		print((len(argument)-1)*"\b" + argument, end = "")
		sys.stdout.flush()
	elif flag == "time_taken":
		print (f"\n Time Taken by user: {argument} \n")
	else:
		print (f"{flag}: {argument} \n")

def track_user_input():
	"""
	The function is used to track the user input and backspaces used.

	This function takes user input character by character and keeps track of
	whenever the user uses delete button for backspace. Also keeps track of the
	enter key as pressing the key submits the user's answer and records time at
	the time of submission of input.

	Arguments:
		None

	Returns:
		user_typing_data (dict): A dictionary containing the following keys and values:
			user_spelling (str): The spelling of the word typed by the user.
			backspaces_count (int): Number of times user has used backspace before submitting.
			submit_time (float): The system time in seconds when the answer was submitted. 
	"""
	user_spelling = ""
	backspaces_count = 0

	display_helper("user_typed", None)
	char = getch()
	while ord(char) != ENTER_KEY:  
	    if ord(char) == DELETE_KEY:
	        backspaces_count +=1
	        user_spelling = user_spelling[:-1]
	        display_helper("delete_key", user_spelling)
	    else:
	        user_spelling = user_spelling + char
	        display_helper("enter_key", user_spelling)
	    char = getch()	
	
	submit_time = time.time()
	
	return {
		"user_spelling" : user_spelling,
		"backspaces_count": backspaces_count,
		"submit_time": submit_time,
	}

def get_accuracy_score(actual_spelling, user_spelling, backstrokes_count):
	"""
	The function calculates the accuracy score for the spelling input by the user.

	This function compares the actual spelling of word with the spelling submitted by
	the user, word by word.  For each correct word, the user gets a positive score and
	for every mismatch, a negative score is added to total sum equal to the weightage
	of each character. For each backspace, score is deducted equal to number of backspaces
	* weightage of each character.

	Arguments:
		actual_spelling (str): Actual correct spelling of the word.
		user_spelling (int): The spelling submitted by the user.
		backstrokes_count (int): The count for the backspaces used by user.

	Returns:
		accuracy_score (int): A value within 0 to 100, both inclusive and rounded to 2 decimal 
		places. It denotes the accuracy of the spelling with negative points for mismatches and 
		usage of backstrokes.
	"""
	accuracy_score = 0
	score_per_letter = 100/ len(actual_spelling)

	for i in range(min(len(actual_spelling), len(user_spelling))):
		if actual_spelling[i] == user_spelling[i]:
			accuracy_score +=score_per_letter

	accuracy_score -= ((abs(len(actual_spelling) - len(user_spelling))) * score_per_letter)

	accuracy_score -= (backstrokes_count * score_per_letter)

	if accuracy_score <= 0:
		return 0
	elif accuracy_score >= 100:
		return 100

	return round(accuracy_score,2)

def get_time_score(actual_spelling, typing_time):
	"""
	The function calculates and returns a score for the speed of typing.

	Arguments:
		actual_spelling (str): The actual correct spelling of the word.
		typing_time (float): The time taken in seconds by the user to type the word.
	
	Returns:
		final_score (int): A value between 0 and 100, both inclusive and rounded to 2 decimal 
		places, for the time score
	"""
	raw_score = (typing_time/AVG_HOVER_TIME + (AVG_KEYSTROKE_TIME*len(actual_spelling) + 1))
	final_score = 100 if raw_score <=1 else 100/raw_score

	return round(max(0, final_score),2)

def view_typing_score(actual_spelling, user_spelling, backstrokes_count, time_taken):
	"""
	The function calculates the total score for the typing tester.

	This function calls the functions to calculate the accuracy score and
	time score and then passes them on to the display functions. It then also
	calculates the total score and sends it to the display function.

	Arguments:
		actual_spelling (str): The actual correct spelling of the word.
		user_spelling (int): The spelling submitted by the user.
		backstrokes_count (int): The count for the backspaces used by user.
		typing_time (float): The time taken in seconds by the user to type the word.
		
	Returns:
		None
	"""
	accuracy_score = get_accuracy_score(actual_spelling, user_spelling, backstrokes_count)
	display_helper("Accuracy Score", accuracy_score)

	time_score = get_time_score(actual_spelling, time_taken)
	display_helper("Time Score", time_score)

	total_score = round((accuracy_score + time_score)/2, 2)
	display_helper("Total Score", total_score)

def typing_tester(user_typing_data, word):
	"""
	The function calculates the scores for the typing tester.

	Arguments:
		user_typing_data (dict): A dictionary containing the following keys and values:
			user_spelling (str): The spelling of the word typed by the user.
			backspaces_count (int): Number of times user has used backspace before submitting.
			submit_time (float): The system time in seconds when the answer was submitted.
			start_time (float): The time when the user was shown the word for typing.
		word (class Word): The object containing information about the word.
	
	Returns:
		None
	"""
	time_taken = round(user_typing_data["submit_time"] - user_typing_data["start_time"], 2)
	display_helper("time_taken", time_taken)

	view_typing_score(
		word.spelling, 
		user_typing_data["user_spelling"], 
		user_typing_data["backspaces_count"], 
		time_taken
	)
	display_helper("Definition", word.definition)
	display_helper("Pronunciation", word.pronunciation) 

