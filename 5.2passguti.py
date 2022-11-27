import random
import pyperclip

def lingua_en():
    #inizio della lingua inglese
    print("==========================================")
    print("    Welcome to my password generator!    ")
    print("==========================================")
    print()
    print('''choose your password difficult: Easy, Medium, Difficult...''')
    choose_pass = input()
    lunghezza = int(input("Choose your password lenght: "))

    if choose_pass == "Easy":
        password = ""
        caratteri_easy = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_easy)
        print("this is yuor easy password: " + password)
        print()
        print("Password already copied!")
        pyperclip.copy(password)
    elif choose_pass == "easy":
        password = ""
        caratteri_easy = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_easy)
        print("this is yuor easy password: " + password)
        print()
        print("Password already copied!")
        pyperclip.copy(password)
    if choose_pass == "Medium":
        password = ""
        caratteri_med = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_med)
        print("this is your medium password: " + password)
        print()
        print("Password already copied!")
        pyperclip.copy(password)
    elif choose_pass == "medium":
        password = ""
        caratteri_med = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_med)
        print("this is your medium password: " + password)
        print()
        print("Password already copied!")
        pyperclip.copy(password)
    if choose_pass == "Difficult":
        password = ""
        caratteri_hard = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-_+=][}{:'"
        for i in range(lunghezza):
            password += random.choice(caratteri_hard)
        print("this is your difficult password: " + password)
        print()
        print("Password already copied!")
        pyperclip.copy(password)
    elif choose_pass == "difficult":
        password = ""
        caratteri_hard = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-_+=][}{:'"
        for i in range(lunghezza):
            password += random.choice(caratteri_hard)
        print("this is your difficult password: " + password)
        print()
        print("Password already copied!")
        pyperclip.copy(password)
    print("you want to restart the program?...Y/N")

    answer = input()

    if answer == "Y":
        loop()
    elif answer == "y":
        loop()

    if answer == "N":
        rosso = "\u001b[31m"
        print("See you next time!...")
        print('''
        \u001b[1m\u001b[33m|C| Guti's industries
        ''')
        input()
    elif answer == "n":
        print("See you later!...")
        print('''
        \u001b[1m\u001b[33m|C| Guti's industries
            ''')
        input()

def lingua_it():
    #inizio del programma
    print("==========================================")
    print("Benvenuti al mio generatore di password!")
    print("==========================================")
    print()
    print('''Digita la difficolta della tua password: Facile, Media, Difficile...''')
    choose_pass = input()
    lunghezza = int(input("Scegli la lunghezza della tua password: "))
    if choose_pass == "Facile":
        password = ""
        caratteri_easy = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_easy)
        print("ecco la tua password Facile: " + password)
        print()
        print("Password copiata automaticamente!")
        pyperclip.copy(password)
    elif choose_pass == "facile":
        password = ""
        caratteri_easy = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_easy)
        print("ecco la tua password Facile: " + password)
        print()
        print("Password copiata automaticamente!")
        pyperclip.copy(password)
    if choose_pass == "Media":
        password = ""
        caratteri_med = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_med)
        print("ecco la tua password Media: " + password)
        print()
        print("Password copiata automaticamente!")
        pyperclip.copy(password)
    elif choose_pass == "media":
        password = ""
        caratteri_med = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        for i in range(lunghezza):
            password += random.choice(caratteri_med)
        print("ecco la tua password Media: " + password)
        print()
        print("Password copiata automaticamente!")
        pyperclip.copy(password)
    if choose_pass == "Difficile":
        password = ""
        caratteri_hard = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-_+=][}{:'"
        for i in range(lunghezza):
            password += random.choice(caratteri_hard)
        print("ecco la tua password Difficile: " + password)
        print()
        print("Password copiata automaticamente!")
        pyperclip.copy(password)
    elif choose_pass == "difficile":
        password = ""
        caratteri_hard = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-_+=][}{:'"
        for i in range(lunghezza):
            password += random.choice(caratteri_hard)
        print("ecco la tua password Difficile: " + password)
        print()
        print("Password copiata automaticamente!")
        pyperclip.copy(password)
    print("Vuoi riavviare il programma?...S/N")


    answer = input()

    if answer == "S":
        loop()
    elif answer == "s":
        loop()

    if answer == "N":
        rosso = "\u001b[31m"
        print("Alla prossima!...")
        print('''
        \u001b[1m\u001b[33m|C| Guti's industries
        ''')
        input()
    elif answer == "n":
        print("Alla prossima!...")
        print('''
        \u001b[1m\u001b[33m|C| Guti's industries
            ''')
        input()

def loop():
    print("Welcome to my password generator choose yuor lenguage...it/en")
    print("if you want to see the changelog type '!changelog'")
    print("type !h or !help to see the instruction")

    choose_lenguage = input()
    if choose_lenguage == "it":
        lingua_it()
    elif choose_lenguage == "en":
        lingua_en()

    if choose_lenguage == "!h":
        print('''choose lenguage instruction...it/en''')
        choose_instruction = input("type here: ")

        if choose_instruction == "it":
            print('''
            -ecco tutte le informazioni sulle funzioni!
             Facile = caratteri minuscoli + numeri
             Media = caratteri minuscolo,maiuscoli e numeri
             Difficile = caratteri minuscolo,maiuscoli + numeri e caratteri speciali (es:@#{]{].<>,.:")
            ''')
            print()
            print("digita end se vuoi ritornare al menu principale e quit se vuoi uscire...")
            in3 = input()
            if in3 == "end":
                loop()
            elif in3 == "quit":
                quit()

        elif choose_instruction == "en":
            print('''
            -Here's all about the function!
             Easy = low carachters + numbers
             Medium = low carachters,up charachters end numbers
             Difficult = low carachters,up charachters + numbers end special carachters (es:@#{]{].<>,.:")
            ''')
            print()
            print("type end to return at main menu or quit to leave programm...")
            in2 = input()
            if in2 == "end":
                loop()
            elif in2 == "quit":
                quit()
    elif choose_lenguage == "!help":
        print('''choose lenguage instruction...it/en''')
        choose_instruction = input("type here: ")

        if choose_instruction == "it":
            print('''
            -ecco tutte le informazioni sulle funzioni!
             Facile = caratteri minuscoli + numeri
             Media = caratteri minuscolo,maiuscoli e numeri
             Difficile = caratteri minuscolo,maiuscoli + numeri e caratteri speciali (es:@#{]{].<>,.:")
            ''')
            print()
            print("digita end se vuoi ritornare al menu principale e quit se vuoi uscire...")
            in3 = input()
            if in3 == "end":
                loop()
            elif in3 == "quit":
                quit()

        elif choose_instruction == "en":
            print('''
            -Here's all about the function!
             Easy = low carachters + numbers
             Medium = low carachters,up charachters end numbers
             Difficult = low carachters,up charachters + numbers end special carachters (es:@#{]{].<>,.:")
            ''')
            print()
            print("type end to return at main menu or quit to leave programm...")
            in2 = input()
            if in2 == "end":
                loop()
            elif in2 == "quit":
                quit()

    if choose_lenguage == "!changelog":
        print("choose your changelog lenguage...it/en")
        changelog = input()
        if changelog == "it":
            print('''
             ecco tutti gli aggiornamenti del 30/05/2022:
            -aggiunta la funzione della lunghezza password
            -ora non cambia se si scrive media o Media ecc...
            -lo stesso vale per la funzione s e S, n e N
            -in attesa di feedback sull applicazione in modo
            da migliorarla.
            -correzione grammaticale e bug
            ''')
            print("digita end se vuoi ritornare al menu o quit se vuoi uscire!")
            menu = input()
            if menu == "end":
                loop()
            elif menu == "quit":
                quit()

        elif changelog == "en":
            print('''
            here's all of uptdate in date 30/05/2022
            -add the function of lenght password
            -add the function if you type medium or Medium the response don't change
            -wait for feedback about the program to improve that!
            -grammaticaly correction end bug
            ''')
            print("type end if you want to return to menu or quit to end this program!")
            menu = input()
            if menu == "end":
                loop()
            elif menu == "quit":
                quit()

#programm start

print("Welcome to my password generator choose yuor lenguage...it/en")
print("if you want to see the changelog type '!changelog'")
print("type !h or !help to see the instruction")

choose_lenguage = input()
if choose_lenguage == "it":
    lingua_it()
elif choose_lenguage == "en":
    lingua_en()

if choose_lenguage == "!h":
    print('''choose lenguage instruction...it/en''')
    choose_instruction = input("type here: ")

    if choose_instruction == "it":
        print('''
        -ecco tutte le informazioni sulle funzioni!
         Facile = caratteri minuscoli + numeri
         Media = caratteri minuscolo,maiuscoli e numeri
         Difficile = caratteri minuscolo,maiuscoli + numeri e caratteri speciali (es:@#{]{].<>,.:")
        ''')
        print()
        print("digita end se vuoi ritornare al menu principale e quit se vuoi uscire...")
        in3 = input()
        if in3 == "end":
            loop()
        elif in3 == "quit":
            quit()

    elif choose_instruction == "en":
        print('''
        -Here's all about the function!
         Easy = low carachters + numbers
         Medium = low carachters,up charachters end numbers
         Difficult = low carachters,up charachters + numbers end special carachters (es:@#{]{].<>,.:")
        ''')
        print()
        print("type end to return at main menu or quit to leave programm...")
        in2 = input()
        if in2 == "end":
            loop()
        elif in2 == "quit":
            quit()
elif choose_lenguage == "!help":
    print('''choose lenguage instruction...it/en''')
    choose_instruction = input("type here: ")

    if choose_instruction == "it":
        print('''
        -ecco tutte le informazioni sulle funzioni!
         Facile = caratteri minuscoli + numeri
         Media = caratteri minuscolo,maiuscoli e numeri
         Difficile = caratteri minuscolo,maiuscoli + numeri e caratteri speciali (es:@#{]{].<>,.:")
        ''')
        print()
        print("digita end se vuoi ritornare al menu principale e quit se vuoi uscire...")
        in3 = input()
        if in3 == "end":
            loop()
        elif in3 == "quit":
            quit()

    elif choose_instruction == "en":
        print('''
        -Here's all about the function!
         Easy = low carachters + numbers
         Medium = low carachters,up charachters end numbers
         Difficult = low carachters,up charachters + numbers end special carachters (es:@#{]{].<>,.:")
        ''')
        print()
        print("type end to return at main menu or quit to leave programm...")
        in2 = input()
        if in2 == "end":
            loop()
        elif in2 == "quit":
            quit()


if choose_lenguage == "!changelog":
    print("choose your changelog lenguage...it/en")
    changelog = input()
    if changelog == "it":
        print('''
         ecco tutti gli aggiornamenti del 02/06/2022:
        -aggiunta la funzione della lunghezza password
        -ora non cambia se si scrive media o Media ecc...
        -lo stesso vale per la funzione s e S, n e N
        -in attesa di feedback sull applicazione in modo
        da migliorarla.
        -correzione grammaticale e bug
        -adesso la password vieni copiata in automatico!
        -fixati alcuni bug
        ''')
        print("digita end se vuoi ritornare al menu o quit se vuoi uscire!")
        menu = input()
        if menu == "end":
            loop()
        elif menu == "quit":
            quit()

    elif changelog == "en":
        print('''
        here's all of uptdate in date 02/06/2022
        -add the function of lenght password
        -add the function if you type medium or Medium the response don't change
        -wait for feedback about the program to improve that!
        -grammaticaly correction end bug
        -now the password is already copied when you choose one!
        -fixed bug
        ''')
        print("type end if you want to return to menu or quit to end this program!")
        menu = input()
        if menu == "end":
            loop()
        elif menu == "quit":
            quit()
