# Author - Kushagra Mittal
# Date - 27/11/2020
# Project - Text Based Adventure Game - Light Pollution Awareness Game - Election Mania


import cmd
import textwrap
import random
import sys
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style

screen_width = 100

''' Universal Functions '''

def text(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != '\n':
            time.sleep(0.05)
        else:
            time.sleep(0.5)

def Happy_Meter(percent):
    #Use this function to print the happy meter
    #Happy meter must always be of same length.
    a = int(percent)/100
    Yes = a*30
    Yes = int(Yes)
    No = 30-Yes
    if 75 <= percent: #Green
        Bar = Back.RESET + Fore.WHITE + '[' + Back.GREEN + (Yes * f' ') + Back.RESET + (No * ' ') + Fore.WHITE + ']'
    elif 50 <= percent < 75: #Yellow
        Bar = Back.RESET + Fore.WHITE + '[' + Back.YELLOW + (Yes * f' ') + Back.RESET + (No * ' ') + Fore.WHITE + ']'
    elif percent < 50: #Red
        Bar = Back.RESET + Fore.WHITE + '[' + Back.RED + (Yes * f' ') + Back.RESET + (No * ' ') + Fore.WHITE + ']'
    os.system('cls')
    print(Fore.RED + f'')
    print(Fore.RED + f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')

    with open('Happy Meter.txt', 'r', encoding="utf8") as screen:
        for lines in screen:
            print('     ' + Fore.GREEN + lines, end='')
            time.sleep(0.1)
    print(f'\n')
    print()
    text(Fore.CYAN + f'  Your decision impacted your re-election probability.\n')
    print()
    text(Fore.CYAN + f'  Here is your constituency\'s Happy-Meter from your work.\n')
    print()
    print('  ' + Bar + f' ' + str(percent) + '%')

    print(Fore.RED + f'')
    print(Fore.RED + f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')

def calculator(prev_percent, new_percent):
    prev_percent = int(prev_percent)
    new_percent = int(new_percent)
    percent = (prev_percent + new_percent)/2
    Happy_Meter(percent)
    return percent

''' Title Screen '''

def title_screen_selection():
    print(Fore.GREEN + '')
    option = input(f'> ')
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    else:
        while option.lower not in ['play', 'help', 'quit']:
            print(Fore.RED + f'Please enter a valid response')
            option = input(Fore.GREEN + f'> ')
            if option.lower() == ("play"):
                start_game()
            elif option.lower() == ("help"):
                help_menu()
            elif option.lower() == ("quit"):
                sys.exit()

def title_screen():
    Style.RESET_ALL
    os.system('cls')
    print(Fore.RED + '')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f' <+>                                        ' + Fore.YELLOW + f'Welcome to Election Mania!' + Fore.RED + f'                                                <+>\n')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'- Play -' + Fore.RED + f'                                                        <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'- Help -' + Fore.RED + f'                                                        <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'- Quit -' + Fore.RED + f'                                                        <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    title_screen_selection()

''' Help '''

def help_menu():
    Style.RESET_ALL
    os.system('cls')
    print(Fore.RED + '')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f' <+>                                        ' + Fore.YELLOW + f'Welcome to Election Mania!' + Fore.RED + f'                                                <+>\n')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+> ' + Fore.YELLOW + f'-In \'Election Mania\' you are the Mayor of a city and you make decisions that would determine' + Fore.RED + f'                     <+>\n')
    print(f' <+>  ' + Fore.YELLOW + f'your re-election you must keep Light Pollution in mind while making these decisions' + Fore.RED + f'                             <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+> ' + Fore.YELLOW + f'-The Happy-Meter will display the % of people who will re-elect you. It updates for each decision you make' + Fore.RED + f'       <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+> ' + Fore.YELLOW + f'-An input is awaited when '+Fore.GREEN + '\'> \''+ Fore.YELLOW + ' is displayed.' + Fore.RED + f'                                                                     <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+> ' + Fore.YELLOW + f'-The Happy-Meter must be above 75%' + Fore.RED + f'                                                                               <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+> ' + Fore.YELLOW + f'-Good luck, Have Fun' + Fore.RED + f'                                                                                             <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                            ' + Fore.YELLOW + f'Return to Title Screen' + Fore.RED + f'                                                <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'-  Home  -' + Fore.RED + f'                                                      <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    help_screen_selection()

def help_screen_selection():
    print(Fore.GREEN + '')
    option = input(f'> ')
    if option.lower() == ("home"):
        title_screen()
    else:
        while option.lower not in ['home']:
            print(Fore.RED + f'Please enter a valid response')
            option = input(Fore.GREEN + f'> ')
            if option.lower() == ("home"):
                title_screen()


''' GAME '''

def start_game():
    Style.RESET_ALL
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                              ' + Fore.YELLOW + f'You should read Help section before moving forward...' + Fore.RED + f'                               <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'-  Start  -' + Fore.RED + f'                                                     <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                                  ' + Fore.YELLOW + f'Need Help?' + Fore.RED + f'                                                      <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'-  Help  -' + Fore.RED + f'                                                      <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                            ' + Fore.YELLOW + f'Return to Title Screen' + Fore.RED + f'                                                <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'-  Home  -' + Fore.RED + f'                                                      <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    play_screen_selection()

def play_screen_selection():
    print(Fore.GREEN + '')
    option = input(f'> ')
    if option.lower() == ("home"):
        title_screen()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("start"):
        game()
    else:
        while option.lower not in ['home', 'help', 'start']:
            print(Fore.RED + f'Please enter a valid response')
            option = input(Fore.GREEN + f'> ')
            if option.lower() == ("home"):
                title_screen()
            elif option.lower() == ("help"):
                help_menu()
            elif option.lower() == ("start"):
                game()

def game():
    Style.RESET_ALL
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(Fore.CYAN + f'')
    text(f'  Welcome to the Light Pollution Awareness Game!\n')
    text(f'  You are the Mayor of this City.\n')
    text(f'  Your decisions decide the fate of your City!\n')
    print(f'')
    print(f'                                                      ' + Fore.YELLOW + f'GAME SETUP' + f'                                                         \n')
    print(Fore.CYAN + f'')
    text(f'  How should we address you?\n')
    print(f'  Enter your name \n')
    Name = input(Fore.GREEN + f'> ')
    print(Fore.CYAN + f'  Type 1 for Mr. and type 2 for Ms. \n')
    Salutation = input(Fore.GREEN + f'> ')
    if Salutation == ('1'):
        Name = 'Mr. ' + Name
    elif Salutation == ('2'):
        Name = 'Ms. ' + Name
    while Salutation not in ['1', '2']:
        print(Fore.RED + f'  Please enter a valid response!')
        Salutation = input(Fore.GREEN + f'> ')
        if Salutation == ('1'):
            Name = 'Mr. ' + Name
        elif Salutation == ('2'):
            Name = 'Ms. ' + Name
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')
    input(Fore.YELLOW + f'  Press Enter to continue...')
    time.sleep(1)

    ### Clear Screen
    
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(Fore.CYAN + f'')
    text(f'  Let us begin ' + Name + '\n')
    text(f'  What type of geographical area would you like to play in?\n')
    text(f'  Press 1 for Busy Urban City or press 2 for Peaceful Countryside Town\n')
    print(f'')
    Area = input(Fore.GREEN + f'> ')
    if Area == ('1'):
        print(Fore.CYAN + f'')
        text(f'  Welcome to your City ' + Name + ', let us begin by naming your City.\n')
        text(f'  Choose a name for your City...\n')
        
        place = input(Fore.GREEN + f'> ')

        print(Fore.RED + f'')
        print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
        print('')
        input(Fore.YELLOW + f'  Press Enter to continue...')
        time.sleep(1)

        city(place, Name)

    elif Area == ('2'):
        print(Fore.CYAN + f'')
        text(f'  Welcome to your Town ' + Name + ', let us begin by naming your Town.\n')
        text(f'  Choose a name for your Town...\n')
        print('')
        
        place = input(Fore.GREEN + f'> ')
        
        print(Fore.RED + f'')
        print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
        print('')
        input(Fore.YELLOW + f'  Press Enter to continue...')
        time.sleep(1)
    
        town(place, Name)
    
    while Area not in ['1', '2']:
        print(Fore.RED + f'  Please enter a valid response!')
        Area = input(Fore.GREEN + f'> ')
        if Area == ('1'):
            print(Fore.CYAN + f'')
            text(f'  Welcome to your City ' + Name + ', let us begin by naming your City.\n')
            text(f'  Choose a name for your City...\n')
            
            place = input(Fore.GREEN + f'> ')

            print(Fore.RED + f'')
            print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
            print('')
            input(Fore.YELLOW + f'  Press Enter to continue...')
            time.sleep(1)

            city(place, Name)

        elif Area == ('2'):
            print(Fore.CYAN + f'')
            text(f'  Welcome to your Town ' + Name + ', let us begin by naming your Town.\n')
            text(f'  Choose a name for your Town...\n')
            print('')
            
            place = input(Fore.GREEN + f'> ')
            
            print(Fore.RED + f'')
            print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
            print('')
            input(Fore.YELLOW + f'  Press Enter to continue...')
            time.sleep(1)
        
            town(place, Name)


def city(place, Name):

    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')
    with open('City.txt', 'r') as screen:
        for lines in screen:
            print(Fore.WHITE + lines, end='')
            time.sleep(0.1)

    print(f'')
    print(Fore.CYAN + f'')
    text(f'  Elections are coming up in ' + place +', '+ Name + ' as the Mayor of this City,\n')
    text(f'  your decisions are influential for your re-election. \n')
    text(f'  Be careful about your choices and choose what is best for the environment to increase \n  your probability of being re-elected.\n')
    text(f'  Your voters are environment enthusiasts. You require at least 75% of the public to be happy to win \n')
    
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')
    
    question1(Name, place)

    Game_End()

    #######################################################################################################################################

def town(place, Name):

    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    # Print Town.txt line by line
    print(f'')
    with open('Town.txt', 'r') as screen:
        for lines in screen:
            print(Fore.WHITE + lines, end='')
            time.sleep(0.1)

    print(f'')
    print(Fore.CYAN + f'')
    text(f'  Elections are coming up in ' + place +', '+ Name + ' as the Mayor of this Town,\n')
    text(f'  your decisions are influential for your re-election. \n')
    text(f'  Be careful about your choices and choose what is best for the environment to increase \n  your probability of being re-elected.\n')
    text(f'  Your voters are environment enthusiasts. You require at least 75% of the public to be happy to win \n')
    
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')

    question1(Name, place)

    Game_End()


def question1(Name, place):    
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')

    with open('Lights.txt', 'r') as screen:
        for lines in screen:
            print('   ' + Fore.WHITE + lines, end='')
            time.sleep(0.1)

    print(f'')
    print(Fore.CYAN + f'')
    text(f'  Unknown: Hello there! I am Cynthia your assistant. Lets get going, you have a long day ahead...\n')
    print()
    text(f'  ' + Name +': Oh, well there is no time to waste in view of Elections. What is the first order of business Cynthia?\n')
    print()
    text(f'  Cynthia: The street lights must be replaced many of them have broken down.\n')
    text(f'           You need to decide if we use (1) CFL bulbs or (2) Led bulbs.\n')
    text(f'           although we can save money if we use CFL bulbs they are far cheaper than those new LED bulbs...\n')
    print()
    print(Fore.YELLOW + f'  You need to take a decision.\n')
    Space = len(Name) + 2
    question1 = input(Fore.GREEN + f'> ')
    
    if question1 == '1':
        text(Fore.CYAN +f'  '+ Name + f': You are right, we can make ourselves richer by using CFL bulbs.\n')
        percent = random.randint(35, 65)
    
    elif question1 == '2':
        text(Fore.CYAN + f'  '+ Name+ f': CFL may be cheap but it consumes more electricity and produces less light,\n')
        text(f'  ' + (Space*f' ') + f'while the LED consumes less electricity and produces more light, which will be good in a long run.\n')
        percent = random.randint(75, 100)
    
    while question1 not in ['1','2']:
        print(Fore.RED + '  Please enter a valid response')
        question1 = input(Fore.GREEN + f'> ')
        
        if question1 == '1':
            text(Fore.CYAN +f'  '+ Name + f': You are right, we can make ourselves richer by using CFL bulbs.\n')
            percent = random.randint(35, 65)
        
        elif question1 == '2':
            text(Fore.CYAN + f'  '+ Name+ f': CFL may be cheap but it consumes more electricity and produces less light,\n')
            text(f'  ' + (Space*f' ') + f'while the LED consumes less electricity and produces more light, which will be good in a long run.\n')
            percent = random.randint(75, 100)
    

    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')

    os.system('cls')

    prev_percent = percent
    calculator(prev_percent, percent)

    #starts second question
    question2(Name, percent, place)

def question2(Name, prev_percent, place):
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')

    with open('Boat.txt', 'r') as screen:
        for lines in screen:
            print('   ' + Fore.WHITE + lines, end='')
            time.sleep(0.1)

    print(f'')
    print(Fore.CYAN + f'')
    text(f'  \n')
    print()
    text(f'  ' + Name +': What is next task on the to-do list Cynthia?\n')
    print()
    text(f'  Cynthia: Remember the complaints about boats in the pond we had a while ago...\n')
    text(f'           It\'s time to get them changed as well its not a hassle since there are only 7 damaged boats. \n')
    text(f'           What do you say... Electric boats to replace fuel boats in the pond? It may increase our annual electricity consumption...\n')
    print()
    print(Fore.YELLOW + f'  You need to take a decision. (Yes/No)\n')
    Space = len(Name) + 2
    question2 = input(Fore.GREEN + f'> ')
    
    if question2.lower() == 'no':
        text(Fore.CYAN +f'  '+ Name + f': So what if it would reduce water pollution? Huh? It still increases the electric consumption that would be expensive\n')
        percent = random.randint(35, 65)
    
    elif question2.lower() == 'yes':
        text(Fore.CYAN + f'  '+ Name+ f': Electric transportation is the future! It will even reduce water pollution.\n')
        text(f'  ' + (Space*f' ') + f'Instead of thinking about it as an addition to our electricity consumption, we should work on sustainable sources.\n')
        percent = random.randint(75, 100)
    
    while question2.lower() not in ['yes','no']:
        print(Fore.RED + '  Please enter a valid response')
        question2 = input(Fore.GREEN + f'> ')
        
        if question2.lower() == 'no':
            text(Fore.CYAN +f'  '+ Name + f': So what if it would reduce water pollution? Huh? It still increases the electric consumption that would be expensive\n')
            percent = random.randint(35, 65)
        
        elif question2.lower() == 'yes':
            text(Fore.CYAN + f'  '+ Name+ f': Electric transportation is the future! It will even reduce water pollution.\n')
            text(f'  ' + (Space*f' ') + f'Instead of thinking about it as an addition to our electricity consumption, we should work on sustainable sources.\n')
            percent = random.randint(75, 100)
    
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')

    os.system('cls')

    
    percent = calculator(prev_percent, percent)
    
    question3(Name, percent, place)

def question3(Name, prev_percent, place):
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')

    with open('Lights.txt', 'r') as screen:
        for lines in screen:
            print('   ' + Fore.WHITE + lines, end='')
            time.sleep(0.1)

    print(f'')
    print(Fore.CYAN + f'')
    text(f'  \n')
    print()
    text(f'  ' + Name +': Now that that is done, I can use a break...\n')
    print()
    text(f'  Cynthia: Uh... I guess not. The re-modelling comittee needs your help.\n')
    text(f'           What do you prefer more (1) Flow Bamboo Lighting or (2) Landscape Lighting for the outdoor lighting... \n')
    print()
    print(Fore.YELLOW + f'  You need to take a decision.\n')
    Space = len(Name) + 2
    question3 = input(Fore.GREEN + f'> ')
    
    if question3 == '2':
        text(Fore.CYAN +f'  '+ Name + f': These fancy Flow Bamboo Lights... they look expensive and probably are not so durabale....\n')
        percent = random.randint(35, 65)
    
    elif question3 == '1':
        text(Fore.CYAN + f'  '+ Name+ f': The lamp is mostly biodegradable and can be easily manufactured by even the most unskilled worker.\n')
        text(f'  ' + (Space*f' ') + f'Moreover artificially changing the light levels impairs the plants’ ability to respond to changing seasons.\n')
        percent = random.randint(75, 100)
    
    while question3 not in ['1','2']:
        print(Fore.RED + '  Please enter a valid response')
        question3 = input(Fore.GREEN + f'> ')
        
        if question3 == '2':
            text(Fore.CYAN +f'  '+ Name + f': These fancy Flow Bamboo Lights... they look expensive and probably are not so durabale....\n')
            percent = random.randint(35, 65)
        
        elif question3 == '1':
            text(Fore.CYAN + f'  '+ Name+ f': The lamp is mostly biodegradable and can be easily manufactured by even the most unskilled worker.\n')
            text(f'  ' + (Space*f' ') + f'Moreover artificially changing the light levels impairs the plants’ ability to respond to changing seasons.\n')
            percent = random.randint(75, 100)
    

    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')

    os.system('cls')


    
    percent = calculator(prev_percent, percent)
    question4(Name, percent, place)

def question4(Name, prev_percent, place):
    os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f'')

    with open('IDA.txt', 'r') as screen:
        for lines in screen:
            print('       ' + Fore.WHITE + lines, end='')
            time.sleep(0.05)

    print(f'')
    print(Fore.CYAN + f'')
    text(f'  \n')
    print()
    text(f'  ' + Name +': What is next task on the to-do list Cynthia?\n')
    print()
    text(f'  Cynthia: Well, cheer up! This is your last task for the day.\n')
    text(f'           We discussed so much about lights... but what light fixtures should I put out an order for?\n')
    text(f'           There are 2 options (1) IDA Approved lighting fixtures or the cheaper (2) Ordinary lighting fixtures\n')
    print()
    print(Fore.YELLOW + f'  You need to take a decision.\n')
    Space = len(Name) + 2

    question4 = input(Fore.GREEN + f'> ')
    if question4 == '1':
        text(Fore.CYAN +f'  '+ Name + f': The fixture seal of approval provides objective, \n')
        text(f'  ' + (Space*f' ') + f'third party certification for luminaries that minimise glare, reduce light trespass, \n')
        text(f'  ' + (Space*f' ') + f'and don’t pollute the night sky\n')
        percent = random.randint(75, 100)
    
    elif question4 == '2':
        text(Fore.CYAN + f'  '+ Name+ f': Does the seal of approval matter so much?\n')
        text(f'  ' + (Space*f' ') + f'These will save us tax payers money and instead we can use it for things people enjoy,\n')
        text(f'  ' + (Space*f' ') + f'we can make a Statue. ( ͡° ͜ʖ ͡°)\n')
        percent = random.randint(35, 65)
    
    while question4 not in ['1','2']:
        print(Fore.RED + '  Please enter a valid response')
    
        question4 = input(Fore.GREEN + f'> ')
    
        if question4 == '1':
            text(Fore.CYAN +f'  '+ Name + f': The fixture seal of approval provides objective, \n')
            text(f'  ' + (Space*f' ') + f'third party certification for luminaries that minimise glare, reduce light trespass, \n')
            text(f'  ' + (Space*f' ') + f'and don’t pollute the night sky\n')
            percent = random.randint(75, 100)
        
        elif question4 == '2':
            text(Fore.CYAN + f'  '+ Name+ f': Does the seal of approval matter so much?\n')
            text(f'  ' + (Space*f' ') + f'These will save us tax payers money and instead we can use it for things people enjoy,\n')
            text(f'  ' + (Space*f' ') + f'we can make a Statue. ( ͡° ͜ʖ ͡°)\n')
            percent = random.randint(35, 65)
        
    
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    
    input(Fore.YELLOW + f' Press Enter to continue...')

    os.system('cls')


    percent = calculator(prev_percent, percent)
    
    result(percent, Name, place)


