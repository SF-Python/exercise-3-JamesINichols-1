def main():
    print("           MAC Manufacturer Program")
    print("------------------------")
    print("")
    
    # List of MAC prefixes and manufacturers
    mac_prefixes = [
        "00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"
    ]
    manufacturers = [
        "Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"
    ]
    
    # Get user input
    mac_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    # Check if input is in list
    if mac_input in mac_prefixes:
        index = mac_prefixes.index(mac_input)
        manufacturer = manufacturers[index]
    else:
        manufacturer = "Unknown"
    
    print(f"For {mac_input} the MAC manufacturer is {manufacturer}.")
    
if __name__ == "__main__":
    main()
