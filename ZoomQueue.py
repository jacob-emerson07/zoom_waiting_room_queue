##################################################################################################################
# File: ZoomQueue.py
# Author: Jacob Emerson
# Date of Revision: 4/16/2020
# Description: This file is to help streamline the process of using Zoom's waiting room feature
#              by adding a Queue that keeps track of who entered the waiting room first.
#
# Note: This project does include third party libraries. This file also works best if you have a
# 		multi-monitor set up as the screen capture naturally takes a screenshot of the main screen.
#
##################################################### Imports ####################################################

import queue

import PIL as pillow #Image saving, viewing

import pyscreenshot as ImageGrab #Image taking

import pytesseract as ptt #Text extraction from image

#Initialize tesseract
ptt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

##################################################### Globals ####################################################


HOST_NAME = None
ZOOM_PHRASES = ["person is waiting", "participant in the meeting"]
WAITING_ROOM = list()
q = queue.Queue()
DEBUG = False

#################################################### Functions ###################################################

def toggle_debug():
	global DEBUG
	
	DEBUG = True if False else True

def get_host_name():
	"""
	Grabs the name of the host and appends the (Host, me) tag to the end of it. 
	Sets the global HOST_NAME to the grabbed name.
	"""
	global HOST_NAME

	while True:
		name_of_host = input("What is your name (As it appears in zoom without the '(Host, me)' part)? ")
		HOST_NAME = name_of_host + " (Host, me)"
		correct = input(f"Host name set as {HOST_NAME}, is this correct? [Y/N]: ")
		if correct.upper() == "Y":
			return

def check_names(debug):
	"""
	Grabs screenshot of area selected in the range_of_window variable and extract the names from it 
	into a queue that meet certain conditions.

		1. The input is actually a name (hard-coded to track statements that zoom uses to separate people in the
		   waiting room vs people in the meeting).
		2. The name is not currently in the queue (checked through a WAITING_ROOM global).
		3. The name is not the hosts.
		4. The name is not the person currently being helped.

	"""

	#Free to change to whatever fits your current setup. Just make sure that nothing is over it when you are
	# running this function.
	range_of_window = (1000,75,1250,880)

	im = ImageGrab.grab(bbox=range_of_window)

	im.save('screenshot.png')

	#If debug is on, see the picture that is being taken.
	if debug:
		im.show()

	text = ptt.image_to_string('screenshot.png').split("\n")
	for name in text:
		if ZOOM_PHRASES[1] in name:
			break

		if _validate_name(name):
			WAITING_ROOM.append(name)
			q.put(name)

def next_name():
	"""
	Prints the person in the front of the queue. If the queue is empty, it will print as such.
	Also removes the person from the queue and the WAITING_ROOM list.
	"""
	if not q.empty():
		name = q.get()
		WAITING_ROOM.remove(name)
		print(name)
	else:
		print("Queue is Empty")

def empty_queue():
	while not q.empty():
		name = q.get()
		WAITING_ROOM.remove(name)

def print_names():
	for name in WAITING_ROOM:
		print(name)

def print_host_name():
	print(HOST_NAME)

############################################ Private Functions ###################################################

def _validate_name(name):
	"""
	Validates names based on the guidelines mentioned in check_names().
	"""
	if HOST_NAME != name and len(name) > 0 and ZOOM_PHRASES[0] not in name and name not in WAITING_ROOM:
		return True
	return False

############################################## Main Script #######################################################

if __name__ == '__main__':

	get_host_name()

	while True:
		command = input()

		if command.upper() == "NEXT":
			next_name()
		elif command.upper() == "CHECK":
			check_names(DEBUG)
		elif command.upper() == "EMPTY":
			empty_queue()
		elif command.upper() == "PRINT":
			print_names()
		elif command.upper() == "QUIT":
			break
		elif command.upper() == "DEBUG":
			toggle_debug()
		elif command.upper() == "HOST":
			print_host_name()
		else:
			continue
