def minutes(num:int) -> str:
    '''Converts the given value into minutes.'''
    return f'{num//60}'

def seconds(num:int) -> str:
    '''Converts the given value into seconds.'''
    return f'{num%60}' 

def time(value:int) -> str:
    '''Converts the given value into a formatted string of minutes and seconds. The minutes and seconds will be in plural or singular based on their value.'''
    min = minutes(value)
    sec = seconds(value)
    # Ternary operator is used to check if the minute and second is in plural or not
    return (f"{min} {'minute' if int(min) == 1 else 'minutes'}, {sec} {'second' if int(sec) == 1 else 'seconds'}")

if __name__ == "__main__":
    runners = {}
    print("Park Run Timer")
    print("~~~~~~~~~~~~~~")
    print("\nLet's go!\n")

    #Loops iterates unless the 'end' is encountered
    while True:
        data = input("> ")
        if data.upper() =="END":
            break
        
        try:
            # Data is entered in the format 'player_no::time_taken'
            player_no, time_taken = data.split("::")
            
            # If the player repeats it will ignore 
            if int(player_no) in runners.keys():
                print("Error in data stream. Repeated player number. Ignoring. Carry on.")
                continue
            
            # If player no and time_taken are given in correct format, it will be added in dictionary 'runners'
            if int(player_no) > 0 and int(time_taken) > 0:
                runners[int(player_no)] = int(time_taken)
            else:
                print("Error in data stream. Ignoring. Carry on")
                
        # The program will ignore any data that is not in format
        except (IndexError, ValueError):
            print("Error in data stream. Ignoring. Carry on")

    player_num = len(runners.keys())

    if player_num == 0:
        print("No data found. Nothing to do. What a pity.")

    else:
        
        print(f"\n{'Total Runner:' if player_num == 1 else 'Total Runners:'} {player_num}")

        print(f"Average Time:  {time (sum (runners.values()) // player_num)}")

        print(f"Fastest Time:  {time (min (runners.values()))}")

        print(f"Slowest Time:  {time (max (runners.values()))}")
        
        print(f"\nBest Time Here: Runner #{list (runners.keys()) [list (runners.values()).index(min(runners.values()) )]}")