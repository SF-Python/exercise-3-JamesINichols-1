# Ishaan Patel
# COP2002-0T1
# Feb 16, 2025
# Exercise 3
# Program asks the user for a mac address as input then uses if elif statements to determine the
# manufacturer of the MAC address.


def main():
    # Header
    print("MAC Manufacturer Program")
    print("------------------------")
    print("")
    
    #input from user
    userMac = input("Enter the first 6 values of the Mac address (format as XX:XX:XX):  ")

    #if elif and else statements
    if userMac == "00:00:17":
        print(f"For {userMac} the MAC manufacturer is Oracle.")
    elif userMac == "00:07:E9":
        print(f"For {userMac} the MAC manufacturer is Intel Corportation.")
    elif userMac == "04:27:28":
        print(f"For {userMac} the MAC manufacturer is Microsoft Corportation.")
    elif userMac == "04:26:65":
        print(f"For {userMac} the MAC manufacturer is Apple Inc.")
    elif userMac == "04:33:89":
        print(f"For {userMac} the MAC manufacturer is Huawei Technologies Co. Ltd.")
    else:
        print("This MAC manufacturer is unknown.")

if (__name__ == "__main__"):
    main()