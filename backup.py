import os
import time
import random
from termcolor import colored, cprint 


# SETTING
standart_directory = '/home/'
save_directory = '/home/$USER'
colors = ('green', 'red', 'cyan', 'magenta', 'yellow')


def local_time():
    return time.asctime().replace(' ', '_')


def searh_files(*args):
    lst_search_output = [[] for _ in range(len(args[0]))]
    for root, dirs, files in os.walk(standart_directory):
        dirs_and_files = dirs + files
        for d_or_f in dirs_and_files:
            for i, search_obj in enumerate(args[0]):
                if d_or_f == search_obj:
                    if search_obj in dirs_and_files:
                        lst_search_output[i].append(f"{root}/{d_or_f}")
    true_lst_search_output = []
    for i,j in enumerate(lst_search_output):
        if bool(lst_search_output[i]):
            true_lst_search_output.append(j)
    return true_lst_search_output


def create_zip(lst_files, save_directory):
    name_zip = local_time()
    for rootall in lst_files:
        for j, root in enumerate(rootall):
            os.system(f"zip -r -u {name_zip}.zip {root[:root.rfind('/')]} . -i \
                        *{root[root.rfind('/')+1:]}*")
    os.system(f"mv {name_zip}.zip {save_directory};cd {save_directory};clear; \
                        zip -sf {name_zip}.zip")


def settings(standart_directory, save_directory):
    while True:
        print(
            f"Current directory:\nSearch :{standart_directory}\nSave: {save_directory}")
        try:
            choice_settings = int(input(colored(
                f"1. Change search directory\n2. Change backup directory\n3. Back to main menu\n", 'green')))
            if choice_settings == 1:
                standart_directory = input('Enter new search directory')
                if standart_directory[0] == '/':
                    return standart_directory, save_directory
            elif choice_settings == 2:
                save_directory = input('Enter new save directory')
                if save_directory[0] == '/':
                    return standart_directory, save_directory
            elif choice_settings == 3:
                return standart_directory, save_directory
        except ValueError:
            continue


def menu(standart_directory, save_directory):
    while True:
        top, mid, bot = f"|{'='*14}|\n|=...", "BACKUP", f"...=|\n|{'='*14}|"
        print(
            f"{colored(top, 'red')}{colored(mid, 'white', attrs=['bold'])}{colored(bot, 'red')}")
        choice = input(
            "Press Enter to continue or '-s' to go to settings, 'q' for exit.")
        if choice == '-s':
            standart_directory, save_directory = settings(
                standart_directory, save_directory)
        elif choice == 'q':
            break
        else:
            search_obj = input('Enter backup file/s: ')
            lst_search_output = searh_files(search_obj.split())
            print(
                f"Find {len(lst_search_output)} coincidence. Select files for backup:\n")
            lst_files = [[] for _ in range(len(lst_search_output))]
            for j, y in enumerate(lst_search_output):
                rc = random.randint(0,4)
                cprint(f"{'='*45}", colors[rc], attrs=['bold'])
                for i, x in enumerate(y):
                    cprint(f"[{i}]{x}", colors[rc], attrs=['bold'])
                choice_files = input(colored(
                    f"{'='*45}\nCoincidence:{j+1}/{len(lst_search_output)}\nChoice need files, enter number/s together: ", 
                    colors[rc], attrs=['bold']))
                for c_file in choice_files:
                    lst_files[j].append(lst_search_output[j][int(c_file)])
            create_zip(lst_files, save_directory)


menu(standart_directory, save_directory)
