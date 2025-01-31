#!/usr/bin/env python3

# Function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54

# Function to convert centimeters to inches
def cm_to_inches(cm):
    return cm / 2.54

# Main program
def main():
    print("1. Convert inches -> cm")
    print("2. Convert cm -> inches")
    
    # Get user choice
    choice = int(input("Make your selection (1,2): "))
    
    if choice == 1:
        # Convert inches to cm
        inches = int(input("Enter inches: "))
        cm = inches_to_cm(inches)
        print(f"Number of cm: {cm}")
    
    elif choice == 2:
        # Convert cm to inches
        cm = int(input("Enter cm: "))
        inches = cm_to_inches(cm)
        print(f"Number of inches: {inches}")
    
    else:
        # Invalid selection
        print("Invalid entry")

# Run the main function
if __name__ == "__main__":
    main()
