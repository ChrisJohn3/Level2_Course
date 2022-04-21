##########################################################################################
# Team 3 Game for the Code Nation Develop - Coding course, starting on Monday 11th April #
# -------------------------------------------------------------------------------------- #
#                                                                                        #
#  2020-04-20 Code and data file updated to carry Health value and its effects.          #
#               Health value also displayed on every screen and effect shown.            #
#               Initial health value randomised between 75% and 100%                     #
#                                                                         Carl Skafie    #
#                                                                                        #
#  2020-04-19 Code and data file updated to have directions rather than page numbers.    #
#               Text wrapping function developed.                                        #
#                                                                         Chris Johnson  #
#                                                                                        #
#  2020-04-16 Code tidying in readiness for future developments and possible data file   #
#               expansion, specifically around how the nth occourance of a character is  # 
#               identified                                                               #
#                                                                         Chris Johnson  #
#                                                                                        #
# 2020-04-15 Due to requirements clarification data import and in game data selection    #
#               rewritten so as not to rely on the installation of specific packages.    #
#            Data csv structure updated to hold the next Goto_page as well, enabling     #
#               verification of the users choice                                         #
#            Structure now: page number, choice number, Goto_page, Text                  #
#                                                                         Chris Johnson  #
#                                                                                        #
# 2020-04-14 Initial sturture coded based around pages of a choose your own adventure    #
#               book.  The data csv file holding the page number, choice number and the  #
#               text associated with that choice.                                        #
#               Page main text to be in choice 0 - choice printed out in order           #
#                                                                         Chris Johnson  #
##########################################################################################

# Libary Imports
# --------------

# Import of libraries that have been written elsewhere so   # 
# I can nick some of their functions and not have to        #
# create my own.                                            #

# os & time are just being brought in identify which system #
# we are running on (different ones = different commands)   #
# and to allow the sleep function which will make the code  #
# take a break for a specified number of seconds            #
from os import system, name 
from time import sleep

# Function Definitions
# --------------------

# Function to control the length of the printed out string  #
# and where possible avoid line breaks in the middle of     #
# words.  Into it will be passed the string to wrapped and  #
# the line length limit.                                    #


def text_wrapper (text_to_wrap,desired_max_length):
    # First lets get the length of the entire string that   # 
    # we have been passed.  We don't want to get errors by  # 
    # trying to jump passed the end of the string           #
    
    tt_len=len(text_to_wrap)

    # Initialise the start position, this will be updated   # 
    # to hold how far through the string we have managed to #
    # progress                                              # 
    
    start_pos=0

    # Now lets grab a chunk of the text string we have been #
    # passed. This will be repeated until out start         #
    # position reaches the end of the text string           #
    while start_pos<tt_len:
        # Using the rfind method to get the first           #
        # occourance of a space working from the right to   #
        # the left of the string                            #
        line_len=text_to_wrap[start_pos:min(start_pos+desired_max_length,tt_len)].rfind(" ")
        # If the space was not found then a -1 will have    #
        # been returned in which case we will just take the #
        # max allowed length as we will have to split the   #
        # word                                              #
        if line_len<=0:
            line_len=desired_max_length
            # printout the chunk we have identified 
            print(text_to_wrap[start_pos:start_pos+line_len])
            # Move the start position to the end of the     #
            # string we just sent back                      #
            start_pos+=line_len
        else :
            print(text_to_wrap[start_pos:start_pos+line_len])
            # Move the start position to the end of the     #
            # string we just sent back                      #
            start_pos+=line_len
            # Oh-and we don't want the space that was there #
            start_pos+=1
    # Testing Lines used to see the progression through the function
        # print(str(tt_len) +"   -    " + str(start_pos) +  "   -   " + str(line_len) +"   -   " )
        # sleep(0.5)


# The following clear() function clears the terminal screen #
# It was found after a google search for how to clear the   #
# terminal and stolen entirely - however it the name        #
# variable imported "from os" above to know which operating #
# system is in use and then issue the correct command for   #
# that system                                               #

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# The next function is currently the guts of this code.     #
# First we clear the screen so as no confusion from earlier.#
# First we ensure that our selection list is empty, it is   #
# then populated with if the value in the same index        #
# position is equal to the value we want.  Now that we have #
# a list of if the record is one that we want we can now    #
# step through this list with the list containing our text  #
# and populate the screen with it if it is in the correct   #
# index position, with an extra space in between each for   #
# readability                                               #


