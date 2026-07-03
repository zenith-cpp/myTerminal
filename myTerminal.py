from tkinter import *
import os
import shutil
import textwrap
import time
import sys
import socket

COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_BLUE = "\033[34m"
COLOR_PINK = "\033[95m"
COLOR_MAGENTA = "\033[35m"
COLOR_BLACK = "\033[30m"
COLOR_WHITE_STRONG = "\033[97m"
COLOR_WHITE = "\033[37m"
COLOR_YELLOW = "\033[33m"

BACKGROUND_COLOR_GREEN = "\033[42m"


RESET = "\033[0m"
BOLD = "\033[1m"

# check for flags
if len(sys.argv) > 1:
    if sys.argv[1] == "--version":
        print("version 1.1.0")
        quit()
    elif sys.argv[1] == "--about":
        print("This is an open source CLI project made simply for fun by Yikebones.\n")
        quit()
    else:
        print(f"{COLOR_GREEN}--version{RESET}: displays the version of myTerminal.")
        print(f"{COLOR_GREEN}--about{RESET}  : displays information about myTerminal.")
else:
    pass
user_pref_if = "" # `if` is short for `input field` in this case
user_pref_input = ""
user_pref_ds = ""
user_pref_if_template = 1
color_dict = {
    "GREEN": COLOR_GREEN,
    "BLUE": COLOR_BLUE,
    "RED": COLOR_RED,
    "PINK": COLOR_PINK,
    "MAGENTA": COLOR_MAGENTA,
    "GRAY": COLOR_BLACK,
    "WHITE": COLOR_WHITE_STRONG
}




os.chdir(f"C:\\Users\\{os.getlogin()}")
# input field (color)
try:
    with open("mt_data.txt", "r+") as file:
        lines = file.readlines()
        if lines:
            if lines[0].strip() in color_dict:
                user_pref_input = color_dict[lines[0].strip()]
            else:
                user_pref_input = COLOR_BLUE
        else:
            file.write("BLUE")
            user_pref_input = COLOR_BLUE
except FileNotFoundError:
    with open("mt_data.txt", "a+") as file:
        file.write("BLUE")
        user_pref_input = COLOR_BLUE
# dollar sign
try:
    with open("mt_datadollarsign.txt", "r+") as file:
        lines = file.readlines()
        if lines:
            if lines[0].strip() in color_dict:
                user_pref_ds = color_dict[lines[0].strip()]
            else:
                user_pref_ds = COLOR_RED
        else:
            user_pref_ds = COLOR_RED
            file.write("RED")
except FileNotFoundError:
    with open("mt_datadollarsign.txt", "a+") as file:
        file.write("RED")
    user_pref_ds = COLOR_RED



try:
    from tkinter import *
except ModuleNotFoundError:
    print(f"{COLOR_GREEN}Installing Module {BOLD}TKINTER{RESET}")
    os.system("pip install tkinter")


installation_path = ""
def get_user_pref_if():
    working_directory = os.getcwd().replace("\\", "/")
    userPrefDict = {
        1: f"MT {user_pref_input}{BOLD}{working_directory}\\n\\t\\t┕━━━━━━━━{RESET}{user_pref_ds}${RESET}",
        2: f"MT {user_pref_input}{BOLD}{working_directory}{RESET}{user_pref_ds}>{RESET}",
        3: f"MT {user_pref_input}{BOLD}{working_directory}{RESET}{user_pref_ds}~${RESET}",
        4: f"MT ╭─ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET}\\n   ╰─ {user_pref_ds}${RESET}",
        5: f"MT ┌─[{user_pref_input}{BOLD}{working_directory}{RESET}]\\n   └─ {user_pref_ds}${RESET}",
        6: f"MT [ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET} {user_pref_input}{BOLD}{working_directory}{RESET} ] {user_pref_ds}${RESET}",
        7: f"MT < {user_pref_input}{os.getlogin()}{RESET}@{user_pref_input}{BOLD}{working_directory}{RESET} > {user_pref_ds}${RESET}"
    }
    return userPrefDict[user_pref_if_template]


