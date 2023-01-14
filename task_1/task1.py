from random import shuffle, choice

GAMES = ["football", "basketball", "cricket", "boxing", "tennis", "hockey", "rugby"]
UTENSILS = ["cup","spoon", "plate", "bowl"]
FRUITS = ["apple", "banana", "orange"]
LISTS = [GAMES, UTENSILS, FRUITS]

def psw_generator(num:int) -> None:
    '''Generates given number of unique passwords'''
    print()
    passwords = []
    password = ''
    count = 1
    
    while True:
        # Shuffle the constant 'LISTS'
        shuffle(LISTS)
        for lst in LISTS:
            password += choice(lst)

        # If the password is repeated it will be skipped     
        if password in passwords:
            password = ''
            continue

        print(f"{count:4} --> {password:2}")
        count += 1

        # Add the printed password to passwords list
        passwords.append(password)
        password = ''

        # When the required number of password is printed the loops breaks
        if count == (num+1):
            break

if __name__ == "__main__":
    print("Password Generator")
    print("==================\n")
    
    #Loops iterates unless the user inputs the value between 1 to 24
    while True:
        try:
            num = int(input("How many passwords are needed?: "))
            if 0< num <= 24:
                psw_generator(num)
                break
            else:
                print("Please enter a value between 1 and 24.")
        
        except ValueError:
            print("Please enter a number.")