def result(percent, Name, place):
    percent = int(percent)
    if percent >= 75:
        win(Name, place, percent)
    else:
        lose(Name, place, percent)

def meter(percent):
    a = int(percent)/100
    Yes = a*30
    Yes = int(Yes)
    No = 30-Yes
    if 75 <= percent: #Green
        Bar = Back.RESET + Fore.WHITE + '[' + Back.GREEN + (Yes * f' ') + Back.RESET + (No * ' ') + Fore.WHITE + ']'
    elif 50 <= percent < 75: #Yellow
        Bar = Back.RESET + Fore.WHITE + '[' + Back.YELLOW + (Yes * f' ') + Back.RESET + (No * ' ') + Fore.WHITE + ']'
    elif percent < 50: #Red
        Bar = Back.RESET + Fore.WHITE + '[' + Back.RED + (Yes * f' ') + Back.RESET + (No * ' ') + Fore.WHITE + ']'
    print(f'')

    with open('Happy Meter.txt', 'r', encoding="utf8") as screen:
        for lines in screen:
            print('     ' + Fore.GREEN + lines, end='')
            time.sleep(0.1)
    print(f'\n')
    print()
    print('                 ' + Bar + f' ' + str(percent) + '%')
    print()

def win(Name, place, percent):
    
    for n in range (30,0,-1):

        print(Fore.RED + f'')
        print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
        print(n*'\n')
        with open('Election Mania.txt', 'r') as screen:
            for lines in screen:
                print('                          ' +Fore.WHITE + lines, end='' + Back.RESET)
        print(Fore.RED + f'')
        print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
        time.sleep(0.15)
        os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    with open('Election Mania.txt', 'r') as screen:
        for lines in screen:
            print('                          ' +Fore.WHITE + lines, end='' + Back.RESET)
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print()
    meter(percent)
    time.sleep(2)
    with open('Cynthia.txt', 'r') as screen:
        for lines in screen:
            print('       ' +Fore.WHITE + lines, end='' + Back.RESET)
            time.sleep(0.1)
    print(Fore.CYAN)
    text('  ' + Name + f', We won in the re-election. We will govern for another term.\n')
    text( f'  The people of '+ place +f' really loved our initiatives that were in line with the environmental enthusiasts.\n')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print()
    time.sleep(2)
    input(Fore.YELLOW + f'  Press Enter to continue...')

