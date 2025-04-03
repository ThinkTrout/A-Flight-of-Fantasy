# Welcome to A Flight of Fantasy, a text-based RPG game created by ThinkTrout.

import random
import sys
import textwrap
import termios
import fcntl
import os
import time
from os import system as system
from time import sleep as sleep
from colors import *
from plot import *

# Keyboard Functions -----------------------------------

def ignore_keyboard():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    return oldterm, oldflags, fd

def restore_keyboard(oldterm, oldflags, fd):
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

# System Functions -----------------------------------

def sysMessage(color, text, time=None):
    wait = time if time is not None else 0.5
    print(f'\n{color}{text}{DEFAULT}')
    sleep(wait)
    system('clear')
    sleep(0.2)

def clear():
    sleep(0.5)
    system('clear')
    sleep(0.2)

# Game Functions -----------------------------------

def typeThenInstant(type,typespeed,instant,delay):
    typeout(type,typespeed)
    time.sleep(delay)
    print(instant)
    time.sleep(delay)

def typeout(sentence, delay):
    oldterm, oldflags, fd = ignore_keyboard()
    try:
        for char in sentence:
            if is_enter_pressed(fd):
                system('clear')
                print(sentence)
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay)
    finally:
        restore_keyboard(oldterm, oldflags, fd)

def is_enter_pressed(fd):
    try:
        input_char = os.read(fd, 1)
        return input_char == b'\n'  # Check if the Enter key is pressed
    except OSError:
        return False

def story(text, delay):
    final_text = text + input_box
    oldterm, oldflags, fd = ignore_keyboard()
    typeout(final_text, delay)
    restore_keyboard(oldterm, oldflags, fd)
    return input()

def intro():
    clear()
    repeat = False
    current_chapter = 1
    
    while current_chapter:
        wrapped_text = textwrap.fill(chapters[current_chapter]["text"], 50)

        if chapters[current_chapter]["type"] == "continue":
            if not repeat:
                user_input = story(wrapped_text, type_speed)
            else:
                user_input = input(wrapped_text + input_box)

            if user_input == '':
                next_chapter = current_chapter + 1
                if next_chapter in chapters:  
                    current_chapter = next_chapter
                    repeat = False
                    clear()
                else:
                    clear()
                    break  # Ends the game if no next chapter exists
            else:
                sysMessage(RED, 'Invalid input. Press [ENTER] to continue.')
                repeat = True

        elif chapters[current_chapter]["type"] == "choice":
            choice_text = wrapped_text+f'\n\n'+'\n'.join(chapters[current_chapter]["options"])
            if not repeat:
                user_input = story(choice_text, type_speed)
            else:
                user_input = input(choice_text + input_box)

            user_input = user_input.lower().strip()

            if user_input in chapters[current_chapter]["inputs"]:
                current_chapter = chapters[current_chapter]["inputs"][user_input]
                repeat = False
                clear()
            else:
                sysMessage(RED, 'Invalid input. Try again.')
                repeat = True

# Game Loop -----------------------------------

input_box = '\n\n> '
type_speed = 0.015
intro()