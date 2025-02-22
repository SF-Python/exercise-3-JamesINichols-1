# Ian James(JamesIan20)
# COP2002.0T1 Spring 2025
# 1/26/2025
# Exercise 2: Variables
# The purpose of this program is to ensure students know how if functions work with loops user inputs

def main(): # Used to simplify code down only to call one function into print
   
    # Header
    print("MAC Manufacturer Program")
    print("------------------------")
    print() # Prints a blank line before the input
    
    # List of known hex digits and their corresponding manufacturers
    hex_digits = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]
    manufacturers = ["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"]

    # Prompt the user to enter the hex digits
    hex_input = input("Please enter the first 6 hex digits (format as XX:XX:XX): ")

    # Initialize the manufacturer as Unknown
    manufacturer = "Unknown"

    # Loop to find the manufacturer
    for i in range(len(hex_digits)):
        if hex_input == hex_digits[i]:
            manufacturer = manufacturers[i]

    # Print the result
    print(f"For {hex_input} the MAC manufacturer is {manufacturer}")

# To call the function into effect
if __name__ == "__main__": 
    main()