def lose(Name, place, percent):
    for n in range (30,0,-1):

        print(Fore.RED + f'')
        print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
        print(n*'\n')
        with open('Election Mania.txt', 'r') as screen:
            for lines in screen:
                print('                          ' +Fore.WHITE + lines, end='' + Back.RESET)
        print(Fore.RED + f'')
        print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
        time.sleep(0.15)
        os.system('cls')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    with open('Election Mania.txt', 'r') as screen:
        for lines in screen:
            print('                          ' +Fore.WHITE + lines, end='' + Back.RESET)
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print()
    meter(percent)
    time.sleep(2)
    with open('Marlo.txt', 'r') as screen:
        for lines in screen:
            print('                       ' +Fore.WHITE + lines, end='' + Back.RESET)
            time.sleep(0.1)
    print(Fore.CYAN)
    text(f'  I am Marlo, i won the election.\n')
    text(f'  I will be the new mayor of ' + place +'.\n')
    text(f'  Your orthodox ideas and greed for money are degradable for environment.\n')
    text(f'  You stood no chance in front of me.\n')
    text(f'  I was well informed about light pollution in this area and pollution in general. You better go and read about it '+ Name +'.\n')
    print(Fore.RED + f'')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print()
    time.sleep(2)
    input(Fore.YELLOW + f'  Press Enter to continue...')



