print("____________________________________________")
print("This system can change any number in any system to another system")
print("Systems:\n - Decimal\n - Binary\n - Octa\n - Hexadecimal\n - ASCII\n")

# Start function (get_system)
def get_system():
    while True:
        # Input and normalize
        name_system_from = input("Enter the current system: ").strip().lower()
        name_system_to = input("Enter the system to change to: ").strip().lower()

        # Decimal to Binary
        if name_system_from == "decimal" and name_system_to == "binary":
            decimal_num = int(input("Enter decimal number to convert to binary: "))
            binary_num = bin(decimal_num)[2:]
            print(f"Decimal number {decimal_num} in binary is {binary_num}")
            break
        
        # Decimal to Octa
        elif name_system_from == "decimal" and name_system_to == "octa":
            decimal_num = int(input("Enter decimal number to convert to octa: "))
            octa_num = oct(decimal_num)[2:]
            print(f"Decimal number {decimal_num} in octa is {octa_num}")
            break
        
        # Decimal to Hexadecimal
        elif name_system_from == "decimal" and name_system_to == "hexadecimal":
            decimal_num = int(input("Enter decimal number to convert to hexadecimal: "))
            hexa_num = hex(decimal_num)[2:]
            print(f"Decimal number {decimal_num} in hexadecimal is {hexa_num}")
            break

        # Decimal to ASCII
        elif name_system_from == "decimal" and name_system_to == "ascii":
            decimal_num = int(input("Enter decimal number to convert to ASCII: "))
            if 0 <= decimal_num <= 127:  # Valid ASCII range
                ascii_char = chr(decimal_num)
                print(f"Decimal number {decimal_num} in ASCII is '{ascii_char}'")
            else:
                print("Decimal number out of ASCII range (0-127).")
            break

        # Binary to Decimal
        elif name_system_from == "binary" and name_system_to == "decimal":
            binary_num = input("Enter binary number to convert to decimal: ")
            decimal_num = int(binary_num, 2)
            print(f"Binary number {binary_num} in decimal is {decimal_num}")
            break

        # Binary to Octa
        elif name_system_from == "binary" and name_system_to == "octa":
            binary_num = input("Enter binary number to convert to octa: ")
            decimal_num = int(binary_num, 2)
            octa_num = oct(decimal_num)[2:]
            print(f"Binary number {binary_num} in octa is {octa_num}")
            break

        # Binary to Hexadecimal
        elif name_system_from == "binary" and name_system_to == "hexadecimal":
            binary_num = input("Enter binary number to convert to hexadecimal: ")
            decimal_num = int(binary_num, 2)
            hexa_num = hex(decimal_num)[2:]
            print(f"Binary number {binary_num} in hexadecimal is {hexa_num}")
            break

        # Binary to ASCII
        elif name_system_from == "binary" and name_system_to == "ascii":
            binary_num = input("Enter binary number to convert to ASCII: ")
            decimal_num = int(binary_num, 2)
            if 0 <= decimal_num <= 127:  # Valid ASCII range
                ascii_char = chr(decimal_num)
                print(f"Binary number {binary_num} in ASCII is '{ascii_char}'")
            else:
                print("Binary number out of ASCII range (0-127).")
            break

        # Octa to Decimal
        elif name_system_from == "octa" and name_system_to == "decimal":
            octa_num = input("Enter octa number to convert to decimal: ")
            decimal_num = int(octa_num, 8)
            print(f"Octa number {octa_num} in decimal is {decimal_num}")
            break

        # Octa to Binary
        elif name_system_from == "octa" and name_system_to == "binary":
            octa_num = input("Enter octa number to convert to binary: ")
            decimal_num = int(octa_num, 8)
            binary_num = bin(decimal_num)[2:]
            print(f"Octa number {octa_num} in binary is {binary_num}")
            break

        # Octa to Hexadecimal
        elif name_system_from == "octa" and name_system_to == "hexadecimal":
            octa_num = input("Enter octa number to convert to hexadecimal: ")
            decimal_num = int(octa_num, 8)
            hexa_num = hex(decimal_num)[2:]
            print(f"Octa number {octa_num} in hexadecimal is {hexa_num}")
            break

        # Octa to ASCII
        elif name_system_from == "octa" and name_system_to == "ascii":
            octa_num = input("Enter octa number to convert to ASCII: ")
            decimal_num = int(octa_num, 8)
            if 0 <= decimal_num <= 127:  # Valid ASCII range
                ascii_char = chr(decimal_num)
                print(f"Octa number {octa_num} in ASCII is '{ascii_char}'")
            else:
                print("Octa number out of ASCII range (0-127).")
            break

        # Hexadecimal to Decimal
        elif name_system_from == "hexadecimal" and name_system_to == "decimal":
            hexa_num = input("Enter hexadecimal number to convert to decimal: ")
            decimal_num = int(hexa_num, 16)
            print(f"Hexadecimal number {hexa_num} in decimal is {decimal_num}")
            break

        # Hexadecimal to Binary
        elif name_system_from == "hexadecimal" and name_system_to == "binary":
            hexa_num = input("Enter hexadecimal number to convert to binary: ")
            decimal_num = int(hexa_num, 16)
            binary_num = bin(decimal_num)[2:]
            print(f"Hexadecimal number {hexa_num} in binary is {binary_num}")
            break

        # Hexadecimal to Octa
        elif name_system_from == "hexadecimal" and name_system_to == "octa":
            hexa_num = input("Enter hexadecimal number to convert to octa: ")
            decimal_num = int(hexa_num, 16)
            octa_num = oct(decimal_num)[2:]
            print(f"Hexadecimal number {hexa_num} in octa is {octa_num}")
            break

        # Hexadecimal to ASCII
        elif name_system_from == "hexadecimal" and name_system_to == "ascii":
            hexa_num = input("Enter hexadecimal number to convert to ASCII: ")
            decimal_num = int(hexa_num, 16)
            if 0 <= decimal_num <= 127:  # Valid ASCII range
                ascii_char = chr(decimal_num)
                print(f"Hexadecimal number {hexa_num} in ASCII is '{ascii_char}'")
            else:
                print("Hexadecimal number out of ASCII range (0-127).")
            break

        # ASCII to Decimal
        elif name_system_from == "ascii" and name_system_to == "decimal":
            ascii_char = input("Enter ASCII character to convert to decimal: ")
            if len(ascii_char) == 1:  # Ensure only a single character is entered
                decimal_num = ord(ascii_char)
                print(f"ASCII character '{ascii_char}' in decimal is {decimal_num}")
            else:
                print("Please enter a single ASCII character.")
            break

        # ASCII to Binary
        elif name_system_from == "ascii" and name_system_to == "binary":
            ascii_char = input("Enter ASCII character to convert to binary: ")
            if len(ascii_char) == 1:  # Ensure only a single character is entered
                decimal_num = ord(ascii_char)
                binary_num = bin(decimal_num)[2:]
                print(f"ASCII character '{ascii_char}' in binary is {binary_num}")
            else:
                print("Please enter a single ASCII character.")
            break

        # ASCII to Octa
        elif name_system_from == "ascii" and name_system_to == "octa":
            ascii_char = input("Enter ASCII character to convert to octa: ")
            if len(ascii_char) == 1:  # Ensure only a single character is entered
                decimal_num = ord(ascii_char)
                octa_num = oct(decimal_num)[2:]
                print(f"ASCII character '{ascii_char}' in octa is {octa_num}")
            else:
                print("Please enter a single ASCII character.")
            break

        # ASCII to Hexadecimal
        elif name_system_from == "ascii" and name_system_to == "hexadecimal":
            ascii_char = input("Enter ASCII character to convert to hexadecimal: ")
            if len(ascii_char) == 1:  # Ensure only a single character is entered
                decimal_num = ord(ascii_char)
                hexa_num = hex(decimal_num)[2:]
                print(f"ASCII character '{ascii_char}' in hexadecimal is {hexa_num}")
            else:
                print("Please enter a single ASCII character.")
            break

        # Unsupported System Message
        else:
            print("Please enter a valid system and try again.")

    # Ask to continue or quit
    solve_q = input("Type 'Yes' to continue, or any other key to quit: ").strip().title()
    if solve_q == "Yes":
        return get_system()
    else:
        print("Thanks for using the converter!")

get_system()