def rmdir_process():
    filename = command[6:].replace('"', "")
    if len(filename) <= 0:
        print(f"{COLOR_BLUE}Usage:{RESET} rmdir [DIRNAME]\n\n")
    try:
        if os.path.isdir(filename):
            os.rmdir(filename)
        else:
            print(f"Please enter a {COLOR_RED}directory{RESET} path. Incase of files, use '{COLOR_GREEN}rm{RESET}'\n\n")

    except FileNotFoundError:
        print(f"File {COLOR_RED}{filename}{RESET} doesn't exist.\n\n")

    except OSError:
        try:
            shutil.rmtree(filename)
            print(f"Directory `{filename}` was successfully {COLOR_GREEN}removed{RESET}.\n\n")
        except PermissionError:
            print(f"Cannot remove given folder: Insufficient permission.\n\n")
        except OSError as e:
            print(f"Can't remove given folder: {e}")
    except PermissionError:
        print(f"Couldn't remove `{filename}`: Insufficient Permission.\n\n")



def listdir_process():
    try:
        folders_with_dots = []
        files_with_dots = []
        folders = []
        files = []
        if len(os.listdir()) > 0:
            for i in os.listdir():
                if os.path.isdir(i):
                    if i.startswith("."):
                        folders_with_dots.append(i)
                    else:
                        folders.append(i)
                else:
                    if i.startswith("."):
                        files_with_dots.append(i)
                    else:
                        files.append(i)
            if files_with_dots:
                for i in files_with_dots:
                    _, ext = os.path.splitext(i)
                    if ext:
                        print(f"[{ext.replace(".", "").upper()}] {COLOR_GREEN}{i}{RESET}")
                    else:
                        print(f"[FILE] {COLOR_GREEN}{i}{RESET}")
            if folders_with_dots:
                for i in folders_with_dots:
                    print(f"{BACKGROUND_COLOR_GREEN}{COLOR_BLACK}[FOLDER]{RESET} {COLOR_BLUE}{i}{RESET}")

            if folders:
                for i in folders:
                    print(f"{BACKGROUND_COLOR_GREEN}{COLOR_BLACK}[FOLDER]{RESET} {COLOR_BLUE}{i}{RESET}")
            
            if files:
                for i in files:
                    _, ext = os.path.splitext(i)
                    if ext:
                        print(f"[{ext.replace(".", "").upper()}] {COLOR_GREEN}{i}{RESET}")
                    else:
                        print(f"[FILE] {COLOR_GREEN}{i}{RESET}")
        else:
            print(f"\n\t\tThis directory is {COLOR_RED}empty{RESET}.\n\n")
    except PermissionError:
        print(f"Can't list the contents of {os.getcwd()}: Insufficient Permission.\n\n")

def clear():
    print("\033[H\033[J", end="")



try:
    with open("mt_userinputfield.txt", "r+") as file:
        lines = file.readlines()
        if lines:
            user_pref_if_template = int(lines[0].strip())
        else:
            file.write("1")
            user_pref_if_template = 1 # default fallback
except FileNotFoundError:
    with open("mt_userprefinput.txt", "a+") as file:
        file.write("1")
    user_pref_if_template = 1
except ValueError:
    print("Value error occured, setting user_pref_if_template to 1")
    user_pref_if_template = 1

