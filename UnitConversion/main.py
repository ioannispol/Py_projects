import os
import length


def main():
    while True:
        os.system('cls')
        userInput = input("Choose the conversion\n1. From Km to Miles\n2. From Miles to Km\n"
                          "3. From Nautical Miles to Km\n4.Press Enter to continue or press Esc to exit: ")

        if userInput == '1':
            print(length.km())
        elif userInput == '2':
            print(length.miles())
        elif userInput == '3':
            print(length.n_miles())
        elif userInput == 'Enter' or 'Esc':
            print("The program has stoped")
            quit()

    return main()


if __name__ == '__main__':
    main()
