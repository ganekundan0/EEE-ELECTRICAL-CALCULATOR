def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
def main():
    while True:
        print("\n=== EEE Electrical Calculator ===")
        print("1. Calculate Voltage (V = I x R)")
        print("2. Calculate Current (I = V / R)")
        print("3. Calculate Resistance (R = V / I)")
        print("4. Calculate Power (P = V x I)")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            current = get_number("Enter current (A): ")
            resistance = get_number("Enter resistance (Ohms): ")
            print(f"Voltage = {current * resistance:.4g} V")
 
        elif choice == "2":
            voltage = get_number("Enter voltage (V): ")
            resistance = get_number("Enter resistance (Ohms): ")
            if resistance == 0:
                print("Error: Resistance cannot be zero!")
            else:
                print(f"Current = {voltage / resistance:.4g} A")
        elif choice == "3":
            voltage = get_number("Enter voltage (V): ")
            current = get_number("Enter current (A): ")
            if current == 0:
                print("Error: Current cannot be zero!")
            else:
                print(f"Resistance = {voltage / current:.4g} Ohms")
        elif choice == "4":
            voltage = get_number("Enter voltage (V): ")
            current = get_number("Enter current (A): ")
            print(f"Power = {voltage * current:.4g} W")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")
if __name__ == "__main__":
    main()
    