os.system("cls") # enables ansi color codes (CRUCIAL)
try:
    print("Welcome to myTerminal.")
    print("Made by Yikebones, 2025. Use the source code however you want, just give credits.")
    command = 0
    os.chdir(f"C:\\Users\\{os.getlogin()}") # I know it was already done, but just in case yk
    while command != exit:
        # User input (looped)
        
        working_directory = os.getcwd()
        user_pref_if = get_user_pref_if().replace("\\n", "\n").replace("\\t", "\t").replace("zaworkdir", working_directory)
        command = input(f"{user_pref_if} ")
        if command.lower() in ['cls', 'clear']:
            print("\033[H\033[J", end="")

        elif command.lower() == "seeColor":
            print(f"{user_pref_input}user pref input {RESET}")
            print(f"{user_pref_ds} user pref ds {RESET}\n\n")

        elif command.lower() == "help":
            print(textwrap.dedent(
                f"""\
                Commands:
                {COLOR_GREEN}ls{RESET} - List everything in your current directory
                {COLOR_RED}OPTIONAL{RESET} {COLOR_GREEN}ls{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - List everything in the given directory.
                {COLOR_GREEN}print-txt{RESET} {COLOR_BLUE}[TEXT]{RESET} - Prints the text you put after the command.
                {COLOR_GREEN}clear{RESET}, {COLOR_GREEN}cls{RESET} - Clears the terminal
                {COLOR_GREEN}exit{RESET} - Terminates the program
                {COLOR_GREEN}touch{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Creates a file with the specified filename
                {COLOR_GREEN}cat{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Views file content (won’t work on directories)
                {COLOR_GREEN}more{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Same as {COLOR_RED}cat{RESET}
                {COLOR_GREEN}cd{RESET} {COLOR_BLUE}[PATH]{RESET} or {COLOR_BLUE}..{RESET} - Changes directory to the given path (`cd ..` goes back)
                {COLOR_GREEN}rm{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Removes a file
                {COLOR_GREEN}rmdir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - Removes a directory
                {COLOR_GREEN}mkdir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - Creates a directory
                {COLOR_GREEN}about myTerminal{RESET} - Displays information about the terminal.
                {COLOR_GREEN}setcolor{RESET} - Displays a menu where you can customize the color of different parts in the input field
                {COLOR_GREEN}sif{RESET} - Stands for `{COLOR_BLACK}set input field{RESET}`, displays a menu where you can customize the input field.
                \n\n
            """))

        elif command.lower().strip().startswith("ls"):  #! LS COMMAND AND ITS ALGORITHM
            dirname = command[3:].strip().lower()
            mess = dirname.replace(dirname[7:].replace('"', ""), "") # this basically gets the --find part ._.
            # check if `dirname` is not actually the command `find` e.g. `ls --find`
            if mess.strip() != '--find' or mess.strip() != '--find ""':
                if len(dirname) > 0:
                    try:
                        org_wd = os.getcwd()
                        os.chdir(dirname)
                        listdir_process()
                        os.chdir(org_wd) # change back to the original directory once it is done
                    except PermissionError:
                        print(f"Can't access `{dirname}`: Insufficient Permission.\n\n")
                    except FileNotFoundError:
                        print(f"Directory `{COLOR_BLACK}{dirname}{RESET}` not found.\n\n")
                    except NotADirectoryError:
                        print(f"{COLOR_RED}Error{RESET}: {COLOR_BLUE}ls{RESET} can't scan files, only folders.")
                        print(f"{COLOR_GREEN}[NOTE]{RESET} For that purpose, use {COLOR_BLUE}`cat`{RESET} or {COLOR_BLUE}`more`{RESET}.\n\n")
                    except OSError:
                        dirname = dirname.replace('"', "")
                        temp_var = os.getcwd()
                        os.chdir(dirname) # new dirname
                        listdir_process()
                        os.chdir(temp_var)
                else:
                    listdir_process()
            else:
                # this statement triggers when the 'dirname' is actually "| find". Now we need to get the name of the directory it is actually trying to find.
                try:
                    lf_dirname = dirname[7:].replace('"', "").strip() # this will get the folder name
                    file = os.listdir()
                    for i in file:
                        if i == lf_dirname:
                            print(f"{COLOR_RED}{lf_dirname}{RESET}")
                            break
                except OSError as e:
                    print("OSERROR occured while trying to run this code; it's unclear why.")
                    print("Original Error:", e)

        elif command.lower().strip().startswith("print-txt"):
            text_to_print = command[10:]
            print(f"{text_to_print}\n\n")

        elif command.lower() == 'pwd':
            print(f"{working_directory}\n\n")

        elif command.lower() == 'exit':
            quit()

        elif command.lower().strip().startswith('touch'):
            filename = command[len('touch '):]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} touch [FILENAME]\n")
            else:
                with open(filename.replace('"', ""), "a+") as file:
                    pass
                print(f"File '{COLOR_GREEN}{filename}{RESET}' was created successfully.\n")

        elif command.lower().strip().startswith('rm'):
            if command.strip().startswith('rmdir') == False:
                filename = command[3:].replace('"', "")
                try:
                    if len(filename) <= 0:
                        print(f"{COLOR_BLUE}Usage:{RESET} rm [FILENAME]\n")
                    else:
                        os.remove(filename)
                        print(f"File '{COLOR_RED}{filename}{RESET}' was removed successfully.\n")

                except FileNotFoundError:
                    print(f"'{filename}' {COLOR_RED}was not{RESET} found.\n")
                except IsADirectoryError:
                    ans = input("The given filename is a directory. Do you wanna remove it?(y/n) ")
                    if ans.lower() == 'y':
                        os.rmdir(filename)
                        print(f"Directory '{COLOR_RED}{filename}{RESET}' was removed successfully.\n")
                    else:
                        print()
            elif command.strip().startswith("rmdir"):
                rmdir_process()

        elif command.lower().strip().startswith('more'):
            filename = command[5:].strip().replace('"', "")
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} more [FILENAME]\n")
            else:
                try:
                    with open(filename, "r+", encoding="utf-8") as f:
                        for i in f.readlines():
                            print(i, end='')
                except IsADirectoryError:
                    print(f'The command {COLOR_BLUE}"more"{RESET} cannot scan directories. Maybe try {COLOR_RED}ls -dir [DIRNAME]{RESET}.\n\n')
                except FileNotFoundError:
                    print(f"'{filename}' {COLOR_RED}was not{RESET} found.\n\n")
                except (UnicodeEncodeError, UnicodeDecodeError):
                    print(f"There was an issue trying to encode or decode the given file. This error can happen when you attempt to use this command on a .exe file, or other files like this. (encoding: utf-8)\n\n")

        elif command.lower().strip().startswith("cat"):
            filename = command[4:].strip().replace('"', "")
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} cat [FILENAME]\n")
            else:
                if os.path.isdir(filename) == False:
                    try:
                        with open(filename, "r", encoding="utf-8") as f:
                            for i in f.readlines():
                                print(i, end='')
                    except PermissionError:
                        print(f"Access {COLOR_RED}Denied{RESET}.\n\n")
                    except FileNotFoundError:
                        print(f"File `{COLOR_GREEN}{filename}{RESET}` doesn't exist.\n\n")
                    except (UnicodeEncodeError, UnicodeDecodeError):
                        print(f"There was an issue trying to encode or decode the given file. This error can happen when you attempt to use this command on a .exe file, or other files like this. (encoding: utf-8)\n\n")


                else:
                    print(f'The command {COLOR_BLUE}"cat"{RESET} cannot scan directories. Maybe try {COLOR_RED}ls -dir [DIRNAME]{RESET}.\n\n')

        elif command.lower().strip().startswith("mkdir"):
            dirname = command[6:].replace('"', "")
            if len(dirname) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} mkdir [DIRNAME]\n\n")
            else:
                os.makedirs(dirname, exist_ok=True)
                print(f"Directory was made {COLOR_GREEN}successfully{RESET}.\n\n")


        elif command.lower().strip().startswith("cd"):
            path = command[3:].strip().replace('"', "")

            if path == "":
                print(f"{COLOR_BLUE}Usage:{RESET} cd [PATH] or '..' to go back.\n\n")
            else:
                if path != "..":
                    try:
                        os.chdir(path)
                        print()
                    except FileNotFoundError:
                        print(f"Path {COLOR_RED}{path}{RESET} doesn't exist.\n\n")
                    except NotADirectoryError:
                        print(f"Path {COLOR_RED}{path}{RESET} is not a directory.\n\n")
                    except OSError:
                        new_path = path.replace('"', "")
                        os.chdir(new_path)
                    except PermissionError:
                        print(f"Can't warp into {COLOR_RED}{path}{RESET}: Insufficient Permission.\n\n")
                elif path == "..":
                    try:
                        os.chdir(path)
                        print()
                    except OSError:
                        print("Can't go back any further.\n\n")

        elif command.lower() == "about myterminal":
            print(textwrap.dedent(
                f"""\
                {COLOR_GREEN}myTerminal{RESET} was made by {COLOR_BLUE}Yikebones{RESET}.
                This project was created to {BOLD}practice my programming skills{RESET}.
                {COLOR_GREEN} Yes, you can use the source code however you'd like, just give credits.{RESET}
                The code is a little messy, I admit, but I'll try to work on that in the future.
            """))

        # customization part (user freewill)
        elif command.lower() == "setcolor":
            def check(var1, var2):
                if var1 == var2:
                    return True
                else:
                    return False

            while True:  # nested while loops
                clear()
                print(textwrap.dedent(
                    """\
                    Welcome to the design settings!
                    Tell me, which part of the terminal's color do you want to customize?
                    1. Command Input
                    2. Dollarsign Customization
                """))
                ans = input("Enter a number, or 'exit' to quit: ")
                if ans == '1':
                    # Color dictionary, numbers are "keys" and the values are tuples with a string and color code
                    color_options = { # rpd, you can use a dictionary
                        "1": ("GREEN", COLOR_GREEN),
                        "2": ("BLUE", COLOR_BLUE),
                        "3": ("RED", COLOR_RED),
                        "4": ("PINK", COLOR_PINK),
                        "5": ("WHITE", COLOR_WHITE_STRONG),
                        "6": ("GRAY", COLOR_BLACK)
                    }
                    colorCommand = "" # value is the key in the dictionary
                    selected_color_name = "" # value from the color name portion of the dictionary
                    while colorCommand != "back":  # if color command is equals to "back", break the loop
                        clear()


                        # Build the dynamic color menu from the dictionary
                        current_if = get_user_pref_if().replace("\\n", "\n").replace("\\t", "\t")
                        menu = f"{current_if}\n"
                        menu += "Options:\n"
                        for key, (name, color) in color_options.items():
                            menu += f"  {key}. {name.capitalize()}{RESET}\n" # .capitalize() just capitilizes the first char in the string, rest are lowercase
                            # menu += f"  {key}. {color}{name.capitalize()}{RESET}\n" # if you want the text to be those colors too (magenta doesn't show for some reason)
                        menu += "  Type 'back' or 'done' to finish.\n"
                        print(menu)

                        colorCommand = input(
                            "Your preference (in nums): "
                        )
                        if colorCommand.lower() == "done":
                            if selected_color_name:
                                temp_var = os.getcwd()
                                os.chdir(f"C:\\Users\\{os.getlogin()}")
                                try:
                                    with open("mt_data.txt", "w") as file:
                                        file.write(selected_color_name.strip())
                                    print(f"Color {selected_color_name} saved successfully!")
                                    time.sleep(1)
                                except Exception as e:
                                    print(f"Error saving color: {e}")
                                    time.sleep(2)
                                os.chdir(temp_var)
                            break

                        elif colorCommand in color_options:
                            name, value = color_options[colorCommand]
                            if check(user_pref_input, value):
                                print("You already have that selected.\n")
                                time.sleep(2)
                            else:
                                user_pref_input = value
                                selected_color_name = name
                                print(f"{value}Color {name}{RESET} is successfully set.")
                                time.sleep(2)
                        elif colorCommand.lower() == "back":
                            break
                        else:
                            print("Invalid option. Please choose a valid number or type 'back'.")
                            time.sleep(2)
                        
                elif ans == '2':
                    color_options = { # rpd, you can use a dictionary
                        "1": ("GREEN", COLOR_GREEN),
                        "2": ("BLUE", COLOR_BLUE),
                        "3": ("RED", COLOR_RED),
                        "4": ("PINK", COLOR_PINK),
                        "5": ("WHITE", COLOR_WHITE_STRONG),
                        "6": ("GRAY", COLOR_BLACK)
                    }
                    colorCommand = "" # value is the key in the dictionary
                    selected_color_name = "" # value from the color name portion of the dictionary
                    while colorCommand != "back":  # if color command is equals to "back", break the loop
                        clear()


                        # Build the dynamic color menu from the dictionary
                        current_if = get_user_pref_if().replace("\\n", "\n").replace("\\t", "\t")
                        menu = f"{current_if}\n"
                        menu += "Options:\n"
                        for key, (name, color) in color_options.items():
                            menu += f"  {key}. {name.capitalize()}{RESET}\n" # .capitalize() just capitilizes the first char in the string, rest are lowercase
                            # menu += f"  {key}. {color}{name.capitalize()}{RESET}\n" # if you want the text to be those colors too (magenta doesn't show for some reason)
                        menu += "  Type 'back' or 'done' to finish.\n"
                        print(menu)

                        colorCommand = input("Your preference (in nums): ")
                        
                        
                        if colorCommand.lower() == "done":
                            if selected_color_name:
                                temp_var = os.getcwd()
                                os.chdir(f"C:\\Users\\{os.getlogin()}")
                                try:
                                    with open("mt_datadollarsign.txt", "w") as file:
                                        file.write(selected_color_name)
                                    print(f"Dollar sign color {selected_color_name} saved successfully!")
                                    time.sleep(1)
                                except Exception as e:
                                    print(f"Error saving color: {e}")
                                    time.sleep(2)
                                os.chdir(temp_var)
                            break


                        elif colorCommand in color_options:
                            name, value = color_options[colorCommand]
                            if check(user_pref_ds, value):
                                print("You already have that selected.\n")
                                time.sleep(2)
                            else:
                                user_pref_ds = value
                                selected_color_name = name
                                print(f"{value}Color {name}{RESET} is successfully set.")
                                time.sleep(2)
                        elif colorCommand.lower() == "back":
                            break
                        else:
                            print("Invalid option. Please choose a valid number or type 'back'.")
                            time.sleep(2)
                elif ans == 'exit':
                    break

                else:
                    print("invalid option.")
                    input()
        elif len(command) == 0:
            pass # if the string is empty; don't do anything
        elif command.lower() == "sif":
            
            while True:
                print(f"""
                1. MT {user_pref_input}{BOLD}{working_directory}\n\t\t\t┕━━━━━━━━{RESET}{user_pref_ds}${RESET} - {COLOR_BLUE}Kali Linux{RESET} inspired design
                2. MT {user_pref_input}{BOLD}{working_directory}{RESET}{user_pref_ds}>{RESET} - Classic Terminal
                3. MT {user_pref_input}{BOLD}{working_directory}{RESET}{user_pref_ds}~${RESET} - Classic Linux
                
                -- BOX-LIKE DESIGNS --

                4. MT ╭─ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET}
                      ╰─ {user_pref_ds}${RESET}
                
                5. MT ┌─[{user_pref_input}{BOLD}{working_directory}{RESET}]
                      └─ {user_pref_ds}${RESET}

                6. MT [ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET} {user_pref_input}{BOLD}{working_directory}{RESET} ] {user_pref_ds}${RESET}
                7. MT < {user_pref_input}{os.getlogin()}{RESET}@{user_pref_input}{BOLD}{working_directory}{RESET} > {user_pref_ds}${RESET}
                """)
                userinp = int(input("\nType the number 8 to exit\n> "))
                if userinp in [1, 2, 3, 4, 5, 6, 7]:
                    thing_to_write = ""
                    with open(f"C:\\Users\\{os.getlogin()}\\mt_userinputfield.txt", "a+", encoding="utf-8") as file:
                        file.seek(0)
                        lines = file.readlines()
                        if lines:
                            file.truncate(0)
                        thing_to_write = str(userinp)
                        file.write(thing_to_write)
                    print(f"Successfully applied number {COLOR_GREEN}{thing_to_write}{RESET}.\n\n")
                    break
                elif userinp == 8:
                    clear()
                    break
                else:
                    print("Invalid Option, Try again.")
                    break
        elif command.lower().strip().startswith("./"):
            exec_name = command[2:]
            if exec_name:
                kewl = command.replace("/", "\\")
                if shutil.which(kewl):
                    os.system(kewl)
                else:
                    print(f"Executable `{COLOR_RED}{exec_name}{RESET}` was not found.\n\n")

        else:
            cmd = command.split()[0]
            if shutil.which(cmd):
                os.system(command)
            else:
                print(f'"{COLOR_RED}{command}{RESET}" is not a valid command. If you\'re stuck, please type in {COLOR_GREEN}"help"{RESET}\n\n')

except FileNotFoundError:
    print(f"{COLOR_RED}Please run `python myTerminal_installer.py` or doubleclick the myTerminal_intaller.py file before continuing.{RESET}")

except KeyboardInterrupt:
    print("CTRL + C is faster i guess. I hope youll be back :D")