def page_up(pag_no):
    clear()

# Below code was optimised as no need to create selection   #
# list saving memory and processing, action taken at        #   
# evaluation of criteria point. Original commented out but  #
# left for reference and understanding.                     #
                           


    # sel_list=[]
    # for i in range(len(list_to_fill)):
    #     sel_list.append(list_to_fill[i]==pag_no)
    # for i in range(len(sel_list)):
    #     if sel_list[i]==True:
    #         print(list_to_fill3[i].strip('"'))
    #         print()


# Updated to include the population of the available option #
# on page selection.  This then can be used to limit the    #
# User's route through the game                             #
    global health
    global awr_accept
    global choice_accept
    global choice_text
    choice_accept=[]
    awr_accept=['9999']
    for i in range(len(list_to_fill)):
        if list_to_fill[i]==pag_no:
            awr_accept.append(list_to_fill3[i])
            choice_accept.append(list_to_fill2[i])
            text_wrapper(list_to_fill5[i].strip('"').strip(),120)
            print("Your health Value coming in to this room was " + str(health))
            health = (health) + int(list_to_fill4[i])
            print("Your health Value is now "+ str(health))
            # print(list_to_fill4[i].strip('"'))
            print()
            
    # print(awr_accept)
    # print(choice_accept)
    choice_text="Available options are:"
    for i in range(len(choice_accept)):
        choice_text=choice_text + " "+choice_convert[i]

    print(choice_text)
    print()

# When the user enters an option we will need to check if   #
# that is a valid option from this point in the game.  When #
# loading the current page we also populated the list of    #
# acceptable answers, so when the user enters their option  #
# we can see if the entry exists within that list.  If not  #
# display what options are available and ask the user to    #
# try again. Looping until they get a valid option          #

def usr_page_sel ():
    global awr_accept
    fred=None
    while fred==None:
        fred=input("Next Choice / Page Number Please : ")
        if choice_convert.count(str(fred))>0:
            # print(awr_accept[choice_convert.index(fred)+1])
            # sleep(1)
            return int(awr_accept[choice_convert.index(fred)+1])
            # break
        elif int(fred)==9999:
            return int(fred)

        else :
            fred=None
            print()
            print("Not a valid option !")
            print("Available Options are : ")
            print(choice_text)
            print()
            sleep(2)

# Finds the nth time a string appears in another as find    #
# only returns the first one                                #

def find_nth(start_str,str_to_find,nth):
    val = -1
    for i in range(0, nth):
        val = start_str.find(str_to_find, val + 1)
    return val

# Run initalisation 
# -----------------

# Next we need to get our game data and hold it in the      #
# memory so we can interrogate it for the game.             #

# Create the initalised health value in a variable , value to be between 75 and 100
import random
global health
health = int(random.random() * 25) + 75
# health = 100

list_to_fill=[]
list_to_fill2=[]
list_to_fill3=[]
list_to_fill4=[]
list_to_fill5=[]
global awr_accept 
awr_accept=['9999']
global choice_accept
choice_accept=[]

choice_convert=['Spin','North','East','South','West']

file1 = open("highway_holocaust4.csv", 'r')
# file1 = open("E:/aaaa Level 2 Certificate Python etc/Backup_game.csv", 'r')
Lines = file1.readline()
cols_to_import=Lines.count(',')+1
j=1


print(r" ________         ____           __       ")
sleep(0.25)
print(r"/_  __/ /  ___   / __/_ _  ___  / /___ __ ")
sleep(0.25)
print(r" / / / _ \/ -_) / _//  ' \/ _ \/ __/ // / ")
sleep(0.25)
print(r"/_/ /_//_/\__/ /___/_/_/_/ .__/\__/\_, /  ")
sleep(0.25)
print(r"                        /_/       /___/   ")
sleep(0.25)

