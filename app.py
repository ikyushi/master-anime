import json
import os
import sys

choice = int
move = int

def initData(): 
    f = open('storage.json', 'r')
    data = json.load(f)
    return data

data = initData()

def clear():
    os.system('clear')

while choice != 6:
    clear()
    print("Master Anime")
    print("by ikyushi")
    print("----------------------------------------------------------------")
    print("Please select your choice...")
    print("1. Show all 'WATCHED' anime")
    print("2. Show all 'WATCHING' anime")
    print("3. Show all 'UNWATCHED' anime")
    print("4. Show all 'DROPPED' anime")
    print("5. Edit lists")
    print("6. Exit")
    print("----------------------------------------------------------------")
    choice = int(input("Your choice: "))
    if choice == 1:
        clear()
        print("Master Anime")
        print("by ikyushi")
        print("----------------------------------------------------------------")
        print("'WATCHED' anime")
        for i in data['watched']:
            print(i)
        print("----------------------------------------------------------------")
        input("Press enter to return...")
    elif choice == 2:
        clear()
        print("Master Anime")
        print("by ikyushi")
        print("----------------------------------------------------------------")
        print("'WATCHING' anime")
        for i in data['watching']:
            print(i)
        print("----------------------------------------------------------------")
        input("Press enter to return...")
    elif choice == 3:
        clear()
        print("Master Anime")
        print("by ikyushi")
        print("----------------------------------------------------------------")
        print("'UNWATCHED' anime")
        for i in data['unwatched']:
            print(i)
        print("----------------------------------------------------------------")
        input("Press enter to return...")
    elif choice == 4:
        clear()
        print("Master Anime")
        print("by ikyushi")
        print("----------------------------------------------------------------")
        print("'DROPPED' anime")
        for i in data['dropped']:
            print(i)
        print("----------------------------------------------------------------")
        input("Press enter to return...")
    elif choice == 5:
        clear()
        print("Master Anime")
        print("by ikyushi")
        print("----------------------------------------------------------------")
        print("Please select your choice...")
        print("1. Add anime")
        print("2. Remove anime")
        print("3. Move anime")
        print("4. Drop anime")
        print("5. Return")
        print("----------------------------------------------------------------")
        move = int(input("Your choice: "))
        if move == 1:
            clear()
            print("Master Anime")
            print("by ikyushi")
            print("----------------------------------------------------------------")
            print("Please select your choice...")
            print("1. Add 'WATCHED' anime")
            print("2. Add 'WATCHING' anime")
            print("3. Add 'UNWATCHED' anime")
            print("4. Add 'DROPPED' anime")
            print("5. Return")
            print("----------------------------------------------------------------")
            move = int(input("Your choice: "))
            if move == 1:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to add...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watched'].append(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 2:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to add...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watching'].append(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 3:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to add...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['unwatched'].append(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 4:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to add...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['dropped'].append(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
        elif move == 2:
            clear()
            print("Master Anime")
            print("by ikyushi")
            print("----------------------------------------------------------------")
            print("Please select your choice...")
            print("1. Remove 'WATCHED' anime")
            print("2. Remove 'WATCHING' anime")
            print("3. Remove 'UNWATCHED' anime")
            print("4. Remove 'DROPPED' anime")
            print("5. Return")
            print("----------------------------------------------------------------")
            move = int(input("Your choice: "))
            if move == 1:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to remove...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watched'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 2:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to remove...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watching'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 3:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to remove...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['unwatched'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 4:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to remove...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['dropped'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
        elif move == 3:
            clear()
            print("Master Anime")
            print("by ikyushi")
            print("----------------------------------------------------------------")
            print("Please select your choice...")
            print("1. Move 'WATCHED' anime")
            print("2. Move 'WATCHING' anime")
            print("3. Move 'UNWATCHED' anime")
            print("4. Move 'DROPPED' anime")
            print("5. Return")
            print("----------------------------------------------------------------")
            move = int(input("Your choice: "))
            if move == 1:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to move...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watched'].remove(anime)
                print("Please select your choice...")
                print("1. Move to 'WATCHING' anime")
                print("2. Move to 'UNWATCHED' anime")
                print("3. Move to 'DROPPED' anime")
                print("4. Return")
                print("----------------------------------------------------------------")
                move = int(input("Your choice: "))
                if move == 1:
                    data['watching'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 2:
                    data['unwatched'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 3:
                    data['dropped'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
            elif move == 2:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to move...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watching'].remove(anime)
                print("Please select your choice...")
                print("1. Move to 'WATCHED' anime")
                print("2. Move to 'UNWATCHED' anime")
                print("3. Move to 'DROPPED' anime")
                print("4. Return")
                print("----------------------------------------------------------------")
                move = int(input("Your choice: "))
                if move == 1:
                    data['watched'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 2:
                    data['unwatched'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 3:
                    data['dropped'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
            elif move == 3:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to move...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['unwatched'].remove(anime)
                print("Please select your choice...")
                print("1. Move to 'WATCHED' anime")
                print("2. Move to 'WATCHING' anime")
                print("3. Move to 'DROPPED' anime")
                print("4. Return")
                print("----------------------------------------------------------------")
                move = int(input("Your choice: "))
                if move == 1:
                    data['watched'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 2:
                    data['watching'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 3:
                    data['dropped'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
            elif move == 4:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to move...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['dropped'].remove(anime)
                print("Please select your choice...")
                print("1. Move to 'WATCHED' anime")
                print("2. Move to 'WATCHING' anime")
                print("3. Move to 'UNWATCHED' anime")
                print("4. Return")
                print("----------------------------------------------------------------")
                move = int(input("Your choice: "))
                if move == 1:
                    data['watched'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 2:
                    data['watching'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
                elif move == 3:
                    data['unwatched'].append(anime)
                    with open('storage.json', 'w') as f:
                        json.dump(data, f)
                    input("Press enter to return...")
            elif move == 5:
                pass
        elif move == 4:
            clear()
            print("Master Anime")
            print("by ikyushi")
            print("----------------------------------------------------------------")
            print("Please select your choice...")
            print("1. Drop 'WATCHED' anime")
            print("2. Drop 'WATCHING' anime")
            print("3. Drop 'UNWATCHED' anime")
            print("4. Drop 'DROPPED' anime")
            print("5. Return")
            print("----------------------------------------------------------------")
            move = int(input("Your choice: "))
            if move == 1:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to drop...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watched'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 2:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to drop...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['watching'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 3:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to drop...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['unwatched'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 4:
                clear()
                print("Master Anime")
                print("by ikyushi")
                print("----------------------------------------------------------------")
                print("Please enter the name of the anime you want to drop...")
                print("----------------------------------------------------------------")
                anime = input("Anime name: ")
                data['dropped'].remove(anime)
                with open('storage.json', 'w') as f:
                    json.dump(data, f)
                input("Press enter to return...")
            elif move == 5:
                pass
        elif move == 5:
            pass
        elif move == 6:
            break