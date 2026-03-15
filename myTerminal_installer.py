
import os

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

def main():
    os.chdir(f"C:\\Users\\{os.getlogin()}")
    print(f"{COLOR_GREEN}[INFO]{RESET} Creating `mt_data.txt`...\n{COLOR_GREEN}[INFO]{RESET} Creating `mt_datadollarsign.txt`...\n{COLOR_GREEN}[INFO]{RESET} Creating `mt_userinputfield.txt`...")
    try:
        with open("mt_data.txt", "a+") as file:
            pass
        with open("mt_datadollarsign.txt", "a+") as file:
            pass
        with open("mt_userinputfield.txt", "a+") as file:
            pass
        
        print("Installation successful. You can close this window and run myTerminal.py")
        print("Press ENTER to continue...")
        input()
    except PermissionError:
        print(f"{COLOR_RED}[ERROR]{RESET} Couldn't install assets; insufficient permission.\n")
        input()
        input()
        quit()


if __name__ == "__main__":
    main()