print(r"   ___                      __          ")
sleep(0.25)
print(r"  / _ )__ _____  ___ ____ _/ /__ _    __")
sleep(0.25)
print(r" / _  / // / _ \/ _ `/ _ `/ / _ \ |/|/ /")
sleep(0.25)
print(r"/____/\_,_/_//_/\_, /\_,_/_/\___/__,__/ ")
sleep(0.25)
print(r"               /___/                    ")
sleep(2)


for i in file1:
# Each line will be interpreted for the four pieces of data # 
# it holds, the first three pieces are ended by a comma     #
# - however the last piece can have commas within it.       #
# They will be put in the holding lists in matching index   #
# positions                                                 #
# Although there are a lot of find statements in here all   #
# they are trying to do is find the start and end position  #
# of each piece of data.  To manually see it through go     #
# along a line until the brackets stop opening and start    #
# closing,  figure out what value the function with those   #
# brackets gives and then put that into the next set out    #


    # list_to_fill.insert(j,int(i[0:i.find(",")]))
    # list_to_fill2.insert(j,i[i.find(",")+1:i.find(",",i.find(",")+1)])
    # list_to_fill3.insert(j,i[i.find(",",i.find(",")+1)+1:i.find(",",i.find(",",i.find(",")+1)+1)])
    # list_to_fill4.insert(j,i[i.find(",",i.find(",",i.find(",")+1)+1)+1:len(i)])

# Code becoming extreamely messy so developed function      # 
# find_nth() to find the nth time a string appeared         #
# within another                                            #

    list_to_fill.insert(j,int(i[0:find_nth(i,',',1)]))
    list_to_fill2.insert(j,i[find_nth(i,',',1)+1:find_nth(i,',',2)])
    list_to_fill3.insert(j,i[find_nth(i,',',2)+1:find_nth(i,',',3)])
    list_to_fill4.insert(j,i[find_nth(i,',',3)+1:find_nth(i,',',4)])
    list_to_fill5.insert(j,i[find_nth(i,',',4)+1:len(i)])

    j+=1
    
file1.close()

# sleep(3)
clear()

# Lets set the first page as the selected page, that way we #
# have a value in place when we call the page_up function   #
sel_page=1


# Run core 
# --------

# In essence we want to do the same thing again and again   #
# That is put some info on screen and get a user response   #
# So we will use a while loop,  this requires some          #
# achievable value to be able to exit - otherwise we have   #
# an infinate loop - I chose 9999                           #

while sel_page != 9999 and health > 0:
    page_up(sel_page)
    sleep(1)
    sel_page=usr_page_sel()
    # sel_page=int(input("Next Choice / Page Number Please : "))

# Run Completion
# --------------

# Just say goodbye to our customers and then leaving the    #
# terminal clear to show we are out of the way :)           #
clear()

print(r" o-o    O  o   o o--o      o-o  o   o o--o o--o  ")
sleep(0.25)
print(r"o      / \ |\ /| |        o   o |   | |    |   | ")
sleep(0.25)
print(r"|  -o o---o| O | O-o      |   | o   o O-o  O-Oo  ")
sleep(0.25)
print(r"o   | |   ||   | |        o   o  \ /  |    |  \  ")
sleep(0.25)
print(r" o-o  o   oo   o o--o      o-o    o   o--o o   o ")

sleep(0.25)
print()
print("Thanks for playing our game, we're sure you died horribly but at least here you can do it again.  Don't do this in real life it's a one time deal!!!")
sleep(3.5)
clear()


# Thinking around the Health Value to be carried / effected through the game

# First we will need to create a variable that will hold the heath value.  
# What range will the health cover - straight % or out of 200? 
# We need to show the health value on each screen
#
# We can then create a random value - with a minimum and maximum to populate into this variable at the start of each game
# To have each room potentially effect the Health value the effect will have to be included in the file with the room data 
# Because of the structure of the data file this will be included prior to the room/option Text and will need an extra list 
# in the program for the data to be loaded into.  
# 
# Then as a part of the screen display function we can add on or take away however many points are related to that room
#
# Overall we can then make the main while loop also consider that the Health value must be above x otherwise goto GAME OVER 
# screen and then pause and go back to game start again 
