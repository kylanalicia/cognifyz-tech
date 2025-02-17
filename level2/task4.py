
def heat_quantizer():
    # Display the main menu
    print("\nTemperature Converter: Choose Your Conversion Path")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # Get user input to choose conversion direction
    choice = input("Choose option 1 or 2: ")

    # Celsius to Fahrenheit conversion
    if choice == "1":
        # Input temperature in Celsius
        celsius = float(input("Enter temperature in Celsius: "))
        
        # Convert Celsius to Fahrenheit using the formula F = C * (9/5) + 32
        fahrenheit = (celsius * 9 / 5) + 32
        
        # Display the converted temperature in Fahrenheit
        print(f"{celsius}°C wraps to {fahrenheit:.2f}°F")

    # Fahrenheit to Celsius conversion
    elif choice == "2":
        # Input temperature in Fahrenheit
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        # Convert Fahrenheit to Celsius using the formula C = (F - 32) * (5/9)
        celsius = (fahrenheit - 32) * 5 / 9
        
        # Display the converted temperature in Celsius
        print(f"{fahrenheit}°F harmonizes to {celsius:.2f}°C")

    # Handle invalid input for menu selection
    else:
        print("Invalid choice. Clearly, you're lost in the void. Choose 1 or 2 next time.")

heat_quantizer()
