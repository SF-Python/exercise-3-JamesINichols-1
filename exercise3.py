# exercise3.py
def main():
    hex_digits = input("Please enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    if hex_digits == "00:00:17":
        manufacturer = "Oracle"
    elif hex_digits == "00:07:E9":
        manufacturer = "Intel Corporation"
    elif hex_digits == "04:27:28":
        manufacturer = "Microsoft Corporation"
    elif hex_digits == "04:26:65":
        manufacturer = "Apple, Inc."
    elif hex_digits == "04:33:89":
        manufacturer = "Huawei Technologies Co.,Ltd"
    elif hex_digits == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"
    else:
        manufacturer = "<Not found>"

    print("For the MAC address, the manufacturer is " + manufacturer)

if __name__ == "__main__":
    main()
