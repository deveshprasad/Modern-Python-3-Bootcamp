# MODULES


# DIIFERENT WAYS OFMIMPORTING MODULES
# import random
# import random as omg
# from random import *
# from random import choice,shuffle
# from random import choice as gimmeone,shuffle as mixup

# this in anaconda command prompt
#To install this package with conda run:
#conda install -c omnia termcolor
#
# in spyder to run it or activate
#To install this package with conda run one of the following:
#conda install -c conda-forge unicodedata2


from termcolor import colored
text=colored("hi there!",color='magenta',on_color='on_green',attrs=["blink"])
print(text)

# in anaconda comand prompt
#To install this package with conda run one of the following:
#conda install -c conda-forge pyfiglet
import pyfiglet
from termcolor import colored
msg=input('ENTER  :  ')
color=input('Enter color  : ')
ascii_art=pyfiglet.figlet_format(msg)
colored_ascii=colored(ascii_art,color=color)
print(colored_ascii)
# ____  _______     _______ ____  _   _   ___ ____  
#|  _ \| ____\ \   / / ____/ ___|| | | | |_ _/ ___| 
#| | | |  _|  \ \ / /|  _| \___ \| |_| |  | |\___ \ 
#| |_| | |___  \ V / | |___ ___) |  _  |  | | ___) |
#|____/|_____|  \_/  |_____|____/|_| |_| |___|____/ 
#                                                   
# ____  _        _ __   ______   _____   __
#|  _ \| |      / \\ \ / / __ ) / _ \ \ / /
#| |_) | |     / _ \\ V /|  _ \| | | \ V / 
#|  __/| |___ / ___ \| | | |_) | |_| || |  
#|_|   |_____/_/   \_\_| |____/ \___/ |_|  
#                                          

from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "magenta"

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)
#_ __   __ _ _ __   __ _  __ _ 
#| '_ \ / _` | '_ \ / _` |/ _` |
#| | | | (_| | | | | (_| | (_| |
#|_| |_|\__,_|_| |_|\__, |\__,_|
#                   |___/       
#########################################################if name=__main__
#every python has name variable 
#if file is main file its value is main file

def sayhi():
    print(f'hi my __name__ is {__name__}')
sayhi()
# hi my __name__ is __main__

def sayhi2():
    print(f'hi2 my __name__ is {__name__}')
sayhi2()

from sayhi2 import sayhi2# when using file to file importing

#
#hi2 my __name__ is sayhi2
#hi my name is main
#hi2 my __name__ is sayhi2 
#
#if file is main file its value is main file
# other wise value is file name


if __name__ == "__main__":
#    this code will run only 
#    if file is main file


def sayhi2():
    print(f'hi2 my __name__ is {__name__}')
if __name__ == "__main__":
sayhi2()






##################################################################
#
#To install this package with conda run one of the following:
#conda install -c conda-forge autopep8
import math
import sys


def example1():
    # This is a long comment. This should be wrapped to fit within 72
    # characters.
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        'long': 'Long code lines should be wrapped within 79 characters.',
        'other': [
            math.pi,
            100,
            200,
            300,
            9876543210,
            'This is a long string that goes on'],
        'more': {
            'inner': 'This whole logical line should be wrapped.',
            some_tuple: [
                1,
                20,
                300,
                40000,
                500000000,
                60000000000000000]}}

    is_cat_owner = True
    if is_cat_owner:
        print("MEOW!")
    return (some_tuple, some_variable)


def example2(): return (
    '' in {'f': 2}) in {'has_key() is deprecated': True};


class Example3(object):
    def __init__(self, bar):
        # Comments should have a space after the hash.
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
            return (sys.path, some_string)
###############################
            
        
        
import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False
args=[1,2,3,4]
contains_keyword(1)# false
contains_keyword('d')