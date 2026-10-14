print("=== EEE Electrical Calculator ===")
print("1. Calculate Voltage")
print("2. Calculate Current")
print("3. Calculate Resistance")
print("4. Calculate Power")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ohms): "))
    print("Voltage =", current * resistance, "V")

elif choice == "2":
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (Ohms): "))
    print("Current =", voltage / resistance, "A")

elif choice == "3":
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))
    print("Resistance =", voltage / current, "Ohms")

elif choice == "4":
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))
    print("Power =", voltage * current, "W")

else:
    print("Invalid choice!")
