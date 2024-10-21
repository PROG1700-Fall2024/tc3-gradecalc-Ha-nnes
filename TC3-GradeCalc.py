Student: Hannesm Meyer-Rahlfs
# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.

def grade_to_numeric(letter_grade, modifier=None):
    # store grade values in a dictionary (my brother taught me this while I was sick over the last two weeks)
    grade_values = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    # Convert the letter grade to uppercase 
    letter_grade = letter_grade.upper()

    # Check for validity of the letter grade
    if letter_grade not in grade_values:
        return "Invalid letter grade!"  # error message if invalid

    # get base numeric value from the dictionary
    numeric_value = grade_values[letter_grade]

    # Apply modifier to the numeric value if applicable
    if modifier == '+':
        if letter_grade != 'A':  
            numeric_value += 0.3  
    elif modifier == '-':
        if letter_grade != 'F': 
            numeric_value -= 0.3  

    return numeric_value  # Return the calculated numeric value

def main():
    # Introduction message
    print("Welcome to the Grade Converter!")
    print("This program converts letter grades (A-F) into numeric values.")

    # Get the letter grade from the user
    letter_grade = input("Please enter your letter grade (A, B, C, D, or F): ")

    # Get the optional modifier from the user
    modifier = input("If you have a modifier, enter it (+ or -). If not, just press Enter: ").strip()

    print(f"\nYou entered the letter grade: '{letter_grade}'")
    print(f"You entered the modifier: '{modifier}'")

    # Calculate the numeric value based on user input
    numeric_value = grade_to_numeric(letter_grade, modifier)

    # Check if the result is an error message or a valid numeric value
    if isinstance(numeric_value, str):
        print(numeric_value)  
    else:
        # Display the resulting numeric value to the user
        print(f"The numeric value corresponding to your grade is: {numeric_value:.2f}")

    # Closing message
    print("Thank you for using the Grade Converter!")


main()
