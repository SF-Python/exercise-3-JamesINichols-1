#Victor Sosa (VictorSosaRivero)
#
#Febrary 11, 2025
#MAC Manufacturer Program
#This program determine who the manufacturer is based on the 3 first Hex number of the MAC address

#Creating a List with the regitered Hex values
HexValues=["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C"]

print("MAC Manufacturer Program")
print("------------------------\n")

#User imput the Hex values that want to check
UserImput=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ").upper()

#Use if, elif, else statements to compare the User imput with the Hex values of the list and print the result
if UserImput==HexValues[0]:
    print(f"For {UserImput} the MAC manufacturer is Oracle")
elif UserImput==HexValues[1]:
    print(f"For {UserImput} the MAC manufacturer is Intel Corporation")
elif UserImput==HexValues[2]:
    print(f"For {UserImput} the MAC manufacturer is Microsoft Corporation")
elif UserImput==HexValues[3]:
    print(f"For {UserImput} the MAC manufacturer is Apple, Inc.")
elif UserImput==HexValues[4]:
    print(f"For {UserImput} the MAC manufacturer is Huawei Technologies Co.,Ltd")
elif UserImput==HexValues[5]:
    print(f"For {UserImput} the MAC manufacturer is Cisco Systems, Inc")
else:
    print(f"For {UserImput} the MAC manufacturer is Unknown")