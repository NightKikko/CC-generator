import re
import random
from colorama import Fore, Style, init
import socket
import os
import platform
import threading

# Initialisation de colorama
init(autoreset=True)

class Color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

def validate_credit_card(number):
    """Applique l'algorithme de Luhn pour valider le numéro de carte."""
    number = str(number)
    total = 0
    reverse_digits = number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    return total % 10 == 0

def generate_credit_card_number():
    """Génère un numéro de carte de crédit valide."""
    number = [random.randint(0, 9) for _ in range(15)]
    checksum = sum((number[i] * 2 if i % 2 == 1 else number[i]) for i in range(15))
    checksum = (10 - (checksum % 10)) % 10
    number.append(checksum)
    return ''.join(map(str, number))

def clear_screen():
    """Efface l'écran de la console."""
    os_name = platform.system()
    if os_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def export_to_txt(card_numbers):
    """Exporte les numéros de carte dans un fichier texte."""
    with open('generated_credit_cards.txt', 'w') as f:
        for card_number in card_numbers:
            f.write(f"{card_number}\n")
    print(f"{Color.GREEN}[+] {Color.WHITE}Les numéros de carte ont été exportés dans 'generated_credit_cards.txt'.{Color.RESET}")

def validate_and_print(card_number):
    """Valide le numéro de carte et affiche le résultat."""
    is_valid = validate_credit_card(card_number)
    status = Color.GREEN + "Valide" + Color.RESET if is_valid else Color.RED + "Invalide" + Color.RESET
    print(f"{Color.GREEN}[+] {Color.WHITE}Numéro de carte : {card_number} est {status}{Color.RESET}")

def main():
    pc_name = socket.gethostname()

    while True:
        clear_screen()
        print(Color.RED + '''
 ▄████▄   ▄▄▄       ██▀███  ▓█████▄     ██▒   █▓ ▄▄▄       ██▓     ██▓▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌   ▓██░   █▒▒████▄    ▓██▒    ▓██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌    ▓██  █▒░▒██  ▀█▄  ▒██░    ▒██▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌     ▒██ █░░░██▄▄▄▄██ ▒██░    ░██░░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓       ▒▀█░   ▓█   ▓██▒░██████▒░██░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒       ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░░▓   ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒       ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░          ░   ▒     ░░   ░  ░ ░  ░         ░░    ░   ▒     ░ ░    ▒ ░ ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
░ ░            ░  ░   ░        ░             ░        ░  ░    ░  ░ ░     ░          ░  ░            ░ ░     ░     
░                            ░              ░                          ░                                                  

''' + Color.WHITE + "Fully coded by oto.dev, forked by NightKikko" + Color.RESET)
        
        print(f"{Color.RED}[{Color.RESET}1{Color.RED}]{Color.RESET} Vérifier plusieurs cartes")
        print(f"{Color.RED}[{Color.RESET}2{Color.RED}]{Color.RESET} Vérifier une seule carte")
        print(f"{Color.RED}[{Color.RESET}3{Color.RED}]{Color.RESET} Générer des numéros de carte aléatoires")
        choice = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Choisissez une option : ").strip()
        
        if choice == '1':
            while True:
                card_numbers = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Veuillez entrer les numéros de carte séparés par des virgules : {Color.RESET}").strip()
                card_numbers = [number.strip() for number in card_numbers.split(',')]
                
                if not all(re.match(r'^\d+$', number) for number in card_numbers):
                    print(f"{Color.RED}[!] {Color.WHITE}Erreur : Tous les numéros de carte doivent contenir uniquement des chiffres.{Color.RESET}")
                    input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Appuyez sur ENTER pour continuer...{Color.RESET}")
                    clear_screen()
                    continue
                
                threads = []
                for card_number in card_numbers:
                    thread = threading.Thread(target=validate_and_print, args=(card_number,))
                    threads.append(thread)
                    thread.start()
                
                for thread in threads:
                    thread.join()
                break
        
        elif choice == '2':
            while True:
                card_number = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Veuillez entrer le numéro de carte de crédit : {Color.RESET}").strip()
                
                if not re.match(r'^\d+$', card_number):
                    print(f"{Color.RED}[!] {Color.WHITE}Erreur : Le numéro de carte doit contenir uniquement des chiffres.{Color.RESET}")
                    input(f"{Color.GREEN}┌───({Color.RESET}{pc_name}{Color.GREEN})\n└──$ {Color.RESET}Appuyez sur ENTER pour continuer...{Color.RESET}")
                    clear_screen()
                    continue
                
                validate_and_print(card_number)
                break

        elif choice == '3':
            while True:
                try:
                    count = int(input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Combien de numéros de carte souhaitez-vous générer ? : {Color.RESET}"))
                    if count <= 0:
                        print(f"{Color.RED}[!] {Color.WHITE}Erreur : Veuillez entrer un nombre positif.{Color.RESET}")
                        continue
                except ValueError:
                    print(f"{Color.RED}[!] {Color.WHITE}Erreur : Veuillez entrer un nombre valide.{Color.RESET}")
                    continue

                card_numbers = []
                for _ in range(count):
                    card_number = generate_credit_card_number()
                    card_numbers.append(card_number)
                    print(f"{Color.GREEN}[+] {Color.WHITE}Numéro de carte généré : {card_number}{Color.RESET}")
                
                export_choice = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Voulez-vous exporter les numéros générés dans un fichier texte ? (y/n) : {Color.RESET}").strip().lower()
                if export_choice == 'y':
                    export_to_txt(card_numbers)

                validate_export = input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Voulez-vous vérifier les numéros générés ? (y/n) : {Color.RESET}").strip().lower()
                if validate_export == 'y':
                    threads = []
                    for card_number in card_numbers:
                        thread = threading.Thread(target=validate_and_print, args=(card_number,))
                        threads.append(thread)
                        thread.start()
                    
                    for thread in threads:
                        thread.join()
                break
        
        else:
            print(f"{Color.RED}[!] {Color.WHITE}Choix invalide. Veuillez sélectionner 1, 2 ou 3.{Color.RESET}")
            input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Appuyez sur ENTER pour continuer...{Color.RESET}")
            clear_screen()
            continue
        
        break

    input(f"{Color.RED}┌───({Color.RESET}{pc_name}{Color.RED})\n└──$ {Color.RESET}Appuyez sur ENTER pour quitter...{Color.RESET}")

if __name__ == '__main__':
    main()