def Game_End():
    Style.RESET_ALL
    os.system('cls')
    print(Fore.RED + '')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')
    print(f' <+>                                             ' + Fore.YELLOW + f'The Game has Ended' + Fore.RED + f'                                                   <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                           ' + Fore.YELLOW + f'Choose what to do next.' + Fore.RED + f'                                                <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'- Home -' + Fore.RED + f'                                                        <+>\n')
    print(f' <+>                                                 ' + Fore.MAGENTA + f'- Replay -' + Fore.RED + f'                                                       <+>\n')
    print(f' <+>                                                  ' + Fore.MAGENTA + f'- Quit -' + Fore.RED + f'                                                        <+>\n')
    print(f' <+>                                                                                                                  <+>\n')
    print(f' <+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n')

    game_end_selection()

def game_end_selection():
    print(Fore.GREEN + '')
    option = input(f'> ')
    if option.lower() == ("home"):
        title_screen()
    elif option.lower() == ("replay"):
        start_game()
    elif option.lower() == ("quit"):
        sys.exit()
    else:
        while option.lower not in ['help', 'replay', 'quit']:
            print(Fore.RED + f'  Please enter a valid response')
            option = input(Fore.GREEN + f'> ')
            if option.lower() == ("home"):
                title_screen()
            elif option.lower() == ("replay"):
                start_game()
            elif option.lower() == ("quit"):
                sys.exit()


''' Sampling and debugging '''


title_screen()


''' NOTES '''
