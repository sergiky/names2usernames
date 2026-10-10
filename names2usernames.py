#!/usr/bin/env python3

import argparse
import os
import random as rd

term_size = os.get_terminal_size()

parser = argparse.ArgumentParser(prog='names2usernames', description='Transform names to most common account conventions')
parser.add_argument('-u', '--username')
parser.add_argument('-f', '--file', help="File with the possible users in a wordlist format")
parser.add_argument('-r', '--random', help='Randomize order of usernames', action='store_true')
parser.add_argument('-o', '--output')

args = parser.parse_args()
names = []
usernames = []
not_valid_users = []

if args.username:
    names.append(args.username)

if args.file:
    with open (args.file, "r") as file:
        names = [name.strip() for name in file.readlines() if name.strip()]

def check_second_names():
    for i, name in enumerate(names):
        if len(name.split()) >= 4:
            names[i] = f"{name.split()[0]} {name.split()[2]}"

def check_unique_names():
    for i, name in enumerate(names):
        if len(name.split()) == 1:
            not_valid_users.append(names[i])
            names.pop(i)


def transform():
    '''
    1. firstName.lastName = sergio.guijarro
    2. firstInitiallastName = sguijarro
    3. firstNamelastInitial = sergiog
    '''

    check_unique_names()
    check_second_names()
    for name in names:
        usernames.append(f"{name.split()[0]}.{name.split()[1]}")
        usernames.append(f"{name.split()[0][0]}{name.split()[1]}")
        usernames.append(f"{name.split()[0]}{name.split()[1][0]}")

def random():
   rd.shuffle(usernames) 

def output():
    with open(args.output, 'w') as f:
        f.writelines([usern + '\n' for usern in usernames])

def help_panel():
    parser.print_help()

def horizontal_line():
    print('=' * term_size.columns)

def center_text(text):
    terminal_width = term_size[0]
    input_length = len(text)
    empty_space_required = int((terminal_width - input_length) / 2)
    empty_space = empty_space_required * ' '
    print(empty_space + text)

def banner():
    print("""

                                                   .d8888b.                                                                                       
                                                  d88P  Y88b                                                                                      
                                                         888                                                                                      
88888b.   8888b.  88888b.d88b.   .d88b.  .d8888b       .d88P 888  888 .d8888b   .d88b.  888d888 88888b.   8888b.  88888b.d88b.   .d88b.  .d8888b  
888 "88b     "88b 888 "888 "88b d8P  Y8b 88K       .od888P"  888  888 88K      d8P  Y8b 888P"   888 "88b     "88b 888 "888 "88b d8P  Y8b 88K      
888  888 .d888888 888  888  888 88888888 "Y8888b. d88P"      888  888 "Y8888b. 88888888 888     888  888 .d888888 888  888  888 88888888 "Y8888b. 
888  888 888  888 888  888  888 Y8b.          X88 888"       Y88b 888      X88 Y8b.     888     888  888 888  888 888  888  888 Y8b.          X88 
888  888 "Y888888 888  888  888  "Y8888   88888P' 888888888   "Y88888  88888P'  "Y8888  888     888  888 "Y888888 888  888  888  "Y8888   88888P'                   
""")

if __name__ == "__main__":
    banner()
    print()
    center_text("Usernames")
    horizontal_line()
    transform()
    print()

    if args.random:
        random()
    
    print(*usernames, sep='\n')
    print()

    if not_valid_users:
        print(f"[*] Not valid users detected: ", end="")
        print(*not_valid_users, sep=', ')

    if args.output:
        output()
