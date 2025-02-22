# Jeremiah Riche
# 2/17/2025 - 11:37PM
# Exercise 3: If Statements
def main():
    print("MAC Manufacturer Program")
    print("------------------------")
    print()

    # Prompts.
    mac_address = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    #Manufacturer's
    manufacturer = "Unknown"

    # MAC-ADRESSES
    if mac_address == "00:00:17":
        manufacturer = "Oracle"
    if mac_address == "00:07:E9":
        manufacturer = "Intel Corporation"
    if mac_address == "04:27:28":
        manufacturer = "Microsoft Corporation"
    if mac_address == "04:26:65":
        manufacturer = "Apple, Inc."
    if mac_address == "04:33:89":
        manufacturer = "Huawei Technologies Co., Ltd"
    if mac_address == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"

    #Result's
    print(f"For {mac_address} the MAC manufacturer is {manufacturer}")

if __name__ == "__main__":
    main()
