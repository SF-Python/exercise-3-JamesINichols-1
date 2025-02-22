def main():
    # Print program header
    print("MAC Manufacturer Program")
    print("------------------------")
    print()

    # Get user input for MAC hex values
    mac_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Define known MAC prefixes and corresponding manufacturers
    mac_prefixes = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]
    manufacturers = ["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"]

    # Default manufacturer value
    manufacturer = "Unknown"

    # Check for matching MAC prefix
    for i in range(len(mac_prefixes)):
        if mac_input.upper() == mac_prefixes[i].upper():
            manufacturer = manufacturers[i]
            break

    # Print result
    print("For {} the MAC manufacturer is {}.".format(mac_input, manufacturer))


if __name__ == "__main__":
    main()
