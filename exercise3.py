def main():
    # Display program header
    print("MAC Manufacturer Program")
    print("------------------------")
    
    # Ask the user for input
    mac_address = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # List of known MAC address prefixes and corresponding manufacturers
    mac_codes = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]
    manufacturers = ["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.",
                     "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"]

    # Remove any unwanted spaces or characters in the input
    mac_address = mac_address.strip()

    # Check if the input MAC address matches any known MAC address prefix
    if mac_address in mac_codes:
        index = mac_codes.index(mac_address)
        print(f"For {mac_address} the MAC manufacturer is {manufacturers[index]}.")
    else:
        print(f"For {mac_address} the MAC manufacturer is Unknown.")

# Call the main function
if __name__ == "__main__":
    main()
