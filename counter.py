def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    day_of_the_week = dict() 

    # Try except for bad input 
    try:
        with open(file_name) as file_handler: # With opens and closes file
            for line in file_handler:         # Loops through lines in file handler
                if line.startswith("From "):  # Finds lines that start with "From "
                    day_sent = line.split()[2] # Gets the thrid word (which day it was sent)
                    
                    # Sets it to 1 if it isn't in the dictionary and increments if it is
                    if day_sent not in day_of_the_week:
                        day_of_the_week[day_sent] = 1
                    else:
                        day_of_the_week[day_sent] += 1

    except:
        print(f"Bad file name : {file_name}")
        quit()

    print(day_of_the_week) # Print results

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
